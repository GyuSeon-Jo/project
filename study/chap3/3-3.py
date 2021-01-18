'''
list = [1,2,3,4,5]
for i in list:
    print(i)


a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first+last)


marks = [90,25,67,45,80]
number = 0

for mark in marks:
    number += 1
    if mark >=60:
        print('%d번은 합격'%number)
    else:
        print('%d번은 불합격'%number)

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

a = [1,2,3,4]
result = []
result = [num*3 for num in a if num % 2 == 0]
print(result)
'''
result = [x*y for x in range(2,10)
                for y in range(1,10)]
print(result)