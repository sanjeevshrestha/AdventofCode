import sys, re, collections
d=sys.stdin.readlines()
s=0
for l in d:
    c="".join(sorted("".join(filter(lambda x: x!='',re.split("[^a-zA-Z]*","".join(filter(lambda x: x!='',re.split("\[.*\]",l.strip()))))))))
    t="".join(map(lambda u:u[0],sorted(collections.Counter(c).most_common(10),key=lambda x:(-x[1],x[0]))))
    q=int(re.findall(r'\b\d+\b', l.strip())[0])
    if t[0:5]==re.findall("\[(.*)\]",l.strip())[0]:
        s+=q
print s