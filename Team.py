n = int(input())
res = 0
while n>0:
  choices = input()
  c = list(map(int, choices.split()))
  if sum(c)>1:
      res+=1
  n-=1
  
print(res)