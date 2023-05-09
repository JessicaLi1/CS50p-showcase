name=input('File name:').lower().strip()
dic={'.gif':'image/gif',
'.jpg':'image/jpeg',
'.jpeg':'image/jpeg'
,'.png':'image/png'
,'.pdf':'application/pdf'
,'.txt':'text/plain'
,'.zip':'application/zip'}
x=0
for n in dic:
    if name.endswith(n) is True:
        x=dic[n]

    else:
        pass
if x==0:
    print('application/octet-stream')
else:
    print(x)