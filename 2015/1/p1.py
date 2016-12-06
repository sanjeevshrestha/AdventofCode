i=raw_input()
y=0
for x in i:
    y+=1 if x=='(' else -1 if x==')' else 0
print y