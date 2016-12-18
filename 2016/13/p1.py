d= int(raw_input().strip())
s=tuple(map(int,raw_input().strip().split(",")))
e=tuple(map(int,raw_input().strip().split(",")))

def is_path(x,y):
    s = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + d
    c=bin(s)[2:].count('1')
    return (c%2)==0

visited=set()

def path(curr_path):
    return_path=[]
    for n in curr_path:
        x,y=(i for i in n)
        if x!=0 and (x-1,y) not in visited and is_path(x-1,y):
            visited.add(tuple([x-1,y]))
            return_path.append(tuple([x-1,y]))
        if y!=0 and (x,y-1) not in visited and is_path(x,y-1):
            visited.add(tuple([x,y-1]))
            return_path.append(tuple([x,y-1]))
        if (x+1, y) not in visited and is_path(x+1, y):
            visited.add(tuple([x+1, y]))
            return_path.append(tuple([x+1, y]))
        if (x, y + 1) not in visited and is_path(x, y + 1):
            visited.add(tuple([x, y + 1]))
            return_path.append(tuple([x, y + 1]))
    return return_path

steps=0
current_path=[s]

while e not in current_path:
    steps+=1
    current_path=path(current_path)

print steps
