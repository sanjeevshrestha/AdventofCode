import sys, numpy as np
d = sys.stdin.readlines()
c=g=0
x=np.ndarray((3,3))
for l in d:
    a=map(int,filter(lambda y:y!='',l.strip().split(" ")))
    x[g]=a
    g=(g+1)%3
    if g==0:
        y= x.transpose()
        for b in y:
            if sum(b)-max(b)>max(b):
                c=c+1
print c