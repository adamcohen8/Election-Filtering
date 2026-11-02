from pathlib import Path
import json,urllib.request,hashlib,concurrent.futures,re
BASE=Path(__file__).resolve().parent
urls={
'callthemap.html':'https://www.callthemap.com/polls',
'atlas.html':'https://www.atlasintel.org/poll/usa-national-2026-11-01',
'oh-trafalgar.html':'https://www.thetrafalgargroup.org/news/oh-senate-gen-1102/',
'nh-npa.pdf':'https://backend.natpublicaffairs.com/media/NH_General_Election_Memo_103126.2.pdf',
'fl-redbox.pdf':'https://afightworthhaving.com/polling/2026/florida/crosstabs.pdf',
'yougov.html':'https://yougov.com/en-us/survey-results',
'quinnipiac.html':'https://poll.qu.edu/poll-results/'
}
if (BASE/'extra-urls.json').exists(): urls.update(json.loads((BASE/'extra-urls.json').read_text()))
def get(item):
 name,url=item;p=BASE/'sources'/name
 try:
  if not p.exists():
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:p.write_bytes(r.read())
  data=p.read_bytes();out={'name':name,'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'path':str(p)}
  print(name,len(data))
  if name.endswith('html'):
   links=re.findall(r'(?:href|src)=["\']([^"\']+)',data.decode(errors='replace'))
   print(name,[x for x in links if any(k in x.lower() for k in ['.pdf','.xlsx','drive.google','docs.google'])][:20])
  return out
 except Exception as e:print(name,str(e));return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:inventory=list(pool.map(get,urls.items()))
(BASE/'download-inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
