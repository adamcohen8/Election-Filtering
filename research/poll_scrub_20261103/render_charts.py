from pathlib import Path
import json,subprocess
from PIL import Image,ImageDraw
B=Path(__file__).resolve().parent
items=[]
for r in json.loads((B/'chart-pages.json').read_text()):
 if 'state governor' in r['text'] and 'alaska' in r['file']:continue
 stem=r['file'].replace('.pdf','')+'-p'+str(r['page']);out=B/'rendered'/stem
 subprocess.run(['pdftoppm','-f',str(r['page']),'-l',str(r['page']),'-scale-to','2000','-png','-singlefile',str(B/'sources'/r['file']),str(out)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 im=Image.open(out.with_suffix('.png'));w,h=im.size
 # Primary party table is lower-left; retain source filename and page above each crop.
 crop=im.crop((0,int(h*.71),int(w*.34),int(h*.98)))
 canvas=Image.new('RGB',(800,360),'white');d=ImageDraw.Draw(canvas);d.text((8,8),stem,fill='black');crop.thumbnail((790,320));canvas.paste(crop,(0,30));items.append(canvas)
for start in range(0,len(items),5):
 canvas=Image.new('RGB',(800,360*len(items[start:start+5])),'white')
 for j,im in enumerate(items[start:start+5]):canvas.paste(im,(0,j*360))
 canvas.save(B/'rendered'/f'party-crops-{start//5+1}.png')
