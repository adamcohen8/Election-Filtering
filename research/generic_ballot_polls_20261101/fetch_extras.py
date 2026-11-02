from pathlib import Path
import urllib.request, concurrent.futures, re, json
BASE=Path(__file__).resolve().parent
urls={
'emerson-oct26.xlsx':'https://docs.google.com/spreadsheets/d/1LK-sn229somRxouNr_bA4DxoKdq85GAf/export?format=xlsx',
'focaldata-oct20.xlsx':'https://landing.focaldata.com/hubfs/Marketing%20content/Focaldata_US_Midterms_Poll_Oct2026_wave2_all.xlsx',
'focaldata-oct5.xlsx':'https://landing.focaldata.com/hubfs/Marketing%20content/Focaldata_US_Midterms_Poll_Oct2026_all.xlsx',
'clarity.html':'https://www.claritycampaigns.com/clarity-omnibus-2026-oct',
'prolific.html':'https://www.prolific.com/resources/poll-democrats-lead-by-11-points-here-s-how-we-reached-that-number',
'rainey.html':'https://www.raineycenter.org/polling/ai-data-centers-energy-and-kids-online',
'psu.html':'https://democracy.psu.edu/poll-report-archive/democrats-have-tiny-edge-in-congressional-generic-ballot/',
'morningconsult.html':'https://pro-assets.morningconsult.com/wp-uploads/2026/09/MCPI-Midterm-Ballot.html',
'activote30.html':'https://www.activote.net/polls/generic-ballot/2026-10-30/',
'yougov.html':'https://yougov.com/en-us/survey-results'}
def get(item):
 name,url=item; p=BASE/'sources'/name
 try:
  if not p.exists():
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r: p.write_bytes(r.read())
  print(name,p.stat().st_size)
  if name.endswith('html'):
   data=p.read_text(); links=re.findall(r'(?:href|src)=["\']([^"\']+)',data)
   print(name,[x for x in links if any(y in x.lower() for y in ['.pdf','.xlsx','iframe','topline','crosstab','embed','drive.google'])][:20])
 except Exception as e:print(name,str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(get,urls.items()))
(BASE/'extra-urls.json').write_text(json.dumps(urls,indent=2))
