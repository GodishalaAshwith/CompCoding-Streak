a = sorted(list(map(int,input().split())))
print('Possible' if a[0]/a[2] == a[1]/a[3] else 'Impossible')