import hashlib
k=raw_input()
p=[None]*8
i=c=0
while c<8:
    i+=1
    d=hashlib.md5(k+str(i)).hexdigest()
    n=int(d[5:6],16)
    if n<8 and d[0:5]=='00000' and p[n]==None:
        p[n]=d[6:7]
        c+=1
print "".join(p)