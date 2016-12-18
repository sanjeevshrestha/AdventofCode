d=raw_input().strip()
limit1=int(raw_input().strip())
limit2=int(raw_input().strip())



def is_tile(cur_pos,row):
    l=row[cur_pos-1] if cur_pos>0 else '.'
    r=row[cur_pos+1] if cur_pos<(len(row)-1) else '.'
    c=row[cur_pos]
    t='.'
    if (l=='^' and c=='^' and r =='.') or (c=='^' and r=='^' and l=='.') or (l=='^' and r=='.' and c=='.') or (l=='.' and c=='.' and r=='^'):
        t='^'
    return t


def count_safe_tiles(limit):
    tiles = []
    tiles.append(d)
    for i in range(limit - 1):
        curr_row = tiles[i]
        next_row = []
        for ix in range(len(curr_row)):
            next_row.append(is_tile(ix, curr_row))
        tiles.append(next_row)
    return "\n".join("".join(x) for x in tiles).count('.')


print "Part 1 :", count_safe_tiles(limit1)
print "Part 2 :", count_safe_tiles(limit2)


