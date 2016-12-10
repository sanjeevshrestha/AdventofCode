import sys, re, collections
d=sys.stdin.readlines()
for l in d:
    n="".join(filter(lambda x:x!='',re.split("[^a-zA-Z[-]]*","".join(filter(lambda x: x!='',re.split("\[.*\]",l.strip()))))))
    t="".join(map(lambda u:u[0],sorted(collections.Counter(n.replace('-','')).most_common(10),key=lambda x:(-x[1],x[0]))))
    q=int(re.findall(r'\b\d+\b', l.strip())[0])
    if t[0:5]==re.findall("\[(.*)\]",l.strip())[0]:
        y="".join(map(lambda x:" " if x=='-' else chr((((ord(x)-97)+q)%26)+97),n[:-1]))
        if y=='northpole object storage':
            print q