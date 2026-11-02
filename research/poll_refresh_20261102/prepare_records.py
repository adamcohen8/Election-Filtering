"""Prepare reviewed November 1–2 polling additions; never mutate live data."""
from pathlib import Path
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
from election_modeling.cycles import RACES_2026_BY_ID
from election_modeling.nominees import NOMINEES_2026_BY_RACE
from ingest_senate_research import digest
BASE=Path(__file__).resolve().parent
urls=json.loads((BASE/'extra-urls.json').read_text())
rows=[];reviews={}
def add(race,name,pollster,start,end,pub,vals,artifact,location,total,ns=None,method=None,note='',url=None,deff=2.,basis='party_id',proxy=False,bounds=None):
 spec=RACES_2026_BY_ID[race];nom=NOMINEES_2026_BY_RACE[race]
 r=dict(race_id=race,state=spec.state,office=spec.office,poll_id=name,sample_id=name,pollster=pollster,candidate_a=nom.republican.name,candidate_b=nom.candidate_b.name,candidate_a_party=nom.republican.party,candidate_b_party=nom.candidate_b.party,field_start=start,field_date=end,publication_date=pub,population='LV',reported_total_n=total,crosstab_basis=basis,subgroup_n_method=method or ('reported_n_weighting_unspecified' if ns else 'missing'),source_url=url or urls[artifact],source_location=location,evidence_excerpt='Conditional candidate A/B support within R,D,I respondent groups: '+str(vals),evidence_path=str((BASE/'sources'/artifact).relative_to(ROOT)),notes=note)
 assert (ROOT/r['evidence_path']).is_file()
 for p,pair,n in zip(['republican','democratic','independent'],vals,ns or [None]*3):r[p+'_a']=pair[0]/100;r[p+'_b']=pair[1]/100;r[p+'_n']=n
 review=dict(action='accept',reason='All six conditional support cells verified in the primary source. '+note)
 if ns:review['precision']=dict(method=r['subgroup_n_method'],design_effect=deff,evidence='Exact applicable table bases are reported; weighting classification retained. Provisional conservative design effect; no precision inferred from the headline N.')
 else:review['precision']=dict(method='assumed_covariance',cell_sd=.05,within_group_correlation=-.5,evidence='Exact applicable party subgroup bases are not published. Null Ns retained and the existing conservative 5pp cell SD covariance used.')
 if proxy:review['allow_proxy']=True
 if bounds:review['publication_date_bounds']=bounds
 rows.append(r);reviews[race+'/'+name]=review
# Select the all-likely-voter table, never the adjacent decided-only version.
for race,page,vals in [
 ('mi_gov',1,[(97,0),(9,89),(30,58)]),('mi_sen',1,[(89,7),(13,83),(45,47)]),
 ('mn_gov',2,[(85,9),(5,93),(34,50)]),('mn_sen',2,[(90,5),(3,91),(46,40)]),
 ('oh_gov',4,[(87,7),(0,95),(38,48)]),('oh_sen',4,[(87,7),(7,85),(40,46)]),
 ('pa_gov',5,[(81,16),(4,92),(23,66)]),('wi_gov',6,[(92,5),(0,99),(21,67)])]:
 add(race,'researchco-20261101','Research Co.','2026-10-30','2026-11-01','2026-11-01',vals,'researchco.pdf',f'PDF page{page}; first all450 likely-voter ballot for this office; POLITICAL ID Democrat/Republican/Independent columns',450,note='All450 LV, including undecided/other; adjacent decided-only ballot omitted. Political ID is source label; leaner handling unspecified. No subgroup Ns reported.')
for race,page,vals in [
 ('fl_gov',2,[(95,3),(2,91),(42,31)]),('fl_sen',2,[(93,5),(6,91),(30,53)]),
 ('ga_gov',3,[(87,3),(12,88),(39,40)]),('ga_sen',3,[(80,12),(8,92),(43,46)]),
 ('tx_gov',6,[(95,3),(3,91),(49,28)]),('tx_sen',6,[(87,12),(0,97),(47,41)])]:
 add(race,'researchco-20261102','Research Co.','2026-10-31','2026-11-02','2026-11-02',vals,'researchco-two.pdf',f'PDF page{page}; first all450 likely-voter ballot for this office; POLITICAL ID columns',450,note='All450 LV including undecided/other. Adjacent decided-only alternative omitted. Candidate source aliases (Angela Nixon, Keisha Bottoms) map to registered nominees. No subgroup Ns reported.')
