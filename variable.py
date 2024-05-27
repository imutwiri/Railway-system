x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
print(type(x))

i=1
m=2.8
k=1j

a=float(i)
b=int(m)
c=complex(i)

print(a)
print(b)
print(c)

import random
print(random.randrange(1, 10))

a="Hello World"
print(a.upper())

txt ="My name is Ian Mutwiri"
print("Kinoti" in txt)