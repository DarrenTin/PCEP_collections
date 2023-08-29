empty_tuple = ()
a = 'dog', 
a = ('dog', ) # must put ','
b = ('dog', 'cat', )
d = 1, 2, 3, 4, 

e = ('lee ah beng', '888888-88-8888', '30000', '56, jalan 8, bandar baru kajang')
# print(e)
x, y, z, f = e
print(x)
print(y)
print(z)
print(f)

# e.append('2020')  # cannot because immutable
print(len(e))

s = 'khonglijiun'
t = tuple(s)
print(t)

lst = [1, 2, 3]
t = tuple(lst)
print(t)

d = {'a':1, 'b':2, 'c':3}
t = tuple(d)
print(t)
t = tuple(d.items())
print(t)