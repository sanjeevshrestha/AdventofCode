import re
l=raw_input().strip()
c=0
while len(l)>0:
    f=re.findall(r'^\((\d+x\d+)\)',l)
    if f:
        m,n=map(int,f[0].split('x'))
        y=len(f[0])+2
        z=l[y:m+y]
        c+=(len(z)*n)
        l=l[m+y:]
    else:
        f=re.findall(r'^(\w+)',l)
        c+=len(f[0])
        l=l[len(f[0]):]
print c
