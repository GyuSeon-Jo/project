'''
money = 2000
card = True

if money >= 10000 and card:
    print('taxi')
else:
    print("walk")

if 'a' in ('a', 'b', 'c'):
    print('yes')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("taxi")
'''

pocket = ['paper', 'cellphone', 'money']
card = True
if "money" in pocket:
    print("taxi")
elif card:
    print("taxi")
else:
    print("walk")