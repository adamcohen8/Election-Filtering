from pathlib import Path
import json, urllib.request, concurrent.futures, hashlib
BASE=Path(__file__).resolve().parent
sources={
'economist-oct26':'https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_nJaupnc.pdf',
'economist-oct20':'https://d3nkl3psvxxpe9.cloudfront.net/documents/econTabReport_AjDiUmp.pdf',
'ipsos-oct26':'https://www.ipsos.com/sites/default/files/ct/news/documents/2026-10/Reuters%20Ipsos%20October%20Core%20Political%20Topline%2010.26%20release.pdf',
'marist-oct20':'https://maristpoll.marist.edu/wp-content/uploads/2026/10/NPR_PBS-News_Marist-Poll_USA-NOS-and-Tables_202610211808AS.pdf',
'cygnal-oct24':'https://www.cygn.al/wp-content/uploads/2026/10/Cygnal-National-Late-Oct26-NVT-Deck-Public.pdf',
'cbs-oct23':'https://assets1.cbsnewsstatic.com/hub/cms/prod_cms_alt/file/2026/10/25/8ad451c3-2d1f-4f7f-a3c8-97f923271e92/cbsnews_20261025_sun.pdf',
'fox-oct12':'https://static.foxnews.com/foxnews.com/content/uploads/2026/10/fox_october-9-12-2026_complete_national_cross-tabs_october-14-release.pdf',
'harvard-oct26':'https://harvardharrispoll.com/assets/uploads/2026/09/HHP_Oct2026_KeyResults.pdf',
'echelon-oct23':'https://netchoice.org/wp-content/uploads/2026/10/NetChoice-October-2026-Antitrust-Tech-Survey-Topline.pdf'}
if (BASE/'additional-urls.json').exists(): sources.update(json.loads((BASE/'additional-urls.json').read_text()))
def fetch(item):
 name,url=item; path=BASE/'sources'/f'{name}.pdf'
 try:
  if not path.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=40) as r: data=r.read()
   if not data.startswith(b'%PDF'): raise ValueError('not PDF')
   path.write_bytes(data)
  return {'name':name,'url':url,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size}
 except Exception as e: return {'name':name,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,sources.items()))
(BASE/'download-inventory.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results: print(r['name'],r.get('bytes',r.get('error')))
