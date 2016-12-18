import sys,re
d=sys.stdin.readlines()

def is_slot_zero(time,pos,slots):
    return (time+pos)%slots==0

discs={}
for l in d:
    f=re.findall(r'Disc #(.).*?(\d+) positions; at time=0, it is at position (\d+).',l.strip())
    if f:
        xx=map(int,f[0])
        discs[xx[0]]=xx[1:]
t=0
while True:
    #Checking if all the discs are at slot zero, x is disc no and also acts as tiime delay
    if all(map(lambda x:is_slot_zero(t+x,discs[x][1],discs[x][0]),discs)):
        print "Part 1 :",t
        break
    t+=1

#Adding new disc at position 0 with 11 slots
discs[7]=[11,0]
t=0
while True:
    #Checking if all the discs are at slot zero, x is disc no and also acts as tiime delay
    if all(map(lambda x:is_slot_zero(t+x,discs[x][1],discs[x][0]),discs)):
        print "Part 2 :", t
        break
    t+=1
