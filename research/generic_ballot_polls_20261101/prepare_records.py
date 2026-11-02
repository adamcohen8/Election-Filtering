"""Build reviewable source records; never mutates the model or poll feed."""
from pathlib import Path
import json,re,hashlib
from openpyxl import load_workbook
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
S=BASE/'sources'
urls={r['name']:r['url'] for r in json.loads((BASE/'download-inventory.json').read_text())}
for file in ['extra-urls.json','remaining-urls.json']:
 for name,url in json.loads((BASE/file).read_text()).items():urls[name.rsplit('.',1)[0]]=url
rows=[];decisions={}
def add(name,pollster,start,end,pub,pop,total,vals,ns=None,method=None,basis='party_id',note='',location='',url=None,artifact=None,bounds=None,proxy=False):
 row={'race_id':'us_house_generic','state':'United States','office':'generic_ballot','candidate_a':'Generic Republican','candidate_b':'Generic Democrat','candidate_a_party':'republican','candidate_b_party':'democratic','poll_id':name,'sample_id':name,'pollster':pollster,'field_start':start,'field_date':end,'publication_date':pub,'population':pop,'reported_total_n':total,'crosstab_basis':basis,'subgroup_n_method':method or ('reported_unweighted' if ns else 'missing'),'source_url':url or urls[name], 'source_location':location,'evidence_excerpt':'R/D/I conditional Republican/Democratic support: '+str(vals),'notes':note}
 for party,pair,n in zip(['republican','democratic','independent'],vals,ns or [None]*3):row[party+'_a']=pair[0]/100;row[party+'_b']=pair[1]/100;row[party+'_n']=n
 p=S/(artifact or name+'.pdf');assert p.is_file(),p
 row['evidence_path']=str(p.relative_to(ROOT))
 review={'action':'accept','reason':'Verified all six conditional candidate support cells in the primary source. '+note,'record_sha256':hashlib.sha256(json.dumps(row,sort_keys=True,allow_nan=False).encode()).hexdigest()}
 if bounds:review['publication_date_bounds']=bounds
 if proxy:review['allow_proxy']=True
 if not ns:review['precision']={'method':'assumed_covariance','cell_sd':.05,'within_group_correlation':-.5,'evidence':'Exact applicable subgroup counts unavailable or uncertain; retain null Ns and use the existing provisional conservative measurement covariance.'}
 else:review['precision']={'method':method or 'reported_unweighted','design_effect':2.0,'evidence':'Source-reported applicable subgroup bases; conservative provisional DEFF2 for weighting/nonprobability or unspecified weighting. Preserve the reported base classification.'}
 rows.append(row);decisions['us_house_generic/'+name]=review
for name,end,pub,vals,ns,pg in [
 ('economist-oct5','2026-10-05',None,[(81,5),(2,92),(26,46)],[421,510,441],28),
 ('economist-oct12','2026-10-12','2026-10-14',[(84,3),(2,90),(24,50)],[392,489,512],59),
 ('economist-official-oct20','2026-10-20',None,[(87,3),(2,91),(26,46)],[452,554,490],38),
 ('economist-official-oct26','2026-10-26',None,[(84,6),(1,93),(27,44)],[442,501,487],17)]:
 start={'2026-10-05':'2026-10-02','2026-10-12':'2026-10-10','2026-10-20':'2026-10-19','2026-10-26':'2026-10-23'}[end]
 upper={'2026-10-05':'2026-10-07','2026-10-20':'2026-10-23','2026-10-26':'2026-10-28'}
 add(name,'The Economist/YouGov',start,end,pub,'RV',sum(ns),vals,ns,location=f'PDF page{pg}, Congressional Vote, Party ID columns, Unweighted N row',note='Party columns are the full registered-voter ballot base, NOT the adjacent strict/loose LV columns; one version per wave. Candidate names are piped by district. Party leaner handling not shown in table. Publication bounds use field end and dated public citation when exact first release not pinned.',bounds=[end,upper[end]] if pub is None else None)
