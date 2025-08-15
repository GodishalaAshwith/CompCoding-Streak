# cook your dish here
def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number <= 1 or number%2 == 0 or number%3 == 0:
        return False

    for x in range(5, int(number**.5)+1,2):
        if not number % x:
            return False
    return True

        
for _ in range(int(input())):
    x, y = map(int,input().split())
    #for x in range(1,m):
    #    for y in range(1,n):
    for i in range(1,100):
        if is_prime(x+y+i):
            print(i)
            break
    else:
        print(1)
        
    