add('us_house_generic','atlas-20261101','AtlasIntel','2026-10-28','2026-11-01','2026-11-01',[(88.5,9.5),(1.4,97.5),(32.4,61.4)],'atlas.pdf','PDF page16 generic ballot crosstabs, PARTISANSHIP D/R/I; page5 LV population',3566,note='Primary report identifies likely voters, despite aggregator labeling adults. Chart cells visually verified. Partisanship label, leaner treatment unspecified; no subgroup Ns. No valid-vote renormalization.')
for race,page,vals in [('tx_sen',16,[(90.9,6.6),(0,100),(28,64.5)]),('tx_gov',21,[(93.8,5.6),(0,96.3),(31.4,62.5)])]:
 add(race,'atlas-20261101','AtlasIntel','2026-10-28','2026-11-01','2026-11-01',vals,'atlas-tx.pdf',f'PDF page{page} raw vote crosstabs, PARTISANSHIP D/R/I; page5 LV population',1678,note='Raw published ballot, not adjacent valid-votes chart. Primary LV population overrides aggregator adult label. Chart visually inspected; subgroup Ns absent.')
add('nc_sen','ecu-20261029','East Carolina University','2026-10-26','2026-10-29',None,[(90,9),(2,97),(42,56)],'ecu.pdf','PDF page2 Senate vote choice by party identification, Q5r',1041,note='Already-voted and future-vote combined; Independent or something else. Release dateline November1 and machine timestamp November2 UTC; honest publication bounds. Weighted counts not printed; no invented bases.',bounds=['2026-11-01','2026-11-02'])
add('us_house_generic','yougov-national-20261030','YouGov','2026-10-27','2026-10-30','2026-11-02',[(92,5),(1,97),(32,62)],'yougov-national.pdf','PDF page7 (printed4), House Vote with Leaners, Party ID Dem/Ind/Rep and Unweighted N',3908,[1237,1454,1217],method='reported_unweighted',note='National Pre-election Study; YouGov official survey-results entry created November2. All3915 study LV; ballot item base3908. Use party ID columns, NOT 2026 House Vote columns, which are tautological. Baseline party-ID weighting and modeled LV disclosed; DEFF2 provisional.')
for race,vals,ns in [('ga_sen',[(94.1,5.8),(.8,98),(35.2,59)],[1100,1100,300]),('ga_gov',[(97.4,1.3),(1.6,97.4),(44.9,48.9)],[1100,1100,300])]:
 add(race,'insider-20261102','InsiderAdvantage','2026-10-31','2026-11-02','2026-11-02',vals,'insider-x-ga.webp','Published image: Party table for relevant office; X status2117369154638676386',2500,ns,note='Party label does not establish registration versus self-ID, so authorized unspecified-party proxy. Weighted age/race/gender/political affiliation, bases weighting unspecified. Governor article has49.03 while image49.3; use internally consistent explicit party table, flag source discrepancy.',basis='party_basis_unspecified',proxy=True,url='https://x.com/InsiderPolling/status/2117369154638676386')
add('ak_sen','insider-20261101','InsiderAdvantage','2026-10-31','2026-11-01','2026-11-02',[(81.6,16),(10.7,88.5),(41.5,51.2)],'insider-x-ak.webp','Published image first-round ballot Party table; X status2117293566951395511',1200,[456,336,408],note='First-round candidate support retained as published. Final RCV alternative in same image and duplicate repost are not separate observations. Dan S. Sullivan distinguished from Daniel J. Sullivan Jr. Party basis not explicit, authorized proxy.',basis='party_basis_unspecified',proxy=True,url='https://x.com/InsiderPolling/status/2117293566951395511')
add('mn_sen','insider-20261030','InsiderAdvantage','2026-10-29','2026-10-30','2026-11-01',[(97.1,2.6),(2.5,96.8),(48,39.1)],'insider-x-mn.webp','Published image Senate Party table; X status2117018158611812417',1200,[384,456,360],note='Party basis not explicit, authorized proxy. Original image and November2 repost are one survey, not two.',basis='party_basis_unspecified',proxy=True,url='https://x.com/InsiderPolling/status/2117018158611812417')
for race,vals in [('oh_sen',[(87.4,10.9),(1.3,97.3),(36.5,53.8)]),('oh_gov',[(82.5,14.9),(1.7,97.5),(40.2,50.3)])]:
 add(race,'insider-20261030','InsiderAdvantage','2026-10-29','2026-10-30','2026-11-01',vals,'insider-x-oh.jpg','Published image Party table for relevant office; X status2116992824411636158',1200,[480,336,384],note='Separately posted table recovered via signed-in X search, matched to primary release. Party basis unspecified, authorized proxy. Exact bases reported but weighting unspecified.',basis='party_basis_unspecified',proxy=True,url='https://x.com/InsiderPolling/status/2116992824411636158')
