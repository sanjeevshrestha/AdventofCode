import sys,re
d=sys.stdin.readlines()
b={}
o={}
c=(61,17)
for l in d:
    r=re.findall(r'value\s(\d+)\sgoes\sto\sbot\s(\d+)',l.strip())
    if r:
        if not r[0][1] in b.keys():
            b[r[0][1]]=[]
        b[r[0][1]].append(int(r[0][0]))

def g(i,n,v):
    if not n in b.keys():
        b[n] = []
    b[n].append(v)
    b[i].remove(v)

def h(i,n,v):
    if not n in o.keys():
        o[n] = []
    o[n].append(v)
    b[i].remove(v)

while any(map(lambda x:len(b[x])>1,b)):
    for l in d:
        r=re.findall(r'bot\s(\d+)\sgives\slow\sto\s(\w+)\s(\d+)\sand\shigh\sto\s(\w+)\s(\d+)',l.strip())
        if r:
            k=r[0]
            if k[0] in b.keys() and len(b[k[0]])>1 :
                m,n=min(b[k[0]]),max(b[k[0]])
                if k[1]=='bot':
                    g(k[0],k[2],m)
                if k[3]=='bot':
                    g(k[0],k[4],n)
                if k[1]=='output':
                    h(k[0],k[2],m)
                if k[3]=='output':
                    h(k[0],k[4],n)
print o['0'][0]*o['1'][0]*o['2'][0]