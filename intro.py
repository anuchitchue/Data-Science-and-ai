price = 90
if price >= 100:
    price('Discpunt 5%')
else:
    print('Discount 2%')
print('Bye')

temp = 32
if temp < 30:
    print('Fan off')
elif temp >= 30 and temp < 40:
    print('Small Fan')
else:
    print('Turn on a Big Fan')
    
    
for count in range(4):
    print("test for")
    print(count)
print("done")


name = "kobkiat"
print("Hi, %s" %name)
a = 2
print("Hi, %s a = %d" %(name, a))

import math
print("%.19f" %math.pi)

def area(length):
    area = length * length
    return area
area(4)

cal = lambda x: x * 2
cal(2)


data = [1, 2, 3]
type(data)
data.append(33)

print("test")