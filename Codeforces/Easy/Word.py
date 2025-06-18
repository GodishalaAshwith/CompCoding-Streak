s = input()
upper_count = sum(1 for c in s if c.isupper())
lower_count = sum(1 for c in s if c.islower())
if lower_count>=upper_count:
  s = s.lower()
else:
  s = s.upper()
print(s)