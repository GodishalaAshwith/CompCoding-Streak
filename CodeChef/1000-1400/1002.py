# cook your dish here
t = int(input())
while t > 0:
    t-=1
    Dragon = list(map(int,input().split()))
    Sloth = list(map(int,input().split()))
    if Dragon == Sloth:
        print("TIE")
    
    elif sum(Dragon)>sum(Sloth):
        print("DRAGON")
    elif sum(Sloth)>sum(Dragon):
        print("SLOTH")
    
    elif Dragon[0]>Sloth[0]:
        print("DRAGON")
    elif Dragon[0]<Sloth[0]:
        print("SLOTH")
        
    elif Dragon[1]>Sloth[1]:
        print("DRAGON")
    elif Dragon[1]<Sloth[1]:
        print("SLOTH")
        
    elif Dragon[2]>Sloth[2]:
        print("DRAGON")
    else:
        print("SLOTH")