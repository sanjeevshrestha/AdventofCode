import sys,re
d=sys.stdin.readlines()
c=0
for l in d:
    if re.search(r"(.)(?!\1)(.)\2\1",l) and not re.search(r"\[\w*(.)(?!\1)(.)\2\1\w*\]",l):
        c+=1
print c