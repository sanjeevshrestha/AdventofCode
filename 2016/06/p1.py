import sys,collections
d=sys.stdin.readlines()
a=[[] for x in range(8)]
for l in d:
    e=0
    for c in l.strip():
        a[e].append(c)
        e=(e+1)%8
y=map(lambda x: collections.Counter("".join(x)).most_common(1)[0][0][0],a)
print "".join(y)