for race,artifact,page,total,vals,ns in [
 ('nh_sen','unh-nh.pdf',12,2035,[(89,5),(0,99),(35,54)],[841,926,252]),
 ('nh_gov','unh-nh.pdf',28,2026,[(94,4),(6,92),(52,37)],[834,926,251]),
 ('me_sen','unh-me.pdf',11,1633,[(98,2),(2,98),(45,53)],[642,780,201]),
 ('me_gov','unh-me.pdf',29,1648,[(91,2),(0,92),(31,53)],[654,783,201])]:
 add(race,'unh-20261031','University of New Hampshire Survey Center','2026-10-27','2026-10-31','2026-11-01',vals,artifact,f'PDF page{page}, With Leaners ballot, Party ID rows and N column',total,ns,deff=2.4 if race.startswith('nh') else 2.3,note='Prefer Party ID over registration rows. Source N weighting not explicit; preserve classification. Report writes design effect2.4% (NH)/2.3% (ME); provisionally use conservative dimensionless2.4/2.3, not0.024/0.023. Party leaner handling unspecified. Only one leaned ballot; third candidates remain outside modeled pair.')
add('ia_sen','grayhouse-20261031','GrayHouse','2026-10-28','2026-10-31','2026-11-02',[(94,3),(2,92),(36,58)],'grayhouse-ia.pdf','PDF page1 initial Senate ballot, REP/IND/DEM columns; primary article explicitly identifies these as self-reported party-ID shares',601,note='Party ID preferred to voter-file registration alternative. Other-party/unsure ID categories outside R/D/I. No exact party-ID subgroup bases printed; null Ns and conservative covariance. PDF retrieved from article download control.',url='https://www.grayhouse.com/post/grayhouse-poll-hinson-leads-in-iowa-by-2')
add('ne_sen','grayhouse-20261101','GrayHouse','2026-10-29','2026-11-01','2026-11-02',[(78,18),(6,92),(33,64)],'grayhouse-ne.pdf','PDF page2 Ballot Including Leaners, Republican/Democrat/Unaffiliated Other columns; page3 defines registration',534,basis='party_registration',note='Registration fallback. Osborn remains independent. One leaned full ballot; initial ballot omitted. PDF provides party composition but not applicable group Ns. Browser chart reports rounded weighted bases293/150/91; conservatively keep model Ns null and use existing explicit covariance rather than treat rounded weighted calibration as raw interviews.',url='https://www.grayhouse.com/post/grayhouse-poll-ricketts-leads-in-nebraska-by-4')
# Same Florida RedBox wave revised at its stable URL. Replace, never append a duplicate.
add('fl_gov','redbox-20261031','RedBox Research','2026-10-30','2026-10-31','2026-11-02',[(90,6),(2,95),(29,56)],'fl-redbox.pdf','PDF page18 Q6/Q7 Party ID columns; revised source downloaded November2',2898,[1137,906,855],method='reported_unweighted',deff=1.5,note='Same wave previously loaded. Current primary PDF changes independent Jolly support55 to56; other five model cells and subgroup Ns unchanged. Updated publication dateNovember2. Preserve archived previous source and row. Replacement adds zero observations.',url='https://afightworthhaving.com/polling/2026/florida/crosstabs.pdf')
rows[-1]['supersedes_poll_id']='fl_gov--redbox-20261031'
for r in rows:reviews[r['race_id']+'/'+r['poll_id']]['record_sha256']=digest(r)
(BASE/'polls.json').write_text(json.dumps({'polls':rows},indent=2)+'\n')
(BASE/'review-decisions.json').write_text(json.dumps({'window':{'start':'2026-11-01','end':'2026-11-02'},'reviewed_on':'2026-11-02','decisions':reviews},indent=2)+'\n')
print('Prepared',len(rows),'records, including one replacement')
