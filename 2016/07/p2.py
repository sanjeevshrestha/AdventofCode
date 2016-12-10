import sys,re
d=sys.stdin.readlines()
c=0
for l in d:
    if re.search(r"(.)([^\1])\1(\w*[[\]]\w*[[\]])*\w*[[\]]\w*\2\1\2",l.strip()):
        c+=1
print c