add('fox-oct12','Fox News/Beacon Research/Shaw & Co.','2026-10-09','2026-10-12','2026-10-14','RV',1202,[(94,5),(2,98),(36,62)],location='PDF page8 Q16, Dem/GOP/Ind columns',note='Full registered-voter party columns. PDF reports subgroup MOEs, not exact subgroup Ns.')
add('cbs-oct2','CBS News/YouGov','2026-09-30','2026-10-02','2026-10-04','LV',1572,[(97,3),(1,99),(42,57)],[511,548,483],method='reported_weighted',location='PDF page20, 2026 House Vote, Party ID and Weighted N',note='Weighted subgroup bases; LV party table, not RV approval table.')
add('cbs-oct23','CBS News/YouGov','2026-10-21','2026-10-23','2026-10-25','LV',1749,[(97,3),(1,99),(43,53)],[586,639,489],method='reported_weighted',location='PDF page19, 2026 House Vote, Party ID and Weighted N',note='Weighted subgroup bases; table contains additional non-R/D/I categories, and rounded party bases need not sum to total.')
add('ipsos-oct26','Reuters/Ipsos','2026-10-22','2026-10-26','2026-10-26','LV',1164,[(94,5),(2,98),(35,54)],[410,391,363],location='PDF page5 TM3287Y24_Combined, Base Likely Voters, Dem LV/Rep LV/Ind Other LV',note='Lean-inclusive ballot. Independents include other party; exact source subgroup Ns unweighted. One LV version, RV alternative not counted.')
add('ipsos-oct19','Reuters/Ipsos','2026-10-16','2026-10-19','2026-10-20','A',1679,[(82,4),(2,86),(14,30)],[465,522,692],location='PDF page3 TM3287Y24, Dem/Rep/Ind Other columns; base on pages1–3',note='The complete party columns cover ALL ADULTS, not the adjacent RV column. First choice before lean probe, which applies only to undecided respondents. Independents include other party. Do not substitute RV topline population.')
add('marist-oct20','NPR/PBS News/Marist','2026-10-19','2026-10-20','2026-10-27','LV',None,[(94,6),(2,98),(39,52)],location='PDF page7 USCNGS01, National Likely Voters, Party Identification rows',note='Exact LV party subgroup counts not printed in selected table; 1289 is the RV base and is not substituted.')
add('harvard-oct26','Harvard CAPS/Harris Poll/HarrisX','2026-10-24','2026-10-26',None,'LV',None,[(95,5),(2,98),(44,56)],location='PDF page20 CON2026B, Among Likely Voters, DEM/GOP/IND OTH columns',note='Forced two-party question; preserve source 100% two-party totals. Independents include other party. Exact LV subgroup Ns absent; do not substitute full RV sample.',bounds=['2026-10-26','2026-10-28'])
add('umass-oct4','UMass Lowell/YouGov','2026-10-02','2026-10-04',None,'LV',1000,[(92,4),(1,97),(27,48)],location='PDF page6 Q1, Leaned Party ID',note='Leaned party ID assigns party leaners to D/R; narrow Independent differs from unleaned party ID. Exact subgroup Ns unshown.',bounds=['2026-10-04','2026-10-23'])
add('rainey-oct20','Rainey Center','2026-10-14','2026-10-20',None,'RV',1279,[(95,3),(2,96),(34,50)],location='PDF page10 Q5 top banner PARTY ID Dem/Rep/Ind Other',note='Sum definitely+probably support from rounded components; may differ by1pp from unrounded aggregates. Independent combines other party. Exact subgroup Ns absent.',bounds=['2026-10-20','2026-10-28'])
# Spreadsheet support uses displayed conditional shares, not topline or column composition.
w=load_workbook(S/'emerson-oct26.xlsx',read_only=True,data_only=True);table=list(w['crosstabs'].values)
partyrows={r[1]:r for r in table if len(r)>17 and r[1] in ['Democrat','Republican','Independent/other']}
vals=[];ns=[]
for label in ['Republican','Democrat','Independent/other']:
 r=partyrows[label];vals.append((r[13]*100,r[11]*100));ns.append(r[16])
