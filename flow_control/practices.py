
"""s = "swapnil bhagwat iwarkar"
print(s.replace('swap', 'prem'))
print(s.casefold())
#s = "      SWAPNIL BHAGWAT IWARKAR     "
print(s.casefold())
print(s.lower())
print(s.title())
print(s.join(s[0:3]))
print(s.swapcase())
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdigit())
print(s.islower())
print(s.isdecimal())
print(s.isidentifier())
print(s.isnumeric())
print(s.isprintable())
print(s.isspace())
print(len(s))
print(s.center(28,'a'))
print(s.endswith('kar'))
print([10])
print(type([10]))
print(list())
print(type(list()))
s = "swapnil"
print(type(s))
s=["swapnil", 10, 12.5]
p=s.copy()
print("it is orignal list element in s",s)
print("it is copy list element in p :",p)
print(id(s))
print(id(p))
s[0] = "shree"
print(s)
k = [10,20,30,40,50]
print(k)
print(id(k))
k[0] = 100
print(k)
print(id(k))
print(k)
#print(k.clear())
k = k.copy()
print(k)
t = k
print(t)
print(id(k))
print(id(t))

s1 = [10,20,30,40,50]
s2=s1.copy()
s3 = s1
print("value of s1 =", s1)
print("value of s2 =", s2)
print("value of s3 =", s3)
print(id(s1))   # it is original copy
print(id(s2))   # it is shallow copy
print(id(s3))   # it is deep copy
s = [10,20,30,40,50,60,10,20,20,30]
print(s.count(10))
print(s.count(20))
# extend function
s.extend('swapnil')
s.extend(102.3)
print(s)
s.clear()
print(s)
day 1;
"""
print('hello')
print("hello")
print('"hello"')
print(23 * 9)
100
print(id(100))
