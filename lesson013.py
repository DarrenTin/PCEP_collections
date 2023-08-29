# & | ~ ^ << >>
first_binary = 0b1011
second_binary = 0b0111
result = first_binary & second_binary
print(result)
print(bin(result))

# same as above
first_binary = 11
second_binary = 7
result = first_binary & second_binary
print(result)
print(bin(result))

# ~ -(n + 1)
a = 2
print(~a)

b = 0b0101 << 1
print(bin(b))

c = 20 >> 2
print(c)

# geeksforgeeks python bitwise operators