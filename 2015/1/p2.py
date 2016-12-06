i=raw_input()
y=c=0
for x in i:
    c+=1
    y+=1 if x=='(' else -1 if x==')' else 0
    if y==-1:
        break
print c
