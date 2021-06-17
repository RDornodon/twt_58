#twt_58_1 - always go right
# turn map counter-clockwise n-times
turn=lambda A,n:([A:=[*map(list,zip(*A))][::-1]for _ in'*'*n]or[A])[-1]
p='rdlu'
for _ in[I:=input]*int(I()):
    a,b=I().split();Map=[[*I()]for y in'*'*int(a)];d=0
    for c in b:
        # turn the map to match the direction
        Map,N=turn(Map,(4-d+(d:=p.index(c)))%4),[]
        for l in Map:
            # find the map row with the user
            if'U'in l:
                s=e=i=0
                for c in l:
                    if'U'==c:s=i # find user position
                    if c in'# 'and s:e=i;break # find next non-box position
                    i+=1
                if' '==l[e]:v=l.pop(e);l.insert(s,v) # remove if its empty space and insert before the user
            N+=[l]
        Map=N
    # final turning to North and print
    Map=turn(Map,(4-d)%4)
    for l in Map:print(*l,sep='')