def Elected(voting):
    for party, votes in voting.items():
        if votes>50:
            return party
        else:
            continue
    return "NOTA"
    
# cook your dish here
for _ in range(int(input())):
    a , b , c = list(map(int,input().split()))
    voting = {'A':a,'B':b,'C':c}
    print(Elected(voting))
