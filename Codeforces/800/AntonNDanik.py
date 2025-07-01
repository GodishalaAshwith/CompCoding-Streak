from collections import Counter
n = int(input())
wins = list(input())
freq = Counter(wins)
if freq['A']>freq['D']:
  print("Anton")
elif freq['A']<freq['D']:
  print("Danik")
else:
  print("Friendship")