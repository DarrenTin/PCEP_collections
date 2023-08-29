# numbers = [i for i in range(1, 51) if i % 2 == 0]
# print(numbers)

# sample_text = 'Python is easy and powerful language'
# list_text = [x for x in sample_text]
# print(list_text)
# print(sample_text)

table = [[(i + (3 if j == 1 else 0)) for i in range(3)] for j in range(2)]
print(table)