# cook your dish here
n = int(input())
mn = n//3
reminder = 1 if n%3==1 or n%3==2 else n%3
mx = mn+reminder
print(mx-mn)