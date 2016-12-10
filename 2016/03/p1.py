import sys
d = sys.stdin.readlines()
c=0
for l in d:
    a=l.strip().replace("  "," ").split(" ")
    a=map(int,filter(lambda y:y!='',map(lambda x:x.strip(),l.strip().split(" "))))
    if sum(a)-max(a) > max(a):
        c=c+1
print c