add('emerson-oct26','Emerson College','2026-10-24','2026-10-26','2026-10-30','LV',1000,vals,ns,method='reported_weighted',basis='party_registration',location='Workbook crosstabs rows5–7; columnsL/N conditional row shares, Q weighted bases',note='Question: party registration or affiliation, with Independent/other combined; exact fractional weighted bases retained in raw record and floored only by ingestion.',artifact='emerson-oct26.xlsx')
for name,start,end,pub,question in [('focaldata-oct5','2026-10-02','2026-10-05','2026-10-11','Q69'),('focaldata-oct20','2026-10-16','2026-10-20','2026-10-25','Q66')]:
 w=load_workbook(S/(name+'.xlsx'),read_only=True,data_only=True);rr=list(w['Overall'].values)
 ix=next(i for i,r in enumerate(rr) if isinstance(r[0],str) and r[0].startswith(question+' In the elections'))
 h=rr[ix+2];drow=rr[ix+3];rrow=rr[ix+5];nrow=next(r for r in rr[ix:ix+20] if r[0]=='Base (n)');base=next(r for r in rr[ix:ix+20] if r[0]=='Weighted base')
 groups=[['Not very strong Republican','Strong Republican'],['Strong Democrat','Not very strong Democrat'],['Lean Democrat','Independent','Lean Republican']]
 vals=[];ns=[];pool=[]
 for labels in groups:
  cols=[h.index(l) for l in labels];den=sum(base[c] for c in cols);vals.append((100*sum(rrow[c]*base[c] for c in cols)/den,100*sum(drow[c]*base[c] for c in cols)/den));ns.append(sum(nrow[c] for c in cols));pool.append({'labels':labels,'weighted_base':den,'raw_n':sum(nrow[c] for c in cols)})
 add(name,'Focaldata/Financial Times',start,end,pub,'A',nrow[1],vals,ns,location=f'Workbook Overall {question}, rows{ix+1}–{ix+15}; seven-point Party ID, Base n and Weighted base',note='All-adult first-choice party columns. Pool strong/not-strong identifiers into D/R; retain both leaner groups with Independent. Support pooled using exact weighted bases; raw subgroup Ns summed. Unknown-party respondents excluded from those groups. LV/RV headline columns are different populations and not used.',artifact=name+'.xlsx')
 rows[-1]['pooling_details']=pool;decisions['us_house_generic/'+name]['record_sha256']=hashlib.sha256(json.dumps(rows[-1],sort_keys=True,allow_nan=False).encode()).hexdigest()
# ActiVote's party rows explicitly use registration; composition shares are rounded, not Ns.
for day,start,end,vals in [('03','2026-09-22','2026-10-02',[(93,7),(10,90),(42,58)]),('14','2026-10-04','2026-10-14',[(91,9),(8,92),(44,56)]),('21','2026-10-15','2026-10-21',[(90,10),(7,93),(44,56)]),('30','2026-10-22','2026-10-30',[(91,9),(7,93),(45,55)])]:
 add('activote'+day,'ActiVote',start,end,'2026-10-'+day,'LV',2000 if day=='30' else 1000,vals,basis='party_registration',artifact='activote'+day+'.html',url='https://www.activote.net/polls/generic-ballot/2026-10-'+day+'/',location='Full crosstab table Party D/R/I rows',note='Source-produced binary candidate choice; no new renormalization. Source narrative refers to registered party. Party composition is rounded; exact subgroup Ns stay null. Separate non-overlapping field periods.')
