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

## LIST

data = [2, 1, 3, 4, 5, 6, 3]
type(data)
data.append(33)

lst = ['kobkiat', 2, 5, 8.5]
lst
type(lst)

avg = sum(data) / len(data)
print('Average (mean) = ', avg)

x = [[6, 7, 4], [2, 8, 3]]
x[0][0]
x[0][1]
x[1][2]

## TUPLE

tp1 = (2, 1, 3, 4, 5, 6, 3)
tp1
type(tp1)

tp2 = 2, 1, 3, 4, 5, 6, 3
tp2
type(tp2)

data
for k in data:
    b = k * 2
    print(b)
    
for k in data[:3]:
    b = k * 2
    print(b)
    
for i, k in enumerate(data):
    print(i, k)

print(list(enumerate(data)))

for i, k in enumerate(data, start=1):
    print(i, k)

# DICTIONArY

data = {'Name':'Kobkiat', 'Age':25, 'Score':35}
type(data)
data['Name']
data['Age']
data['Score']

datas = [{'Name' : 'Kobkiat', 'Age' : 25, 'Score' : 35},
         {'Name' : 'Ninan', 'Age' : 22, 'Score' : 26},
         {'Name' : 'John', 'Age' : 35, 'Score' : 32},
         {'Name' : 'Tim', 'Age' : 25, 'Score' : 29},
         {'Name' : 'Steal', 'Age' : 32, 'Score' : 27}]
type(datas)
datas[0]
datas[0:2]
datas[0]['Name']
datas[0]['Age']

for k in datas:
    print('{:8} {}'.format(k['Name'], k['Score']))