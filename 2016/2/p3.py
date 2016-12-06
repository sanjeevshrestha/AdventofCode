import sys
d=sys.stdin.readlines()
c=5
for e in d:
   for x in e:
       j=0
       j= 3 if x=='D' and c not in (7,8,9) else -3 if x=='U' and c not in (1,2,3) else -1 if x=='L' and c not in (1,4,7) else 1 if x=='R' and c not in (3,6,9) else 0
       c=c+j
   print c,