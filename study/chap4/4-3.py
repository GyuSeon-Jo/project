'''
f = open("새파일.txt", 'r')
f.close()


f = open("./chap4/test.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close


f = open("./chap4/test.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close

#파일 요소를 배열 형태로 반환해줌
f = open("./chap4/test.txt", 'r')
lines = f.readlines()
print(lines)


#파일 내용 전체 반환
f = open("./chap4/test.txt", 'r')
data = f.read()
print(data)
f.close


#파일 내용 추가하기
f = open("./chap4/test.txt", 'a')
for i in range(11,21):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


#f.close()를 안써도 되는 다른 방법
with open("./chap4/test2.txt", 'w') as f:
    data = "Life is short! You need python!"
    f.write(data)
'''