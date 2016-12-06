import sys
d=sys.stdin.readlines()
c=5
for e in d:
   e=e.strip()
   for x in e:
       j=0
       if x=='D' and c not in(7,8,9):
           j=3
       elif x=='U' and c not in(1,2,3):
           j=-3
       elif x=='L' and c not in(1,4,7):
           j=-1
       elif x=='R' and c not in(3,6,9):
           j=1
       c=c+j
   print c
