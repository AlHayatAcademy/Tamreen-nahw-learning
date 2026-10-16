import colorsys,json
from pathlib import Path
root=Path(__file__).resolve().parent.parent
def rgb(h):return [int(h[i:i+2],16)/255 for i in (1,3,5)]
def lum(v):return sum(w*(x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for w,x in zip([.2126,.7152,.0722],v))
def ratio(a,b):
 lo,hi=sorted([lum(a),lum(b)]);return (hi+.05)/(lo+.05)
checks=[]
for mode,fgs,bgs in [('light',['#293348','#526078','#573075','#214f80','#145e4b','#07543f'],['#ffffff','#edf5f0','#edf2fa','#faf0f5']),('dark',['#f1edf8','#d2d9e7','#e4c7ff','#b9daff','#b1ecd6','#a6f1cf'],['#202d40','#293e43','#29374f','#423345'])]:
 for fg in fgs:
  for bg in bgs:
   r=ratio(rgb(fg),rgb(bg));assert r>=4.5,(mode,fg,bg,r);checks.append(r)
for fg,bg in [('#fff1d5','#174d58'),('#edf8f4','#174d58'),('#ffe5b6','#174d58'),('#533b12','#ffe5b6'),('#ffffff','#155e4b'),('#07543f','#edf7f1'),('#204d83','#edf2fc'),('#7c3158','#faf0f5'),('#b5f3d8','#293e43'),('#bfddff','#29374f'),('#ffd3e6','#423345'),('#124530','#d7f0e3'),('#71243c','#fbe2e9'),('#e1fff0','#294f3c'),('#ffe5ef','#532f41'),('#603f13','#fff1d7'),('#ffe5b7','#473a26')]:
 r=ratio(rgb(fg),rgb(bg));assert r>=4.5,(fg,bg,r);checks.append(r)
hues=[162,212,275,330,34,185,235,42,198];D=json.loads((root/'content.json').read_text());colors=[]
for l in D['lessons']:
 h=hues[l['stage']]+(l['number']-D['stages'][l['stage']]['from'])*2;s=(48+l['number']%7)/100;v=(26+l['number']%3)/100
 color=colorsys.hls_to_rgb(h/360,v,s);colors.append(color);r=ratio(color,rgb('#fffFFF'));assert r>=4.5,(l['id'],r);checks.append(r)
assert len(set(colors))==len(D['lessons'])
print(f'PASS: {len(checks)} light/dark/state/accent contrast pairs; minimum {min(checks):.2f}:1; 75 unique lesson accents. Browser rendering not tested.')