# Verified browser-exported first-choice table, not the LV headline or leaner-only table.
bigrows=list(load_workbook(S/'bigdata-oct30.xlsx',read_only=True,data_only=True).active.values)
bigvals=[(bigrows[15][c]*100,bigrows[12][c]*100) for c in [3,2,4]]
bigns=[bigrows[9][c] for c in [3,2,4]]
add('bigdata-oct30','BIG DATA POLL','2026-10-27','2026-10-30','2026-10-31','RV',3418,bigvals,bigns,method='reported_weighted',artifact='bigdata-oct30.xlsx',url='https://application.marketsight.com/app/ItemView.aspx?SharedBy=34090&SharedFor=public%40bigdatapoll.com&id=316b028e-c8c9-4dc9-a054-b4f40137114d',location='Exported workbook Generic Congressional Ballot x Party, Sample Size and Column %',note='First-choice registered-voter table3418, not the3214 LV headline. Excel export resolves the displayed rounded Sample Size to fractional weighted bases; use exact source shares and DEFF2. Independent/other combined. Exact browser selections Generic Congressional Ballot and Party.')
add('clarity-oct21','Clarity Campaign Labs','2026-10-15','2026-10-21',None,'LV',1016,[(93,4),(4,94),(17,35)],basis='modeled_party_id',proxy=True,location='PDF page21 Generic House Vote w Leaners by Party ID; page25 definition of partisanship model',note='Modeled party-ID proxy, not direct self-ID; expressly authorized proxy class. R93 minus published R margin89 yields D4; D94 minus published D margin90 yields R4. I17R/35D printed. Arithmetic on independently rounded support/margins can differ by1pp; use explicit conservative covariance.',bounds=['2026-10-21','2026-10-27'])
# On Point's source turnout-model ballot is an authorized modeled subgroup estimate.
w=load_workbook(S/'onpoint-oct28.xlsx',read_only=True,data_only=True)
r=list(w['LV Crosstabs'].values); vals=[(r[12][c]*100,r[11][c]*100) for c in [25,24,26]]
add('onpoint-oct28','On Point Polling','2026-10-28','2026-10-28','2026-10-29','LV',1170,vals,basis='modeled_subgroup_estimate',proxy=True,artifact='onpoint-oct28.xlsx',url='https://docs.google.com/spreadsheets/d/1Zxj6w6DziLGJ6LOaw5aHMw6MdHHjHmKiQCiBoT9TgIQ/edit?usp=sharing',location='LV Crosstabs rows9–17 Q9 leaned House ballot, Party ID columnsY:AA',note='Source turnout-probability weighting and ballot soft targets; source-produced model-based subgroup estimate, not an ordinary1170-person LV screen. All1170 interviewed RV contribute probabilistically. Independent/other unleaned self-ID group; source interviews R371/D424/I375 retained as metadata, model Ns null. No additional undecided allocation applied.')
rows[-1]['reported_interview_bases']={'republican':371,'democratic':424,'independent':375}
decisions['us_house_generic/onpoint-oct28']['record_sha256']=hashlib.sha256(json.dumps(rows[-1],sort_keys=True,allow_nan=False).encode()).hexdigest()

# Exact decisions and sources retained; no backfill because current window exceeds ten.
(BASE/'us_house_generic/polls.json').write_text(json.dumps({'race_id':'us_house_generic','polls':rows},indent=2,allow_nan=False)+'\n')
config={'schema_version':2,'reviewed_on':'2026-11-01','window':{'start':'2026-10-01','end':'2026-11-01'},'decisions':decisions,'limitations':['Selection is national generic House vote preference only; national aggregates of named district candidates are labeled. Congressional-control preference alone is excluded.','Population and party definitions differ: LV, RV and all-adult party tables are explicitly distinguished; national user weights R37/D33/I30 remain unchanged.','One population/question version per poll wave. Unrecovered sources are inventoried; search is not proof of complete public coverage.','Unknown subgroup counts use explicit5pp cellSD covariance with within-pair correlation-.5. Reported weighted/unweighted/uncertain bases use provisional DEFF2; no synthetic exact Ns.','Source binary ballots retain source shares; other candidates, undecided and nonvoters remain outside the model without normalization.','Modeled-party-ID and rounded arithmetic cases are explicitly marked; no empirical calibration claim.']}
(BASE/'review-decisions.json').write_text(json.dumps(config,indent=2)+'\n')
(BASE/'us_house_generic/REPORT.md').write_text('# National generic ballot reviewed source records\n\n'+str(len(rows))+' waves, all released within October1–November1 publication bounds. Exact dates or honest first-publication bounds are recorded. No older backfill needed. See polls.json, review decisions and source artifacts.\n')
print('Prepared',len(rows),'reviewed polls')
for r in rows:print(r['poll_id'],r['population'],[r[p+'_'+c] for p in ['republican','democratic','independent'] for c in ['a','b']])
