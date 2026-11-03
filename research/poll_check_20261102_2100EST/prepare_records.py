"""Extract and verify the scheduled evening increment; no network or model writes.

Run with .venv/bin/python. --append adds reviewed raw records to the existing
November 2 acquisition, whose importer owns chronological replay and exports.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse,hashlib,json,re,sys,zipfile,xml.etree.ElementTree as ET
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
sys.path.insert(0,str(ROOT/'src'))
from election_modeling.cycles import RACES_2026_BY_ID
from election_modeling.nominees import NOMINEES_2026_BY_RACE

def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,allow_nan=False).encode()).hexdigest()
def write(path,value):path.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
class Tables(HTMLParser):
    def __init__(self):super().__init__();self.tables=[];self.table=self.row=self.cell=None
    def handle_starttag(self,tag,attrs):
        if tag=='table':self.table=[]
        elif tag=='tr' and self.table is not None:self.row=[]
        elif tag in ('th','td') and self.row is not None:self.cell=[]
    def handle_data(self,data):
        if self.cell is not None:self.cell.append(data)
    def handle_endtag(self,tag):
        if tag in ('th','td') and self.cell is not None:self.row.append(' '.join(''.join(self.cell).split()));self.cell=None
        elif tag=='tr' and self.row is not None:self.table.append(self.row);self.row=None
        elif tag=='table' and self.table is not None:self.tables.append(self.table);self.table=None

def html_tables(name):
    p=Tables();p.feed((BASE/'sources'/name).read_text());return p.tables

def workbook_cells():
    ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    with zipfile.ZipFile(BASE/'sources/focaldata-nov02.xlsx') as z:
        strings=[''.join(n.itertext()) for n in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',ns)] if 'xl/sharedStrings.xml' in z.namelist() else []
        cells={}
        for c in ET.fromstring(z.read('xl/worksheets/sheet4.xml')).findall('.//s:c',ns):
            v=c.find('s:v',ns)
            if c.get('t')=='inlineStr':cells[c.get('r')]=''.join(c.find('s:is',ns).itertext())
            elif v is not None:cells[c.get('r')]=strings[int(v.text)] if c.get('t')=='s' else float(v.text)
    return cells

def prepare():
    downloads=[r for r in json.loads((BASE/'download-inventory.json').read_text()) if r['status']=='downloaded']
    for item in downloads:assert hashlib.sha256((ROOT/item['file']).read_bytes()).hexdigest()==item['sha256']
    urls={Path(r['file']).name:r['url'] for r in downloads}
    rows=[];decisions={}
    def add(race_id,poll_id,pollster,start,end,pop,total,vals,ns,artifact,location,note,deff=1.5,basis='party_id',pub='2026-11-02',bounds=None,sponsor=None,extras=None):
        race=RACES_2026_BY_ID[race_id];nom=NOMINEES_2026_BY_RACE[race_id]
        r={'race_id':race_id,'state':race.state,'office':race.office,'poll_id':poll_id,'sample_id':poll_id,'pollster':pollster,'sponsor':sponsor,'candidate_a':nom.republican.name,'candidate_b':nom.candidate_b.name,'candidate_a_party':nom.republican.party,'candidate_b_party':nom.candidate_b.party,'field_start':start,'field_date':end,'publication_date':pub,'population':pop,'reported_total_n':total,'crosstab_basis':basis,'subgroup_n_method':'reported_unweighted' if ns else 'missing','source_url':urls[artifact],'source_location':location,'evidence_excerpt':'Conditional candidate A/B support within R,D,I groups: '+str(vals),'evidence_path':str((BASE/'sources'/artifact).relative_to(ROOT)),'notes':note,'ballot_question_stage':'First-choice full ballot; no analyst undecided allocation'}
        for party,pair,n in zip(['republican','democratic','independent'],vals,ns or [None]*3):
            r[party+'_a'],r[party+'_b'],r[party+'_n']=pair[0]/100,pair[1]/100,n
            assert 0<=r[party+'_a'] and 0<=r[party+'_b'] and sum(pair)<=100
        if extras:r.update(extras)
        review={'action':'accept','reason':'Verified all six candidate-support cells in the archived original source. '+note,'record_sha256':digest(r)}
        if ns:review['precision']={'method':'reported_unweighted','design_effect':deff,'evidence':note}
        else:review['precision']={'method':'assumed_covariance','cell_sd':.05,'within_group_correlation':-.5,'evidence':'Applicable subgroup counts unavailable. Retain null Ns and the established provisional 5pp cell SD / -0.5 within-pair correlation covariance; no fabricated counts.'}
        if basis=='party_basis_unspecified':review['allow_proxy']=True
        if bounds:review['publication_date_bounds']=bounds
        rows.append(r);decisions[race_id+'/'+poll_id]=review
        return r,review
    # The second banner row distinguishes actual Party ID from file/model groups.
    tables=html_tables('survey160.html')
    for state,sen,gov,deff,full_n in [('ks',0,2,1.78,1353),('oh',14,16,3.63,1174),('me',28,30,2.30,1342),('mn',42,44,2.04,1423)]:
        for office,idx in [('sen',sen),('gov',gov)]:
            race_id=state+'_'+office;t=tables[idx]
            cols=[20,19,21] if state=='mn' else [19,18,20]
            assert [t[1][c] for c in cols]==['Republican','Democrat','Independent/Other']
            assert t[2][0]=='Unweighted n'
            assert t[3][0].endswith('(D)') and t[4][0].endswith('(R)')
            nom=NOMINEES_2026_BY_RACE[race_id]
            assert t[4][0].removesuffix(' (R)')==nom.republican.name
            assert t[3][0].removesuffix(' (D)')==nom.candidate_b.name
            vals=[(float(t[4][c].strip('%')),float(t[3][c].strip('%'))) for c in cols];ns=[int(t[2][c]) for c in cols]
            note=f'Actual self-reported Party ID columns, full RV question base, NOT the adjacent LV headline or SEN_LEAN/GOV_LEAN variant. Independent/Other pools independent/something else/unsure as published; no analyst reassignment of party leaners. Exact question-specific unweighted subgroup Ns retained; source full-state design effect {deff} applied provisionally to each subgroup, not subgroup-calibrated. Question-base totals can differ from full state sample {full_n}; unclassified/missing party answers remain outside R/D/I. Other candidates and undecided remain outside the pair.'
            add(race_id,'survey160-20261101','Survey 160','2026-10-27','2026-11-01','RV',int(t[2][1]),vals,ns,'survey160.html',f'HTML table {idx+1} (zero-based {idx}), first-choice {office.upper()}, Party ID columns; Unweighted n and named candidate rows',note,deff=deff,sponsor='Survey 160',extras={'reported_full_state_n':full_n,'source_table_index':idx,'source_party_column_indices':cols})
    r,rev=add('us_house_generic','ipsos-20261102','Reuters/Ipsos','2026-10-29','2026-11-02','LV',1212,[(96,3),(1,97),(36,53)],[413,421,378],'ipsos-nov02.pdf','PDF page2 TM3287Y24, Base Likely Voters; Rep LV, Dem LV, Ind/Other LV columns','Lean-inclusive candidate ballot; one LV version, RV alternative omitted. Exact applicable unweighted bases413/421/378. Ind/Other source reporting group retained; party-leaner classification not independently specified. Overall source DEFF1.03 does not override the existing conservative unweighted-base floor1.5; this is not a subgroup-calibrated DEFF.',deff=1.5,sponsor='Reuters')
    r['ballot_question_stage']='Source ballot including candidate leaners; no analyst allocation';rev['record_sha256']=digest(r)
    # Independently verified against openpyxl read-only: source cached cell values.
    c=workbook_cells();assert c['A144'].startswith('Q66 In the elections');assert c['A145']=='Base: All respondents'
    groups=[['AV','AW'],['AQ','AR'],['AS','AT','AU']]
    labels=[['Not very strong Republican','Strong Republican'],['Strong Democrat','Not very strong Democrat'],['Lean Democrat','Independent','Lean Republican']]
    vals=[];ns=[];pool=[]
    for cols,labs in zip(groups,labels):
        assert [c[x+'146'] for x in cols]==labs
        den=sum(c[x+'158'] for x in cols)
        aa=sum(c[x+'150'] for x in cols)/den;bb=sum(c[x+'148'] for x in cols)/den
        # Counts and displayed conditional proportions must agree.
        assert abs(aa-sum(c[x+'149']*c[x+'158'] for x in cols)/den)<1e-12
        assert abs(bb-sum(c[x+'147']*c[x+'158'] for x in cols)/den)<1e-12
        n=int(sum(c[x+'157'] for x in cols));ns.append(n);vals.append((aa*100,bb*100))
        pool.append({'labels':labs,'columns':cols,'weighted_base':den,'raw_n':n,'candidate_a_weighted_count':aa*den,'candidate_b_weighted_count':bb*den})
    assert ns==[916,771,646] and c['B157']==2444
    add('us_house_generic','focaldata-20261101','Focaldata/Financial Times','2026-10-30','2026-11-01','A',2444,vals,ns,'focaldata-nov02.xlsx','Workbook Overall Q66 rows144–158; AQ:AW Party ID; candidate weighted counts rows148/150 divided by weighted bases158; raw Ns157','All-adult first-choice party columns, not LV/RV headline or forced-choice/leaned alternatives. Pool strong/not-strong into R/D; both partisan leaner groups remain with Independent, matching prior Focaldata records. Exact weighted counts/bases determine pooled support; summed raw unweighted counts determine measurement bases. R/D/I Ns sum2333 of2444; unknown-party respondents excluded from these groups. Existing provisional DEFF2.0 retained, not calibrated subgroup precision.',deff=2.0,sponsor='Financial Times',extras={'pooling_details':pool})
    # Iowa article has all six cells despite a stale October 2 date label.
    # Honest earliest/latest bounds use field completion and this primary capture.
    ia=(BASE/'sources/rasmussen-ia.html').read_text()
    assert 'Friday, October 02, 2026' in ia and 'October 27-31, 2026' in ia
    add('ia_sen','rasmussen-20261031','Rasmussen Reports','2026-10-27','2026-10-31','LV',901,[(86,8),(8,89),(37,49)],None,'rasmussen-ia.html','Public release narrative, complete named candidate support across Republican, Democrat and unaffiliated voters','Complete six-cell public narrative; exact party classification and leaner handling unspecified, previously authorized proxy. Applicable subgroup counts missing; no exact Ns inferred from total901. Primary page retains stale October2 dateline preceding October27–31 fieldwork: do not treat it as release date. First publication unknown; conservative bounds October31–November2, newly available in this scheduled capture. Separate premium table401 was not retried or bypassed.',basis='party_basis_unspecified',pub=None,bounds=['2026-10-31','2026-11-02'],extras={'publication_date_discrepancy':'Primary label October2 precedes fieldwork; publication bounded by field end and November2 capture','availability_date':'2026-11-02','fieldwork_organization':'Pulse Opinion Research'})
    oh_tables=html_tables('rasmussen-oh-crosstabs.html')
    # Full primary HTML table is independently checked against source-rendered table.
    ohtext=' '.join((BASE/'sources/rasmussen-oh-crosstabs.html').read_text().split())
    assert 'October 27-31, 2026' in ohtext and oh_tables
    ot=oh_tables[0];assert ot[4][12:15]==['Democrat','Republican','Independent']
    assert [ot[6][x] for x in [14,13,15]]==['83%','11%','35%']
    assert [ot[5][x] for x in [15,14,16]]==['12%','84%','54%']
    add('oh_sen','rasmussen-20261031','Rasmussen Reports','2026-10-27','2026-10-31','LV',1119,[(83,12),(11,84),(35,54)],None,'rasmussen-oh-crosstabs.html','First Senate ballot, Party Democrat/Republican/Independent columns; Another party separate','Party classification source/leaners unspecified, authorized proxy. Independent and Another party separate; do not pool Another party. Source full LV total1119 and rounded composition40R/28D/30I/2Other are not exact group counts; keep subgroup Ns null and established conservative covariance. Public original table accessible; no paywall bypass.',basis='party_basis_unspecified',extras={'release_url':urls['rasmussen-oh.html'],'fieldwork_organization':'Pulse Opinion Research'})
    ia_gov=(BASE/'sources/rasmussen-ia-gov.html').read_text()
    dates=re.findall(r'<p class="mb-0 align-self-end align-items-start">(.*?)</p>',ia_gov)
    assert dates and 'November 02, 2026' in dates[0],dates
    add('ia_gov','rasmussen-20261031','Rasmussen Reports','2026-10-27','2026-10-31','LV',901,[(81,13),(9,89),(35,57)],None,'rasmussen-ia-gov.html','Public governor release narrative, Sand and Lahn support within Democrat, Republican and unaffiliated groups','Complete six-cell public narrative; exact party classification and leaner handling unspecified, authorized proxy. Same901-person Iowa survey as Senate; separate offices updated once each. Applicable subgroup counts missing, retained null; no sample-size fabrication or undecided allocation.',basis='party_basis_unspecified',extras={'fieldwork_organization':'Pulse Opinion Research'})
    assert len(rows)==13 and len(decisions)==13
    before=json.loads((BASE/'baseline/before-0-2026_normalized_polls.json').read_text())['polls']
    oldwaves={(r['race_id'],r['pollster'].casefold(),r.get('field_start'),r['field_date']) for r in before}
    assert all((r['race_id'],r['pollster'].casefold(),r['field_start'],r['field_date']) not in oldwaves for r in rows)
    write(BASE/'new-records.json',{'polls':rows});write(BASE/'new-review-decisions.json',{'decisions':decisions})
    return rows,decisions

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--append',action='store_true');args=p.parse_args()
    rows,decisions=prepare()
    if args.append:
        dest=ROOT/'research/poll_refresh_20261102'
        old=json.loads((BASE/'baseline/before-5-polls.json').read_text());config=json.loads((BASE/'baseline/before-6-review-decisions.json').read_text())
        # Base from archived raw records makes this append idempotent.
        assert len(old['polls'])==32 and not (set(config['decisions'])&set(decisions))
        old['polls'].extend(rows);config['decisions'].update(decisions)
        config['window']['start']='2026-10-31'
        config['scheduled_increment']={'checked_at':'2026-11-02T21:00:00-05:00','new_observations':13,'source':'research/poll_check_20261102_2100EST','window_note':'Start broadened only to accommodate honest October31–November2 first-publication bounds for newly available Iowa Rasmussen page with stale dateline. Original32 reviewed records unchanged.'}
        write(dest/'polls.json',old);write(dest/'review-decisions.json',config)
    print(json.dumps({'prepared':len(rows),'new_surveys':8,'new_races':sorted(set(r['race_id'] for r in rows)),'appended':args.append},indent=2))
