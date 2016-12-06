import sys,itertools
i=sys.stdin.readlines()
s=0
for l in i:
    t=[int(x)*int(y) for x,y in itertools.combinations(l.strip().split('x'),2)]
    m=min(t)
    s+=(2*sum(t)+m)
print s