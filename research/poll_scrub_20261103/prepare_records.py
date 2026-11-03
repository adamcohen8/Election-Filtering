"""Prepare November 3 source-reviewed additions; --append updates the owning acquisition."""
from pathlib import Path
import sys,json,hashlib,re,html,argparse
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
from election_modeling.cycles import RACES_2026_BY_ID
from election_modeling.nominees import NOMINEES_2026_BY_RACE
from ingest_senate_research import digest

def read(p):return json.loads(p.read_text())
def write(p,v):p.write_text(json.dumps(v,indent=2,allow_nan=False)+'\n')
def prepare():
    inventories=[read(B/n) for n in ['download-inventory.json','more-download-inventory.json','extra-download-inventory.json','last-download-inventory.json','final-download-inventory.json','recheck-download-inventory.json']]
    sources={r['name']:r for inv in inventories for r in inv if 'path' in r}
    for r in sources.values():assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
    rows=[];decisions={}
    def add(race_id,name,pollster,start,end,pub,n,vals,artifact,location,note,basis='party_id',extra_artifacts=()):
        race=RACES_2026_BY_ID[race_id];nom=NOMINEES_2026_BY_RACE[race_id]
        r=dict(race_id=race_id,state=race.state,office=race.office,poll_id=name,sample_id=name,pollster=pollster,sponsor='PollsterGraph' if pollster=='AtlasIntel' else None,candidate_a=nom.republican.name,candidate_b=nom.candidate_b.name,candidate_a_party=nom.republican.party,candidate_b_party=nom.candidate_b.party,field_start=start,field_date=end,publication_date=pub,population='LV',reported_total_n=n,crosstab_basis=basis,subgroup_n_method='missing',source_url=sources[artifact]['url'],source_location=location,evidence_excerpt='Published conditional candidate A/B percentages within R,D,I groups: '+str(vals),evidence_path=sources[artifact]['path'],notes=note,ballot_question_stage='Published full ballot; no analyst undecided/other redistribution',scrub_id=B.name)
        for p,pair in zip(['republican','democratic','independent'],vals):
            assert all(0<=x<=100 for x in pair) and sum(pair)<=100
            r[p+'_a'],r[p+'_b'],r[p+'_n']=pair[0]/100,pair[1]/100,None
        if extra_artifacts:r['additional_source_artifacts']=[{'path':sources[x]['path'],'sha256':sources[x]['sha256'],'url':sources[x]['url']} for x in extra_artifacts]
        rev=dict(action='accept',reason='All six full-ballot conditional party support cells verified against primary source. '+note,record_sha256=digest(r),precision=dict(method='assumed_covariance',cell_sd=.05,within_group_correlation=-.5,evidence='Applicable subgroup respondent counts not reported. Null Ns retained; established conservative 5pp support-cell SD with -0.5 within-group pair correlation, zero between-group correlation. No synthetic counts or precision inferred from headline N.'))
        if basis=='party_basis_unspecified':rev['allow_proxy']=True
        rows.append(r);decisions[race_id+'/'+name]=rev
    note='Atlas/PollsterGraph primary report, published November2 on the Atlas exclusive public-polls page. All-likely-voter raw ballot, not adjacent valid-vote charts. PARTISANSHIP Democrat/Republican/Independent columns; party-leaner classification unspecified. No subgroup Ns. Undecided/other/nonvoting shares retained outside the two candidates. Charts are embedded images and were visually checked in full-page renders; source figures copied without renormalization.'
    charts=[
      ('ak_sen','alaska',15,522,[(84.4,14.8),(1.2,98.5),(25.8,63.8)]),
      ('ia_sen','iowa',16,1219,[(93.9,3.2),(6.2,92.6),(28.5,66.3)]),
      ('ia_gov','iowa',21,1219,[(86.8,9.1),(6.1,93.9),(29.5,69.2)]),
      ('ks_sen','kansas',16,2038,[(85.7,12.2),(2.8,96.1),(24.0,70.0)]),
      ('ks_gov','kansas',21,2038,[(86.1,10.2),(1.8,96.0),(26.4,66.8)]),
      ('me_sen','maine',16,967,[(96.1,1.3),(2.0,97.4),(39.2,56.1)]),
      ('me_gov','maine',21,967,[(96.4,1.0),(1.8,87.6),(34.5,54.8)]),
      ('mi_sen','michigan',12,1316,[(99.5,.5),(.1,99.8),(43.9,55.9)]),
      ('mi_gov','michigan',17,1316,[(99.2,.4),(.1,99.4),(40.5,55.6)]),
      ('mn_sen','minnesota',16,2133,[(98.8,.5),(3.4,95.6),(46.4,39.0)]),
      ('nh_sen','new_hampshire',13,1057,[(92.0,6.5),(3.1,95.0),(37.8,56.6)]),
      ('nh_gov','new_hampshire',18,1057,[(90.0,6.5),(6.1,90.8),(49.3,40.6)]),
      ('nc_sen','north_carolina',16,1459,[(89.6,7.9),(.5,99.5),(30.4,66.2)]),
      ('oh_sen','ohio',16,1801,[(87.3,7.3),(0,99.1),(31.4,61.4)]),
      ('oh_gov','ohio',21,1801,[(88.3,8.6),(.6,97.3),(29.7,62.4)])]
    for race,state,page,n,vals in charts:
        specific=' Alaska uses the initial full multi-candidate ballot; incumbent Dan S. Sullivan is distinguished from Dan J. Sullivan and Gerald Heikes. Alaska governor remains excluded.' if state=='alaska' else ''
        add(race,'atlas-20261101','AtlasIntel','2026-10-28','2026-11-01','2026-11-02',n,vals,f'atlas-{state}.pdf',f'PDF page{page}, raw ballot crosstabs, PARTISANSHIP D/R/I columns; page5 target LV/sample',note+specific,extra_artifacts=('atlas-exclusive.html',))
    def table_rows(name):
        out=[]
        for tr in re.findall('<tr.*?</tr>',(ROOT/sources[name]['path']).read_text(),re.S):
            cells=[' '.join(html.unescape(re.sub('<[^>]+>',' ',c)).split()) for c in re.findall('<t[dh][^>]*>(.*?)</t[dh]>',tr,re.S)]
            out.append(cells)
        return out
    # Candidate rows have different rowspan offsets. Align from the first percentage,
    # and map party headers independently of the preceding question column.
    def extract(name,a_label,b_label,party_labels):
        ts=table_rows(name);headers=next(r for r in ts if all(x in r for x in party_labels) and "LV's" in r)
        vals={}
        for label in [a_label,b_label]:
            row=next(r for r in ts if label in r)
            start=next(i for i,x in enumerate(row) if re.fullmatch(r'\d+%',x))
            vals[label]=[int(row[start+headers.index(p)].strip('%')) for p in party_labels]
        return list(zip(vals[a_label],vals[b_label]))
    rass=[('me_sen','rasmussen-20261102','2026-10-27','2026-11-02','2026-11-02',896,'rasmussen-me-tabs.html','Susan Collins (R)','Troy Jackson (D)',['Republican','Democrat','Ind/Other'],[(87,8),(13,82),(40,55)],'sen-me-15.html'),('mi_gov','rasmussen-20261029','2026-10-28','2026-10-29','2026-10-30',745,'gov-mi-14.html','John James (R)','Jocelyn Benson (D)',['Republican','Democrat','Ind/Other'],[(82,9),(9,86),(28,56)],'rasmussen-mi-gov-release.html'),('oh_gov','rasmussen-20261031','2026-10-27','2026-10-31','2026-11-02',1119,'rasmussen-oh-gov-tabs.html','Vivek Ramaswamy (R)','Amy Acton (D)',['Republican','Democrat','Independent'],[(82,13),(13,82),(36,54)],'rasmussen-oh-gov.html')]
    for race,name,start,end,pub,n,artifact,a,b,groups,expected,release in rass:
        vals=extract(artifact,a,b,groups);assert vals==expected,(race,vals)
        note='Complete public demographic HTML table, with all six support cells. Party label does not establish self-ID versus registration, so use previously authorized unspecified-party proxy. No subgroup Ns; rounded party composition is not converted to interviews. Full ballot with residual other/undecided retained. Publication date verified in archived release HTML. Independent is separate from Another party in Ohio; published Ind/Other grouping retained for Maine/Michigan.'
        add(race,name,'Rasmussen Reports',start,end,pub,n,vals,artifact,'Public demographic table, first governor/Senate ballot, Party columns '+str(groups)+'; candidate row percentages aligned to LV total header',note,basis='party_basis_unspecified',extra_artifacts=(release,))
    return rows,decisions

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--append',action='store_true');args=p.parse_args()
    rows,decisions=prepare();write(B/'new-records.json',{'polls':rows});write(B/'new-review-decisions.json',{'decisions':decisions})
    if args.append:
        dest=ROOT/'research/poll_refresh_20261102';old=read(B/'baseline/raw-before.json');cfg=read(B/'baseline/reviews-before.json')
        # Refuse to overwrite any concurrent additions; allow exact idempotent replay.
        now=read(dest/'polls.json');reviews=read(dest/'review-decisions.json')
        expected=old['polls']+rows
        assert now['polls'] in [old['polls'],expected], 'Concurrent raw acquisition update; reconcile first'
        assert all(reviews['decisions'][k]==v for k,v in cfg['decisions'].items())
        assert not (set(cfg['decisions'])&set(decisions))
        old['polls']=expected;cfg['decisions'].update(decisions);cfg['window'].update(start='2026-10-30',end='2026-11-03')
        cfg['november3_increment']={'source':'research/poll_scrub_20261103','new_observations':len(rows),'window_note':'Start widened to October30 for the previously held Michigan Rasmussen governor release, whose full public table is now verified. Other new sources published November2. Existing records and decisions preserved exactly.'}
        write(dest/'polls.json',old);write(dest/'review-decisions.json',cfg)
    print(json.dumps({'new_observations':len(rows),'races':[r['race_id'] for r in rows],'appended':args.append},indent=2))
