# country_1 = "Malaysia"
# country_2 = "Singapore"
# country_3 = "Thailand"
# country_4 = "Indonesia"

# empty_list = []
# another_empty_list = list()
# southeast_asia = [country_1, country_2, country_3, country_4]
# print(southeast_asia)
# print(southeast_asia[0])
# # print(southeast_asia[5])
# print(southeast_asia[-1])
# print(southeast_asia[0:2])
# print(southeast_asia[::-1])
# print(southeast_asia[1:5:-1])

# string_list = list('Hello')
# print(string_list)

# print(southeast_asia)
# del southeast_asia[1]
# print(southeast_asia)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# numbers.remove(2)
# print(numbers)

# temp = numbers.pop()
# print(temp)

# southeast_asia.append('Vietnam')
# print(southeast_asia)
# southeast_asia.insert(1, 'Philippines')
# print(southeast_asia)

# missing_countries = ['Cambodia', 'Sample']
# southeast_asia.extend(missing_countries)
# print(southeast_asia)

# numbers_one = [1, 3, 5]
# numbers_two = [2, 4, 8]
# print(numbers_one + numbers_two)

# numbers = [4, 1, 3, 2, 5]
# numbers.sort()
# print(numbers)
# print(sorted(numbers, reverse=True))

# catalog = ['apples', 'oranges', 'bananas']
# print('apples' in catalog)

# grades = [10, 90, 90, 30, 50]
# print(grades.count(90))
# print(grades.index(90))

c = [1, 2, 3]
d = c
d = c[:] # not change accordingly
print(d)
c[0] = 10
print(c)
print(d)