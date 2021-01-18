#이거 아님 그냥 패스함
def avg(*args):
    res = 0
    for i in args:
        res += i
    return res/len(args)

while True:
    num = int(input("숫자를 입력해주세요, 0 입력 시 정지 : "))
    if num == 0:
        break
    avg(num)

print(avg(1,2))