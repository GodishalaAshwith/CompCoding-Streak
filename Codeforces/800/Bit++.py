n = int(input())
x =0
while n>0:
  n-=1
  op = input()
  if op[0] =="+" or op[1] =="+":
    x+=1
  else:
    x-=1
print(x)