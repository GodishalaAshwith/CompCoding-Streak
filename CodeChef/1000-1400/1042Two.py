# cook your dish here
for _ in range(int(input())):
    a,b,c,d,e = list(map(int,input().split()))
    luggage = [a,b,c]
    for i in range(len(luggage)):
        if luggage[i-1] + luggage[i]<d:
            luggage.remove(luggage[i-1])
            luggage.remove(luggage[i])
            if len(luggage)>0 and luggage[0]<e:
                print("YES")
    print("NO")