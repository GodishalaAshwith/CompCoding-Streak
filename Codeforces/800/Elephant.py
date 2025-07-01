x = int(input())
steps = 0
while x>=5:
  steps+=1
  x-=5
while x>=4:
  steps+=1
  x-=4
while x>=3:
  steps+=1
  x-=3
while x>=2:
  steps+=1
  x-=2
while x>=1:
  steps+=1
  x-=1

print(steps)