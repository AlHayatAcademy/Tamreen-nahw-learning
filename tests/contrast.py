import colorsys,json,re
from pathlib import Path
root=Path(__file__).resolve().parent.parent
def rgb(h):return [int(h[i:i+2],16)/255 for i in (1,3,5)]
def luminance(v):return sum(w*(x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4) for w,x in zip([.2126,.7152,.0722],v))
def ratio(a,b):
 lo,hi=sorted([luminance(a),luminance(b)]);return (hi+.05)/(lo+.05)
pairs=[('#29334d','#ffffff'),('#526077','#ffffff'),('#07553e','#edf7f1'),('#493260','#edf7f1'),('#493260','#eff4fd'),('#493260','#fbf0f6'),('#f0eaf8','#202c3e'),('#a1f0ce','#273d43'),('#b6d9ff','#253246')]
ratios=[]
for a,b in pairs:
 r=ratio(rgb(a),rgb(b));assert r>=4.5,(a,b,r);ratios.append(r)
hues=[162,212,275,330,34,185,235,42]
D=json.loads((root/'content.json').read_text())
for l in D['lessons']:
 h=hues[l['stage']]+(l['number']-D['stages'][l['stage']]['from'])*2
 r=ratio(colorsys.hls_to_rgb(h/360,.28,.52),rgb('#ffffff'));assert r>=4.5,(l['id'],r);ratios.append(r)
print(f'PASS: {len(ratios)} selected light/dark/accent contrast pairs; minimum {min(ratios):.2f}:1. Static color checks, not browser screenshots.')
