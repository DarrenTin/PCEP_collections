for x in range(1, 13):
    for y in range(1, 13):
        print(x, 'x', y, '=', x * y)
    print()

for i in range(1, 11):
    if i == 3 or i == 7:
        continue  # skip
    print(i)

for i in range(1, 100):
    pass