p = list(input())
def dangerous(p):
    counts = []
    zCount = 0
    oCount = 0
    for i in p:
        if i == '0':
            zCount+=1
            counts.append(int(zCount))
            oCount=0
        elif i == '1':
            oCount+=1
            counts.append(int(oCount))
            zCount=0
    if max(counts)>6:
        return "YES"
    else:
        return "NO"
        
print(dangerous(p))