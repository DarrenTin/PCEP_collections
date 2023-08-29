bags = {
    'gucci' : 4000,
    'prada' : 2000,
    'LV' : 6500
}
print(bags)
bags['blueberry'] = 2300
bags.update({'versace' : 3000})
print(bags)
bags['prada'] = 2400

print('blueberry' in bags)
print('strawberry' in bags)

for bag in bags.keys():
    print(bag)

for bag in bags.values():
    print(bag)

for key, value in bags.items():
    print(key, value)

print(bags.popitem())
print(bags)
bags.clear()
print(bags)