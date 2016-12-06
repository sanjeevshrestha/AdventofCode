import sys
d=sys.stdin.readlines()
c=5
for e in d:
   for x in e:
       j=0
       if x=='D' and c not in(5,10,12,13,9):
           j=2 if c==1 or c==11 else 4
       elif x=='U' and c not in(5,2,1,4,9):
           j= -2 if c == 13 or c==3 else -4
       elif x=='L' and c not in(1,2,5,10,13):
           j=-1
       elif x=='R' and c not in(1,4,9,12,13):
           j=1
       c=c+j
   print c,