import base64
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
F='../tochal-hours-story/assets/fonts/'
s=open('studio.src.html',encoding='utf8').read()
s=s.replace('__PEYDA_400__',b(F+'peyda-regular.woff')).replace('__PEYDA_600__',b(F+'peyda-semibold.woff')).replace('__PEYDA_800__',b(F+'peyda-bold.woff'))
s=s.replace('__LOGO__','data:image/png;base64,'+b('logo-small.png'))
open('glassy-studio.html','w',encoding='utf8').write(s)
print(len(s))
