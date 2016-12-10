import re
l=raw_input().strip()
def cd(l):
    c=0
    if len(l)<=0:
        return 0
    else:
        f = re.findall(r'^\((\d+x\d+)\)', l)
        if f:
            m, n = map(int, f[0].split('x'))
            y = len(f[0]) + 2
            z = l[y:m + y]
            w= cd(z)
            c += w* n
            l = l[m + y:]
        else:
            f = re.findall(r'^(\w+)', l)
            c += len(f[0])
            l = l[len(f[0]):]
    x=cd(l)
    return c+x
print cd(l)
