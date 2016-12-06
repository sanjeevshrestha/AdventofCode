i=raw_input()
c=1
n=[]
for _ in range(50):
    n = []
    for x in range(1,len(i)):
        if i[x]==i[x-1]:
            c+=1
        else:
            n.append(str(c))
            n.append(str(i[x-1]))
            c=1
    n.append(str(c))
    n.append(str(i[x]))
    i= "".join(n)
print len(i)
print '---'
