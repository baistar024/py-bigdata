# print("{:0>3} is".format(25))
#
# str = "{:0>5}".format(36)
# print(str)
import decimal
from datetime import datetime

for i in range (1000):
    str = "{:0>5}".format(i)
    print(str ,end = "\t")
    if i % 10 == 9:
        print()

print(('hello ')*5)

name = 'Zoy'

print("this is {name!r}")
print("this is {name!s}")
print("this is {name!a}")
print(f"this is {name!r}")
print(f"this is {name!s}")
print(f"this is {name!a}")

print(	'{0}, {1}, {2}'.format('a', 'b', 'c')	)
print(	'{}, {}, {}'.format('a', 'b', 'c'))
print(	'{2}, {1}, {0}'.format('a', 'b', 'c')	)
print(	'{2}, {1}, {0}'.format(*'abc'))
print(	'{0}{1}{0}'.format('abra', 'cad'))
#按名称访问
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
#按名称访问
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))