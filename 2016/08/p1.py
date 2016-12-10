import sys,re,numpy as np
d=sys.stdin.readlines()
w,h=50,6
s=np.zeros((h,w),dtype=str)
s[:h,:w]=' '
for l in d:
    q=re.split(r'[\s=]',l)
    if q[0]=='rect':
        a,b=map(int, q[1].split('x'))
        s[:b,:a]='#'
    elif q[0]=='rotate':
        if q[1]=='row':
            y,n=int(q[3]),int(q[5])
            s[y]=np.roll(s[y],n)
        else:
            x,n=int(q[3]),int(q[5])
            s[:,x]=np.roll(s[:,x],n)

print 'Total On -',np.sum(map(lambda x:x=='#',s))
print '\n'.join(''.join(r) for r in s)