from pathlib import Path
import json,urllib.request,hashlib,concurrent.futures,re
B=Path(__file__).resolve().parent
urls=json.loads((B/'recheck-urls.json').read_text())
def get(item):
 name,url=item;p=B/'sources'/name
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35) as r:data=r.read();final=r.url
  p.write_bytes(data)
  if name.endswith('.html'):
   links=re.findall(r'(?:href|src)=["\']([^"\']+)',data.decode(errors='replace'))
   special=[x for x in links if any(k in x.lower() for k in ['.pdf','.xlsx','drive.google','docs.google','pollvault','atlasintel','crosstab'])]
  else:special=[]
  return dict(name=name,url=url,final_url=final,path=str(p.relative_to(B.parents[1])),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),links=special)
 except Exception as e:return dict(name=name,url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:out=list(pool.map(get,urls.items()))
(B/'recheck-download-inventory.json').write_text(json.dumps(out,indent=2)+'\n')
for r in out:print(r)
