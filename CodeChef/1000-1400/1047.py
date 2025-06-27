# cook your dish here
for _ in range(int(input())):
    s = input()
    s = s.replace('<','temp')
    s = s.replace('>','<')
    s = s.replace('temp','>')
    c = s.count('><')
    print(c)