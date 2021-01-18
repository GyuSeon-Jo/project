def add(a, b):
    return a+b

'''
x = 1
y = 2
z = add(x,y)

print(z)
print(add(2,3))


def say():
    return "Hi"

print(say())

#매개변수를 지정하여 사용도 가능
result = add(a = 1, b = 2)
print(result)

#아래와 같이 지정하면 순서에 상관없다
result = add(b=2, a=7)
print(result)


#다중 입력
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

res = add_many(1,2,3)

print(res)


#다중 입력 응용
def calc(work, *args):
    if work == 'add':
        result = 0
        for i in args:
            result += i

    elif work == 'mul':
        result = 1
        for i in args:
            result *= i

    return result

add = calc('add', 1,2,3,4,5)
mul = calc('mul', 1,2,3,4,5)

print(add)
print(mul)


#딕셔너리 생성 함수
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name = 'hello', age = 25)

#함수 탈출
def say(nick):
    if nick == '헬로':
        return
    print('월드')

say('헬로')
say('안녕')
'''
def say_myself(name, old, man=True):
    if man:
        print(f'저는 {name}입니다. {old}세 남자입니다.')
    else:
        print(f'저는 {name}입니다. {old}세 여자입니다.')

say_myself('조규선', 25)
say_myself('조규선', 25, True)
say_myself('조규선', 25, False)