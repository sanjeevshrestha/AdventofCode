import hashlib
k=raw_input()
p=[]
i=0
while len(p)<8:
    i+=1
    d=hashlib.md5(k+str(i)).hexdigest()
    if d[0:5]=='00000':
        p.append(d[5:6])
print "".join(p)