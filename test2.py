'''
# import function
import test
x = test.add(2, 1)
print(x)
print("=" * 50)
'''

from test import add
x = add(2, 1)
print("-" * 50)
print(x)
print("=" * 50)
# 以上兩個結果一樣


from test import practice1
y = practice1(6, 2)
print(y)
print("=" * 50)

from test import hr_to_mins
z = hr_to_mins(2.5)
print(z)