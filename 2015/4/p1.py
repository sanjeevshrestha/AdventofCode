import hashlib
k='bgvyzdsv'
f=False
i=0
while not f:
    i+=1
    k1=k+str(i)
    m = hashlib.md5()
    m.update(k1)
    d=m.hexdigest()
    if d[0:6]=='000000':
        f=True
print i, k1, d, d[0:5]

