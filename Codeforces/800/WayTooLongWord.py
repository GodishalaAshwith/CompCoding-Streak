def WayTooLongWord(word):
  if len(word) > 10:
    return word[0] + str(len(word) - 2) + word[-1]

def main():
  word = input()
  result = WayTooLongWord(word)
  if result:
    print(result)
  else:
    print(word)

t = int(input())
while t > 0:
  main()
  t -= 1
