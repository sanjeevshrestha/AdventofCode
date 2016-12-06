import sys,itertools
i=sys.stdin.readlines()
s=0
for l in i:
    t=sorted(map(int,l.strip().split('x')))
    s+=(2*sum(t[0:2])+reduce(lambda x,y:x*y,t))
print s