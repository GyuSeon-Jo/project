print("I eat {0} apples".format(3))

print("I eat {0} apples".format("five"))

number = 3
day = 5
print("I ate {0} apples. so I was sick {1} days.".format(number, day))

print("I ate {num} apples. so I was sick {days} days.".format(num = 7, days = 10))

#좌우 정렬
print("'{0:<10}'".format("hi"))
print("'{0:>10}'".format("hi"))

#^가운데 정렬
print("'{0:^10}'".format("hi"))

#:, ^ 사이에 넣은 기호는 공백 대신 들어감
print("'{0:~^10}'".format("hi"))

#문자열 앞에 f를 붙여도 포맷팅이 된다.(python 3.6 이상)
name = "홍길동"
age = 10
print(f"나의 이름은 {name}입니다. 나이는 {age}세 입니다.")
#변수 계산도 가능
print(f"10년 뒤 나이는 {age+10}세 입니다.")
#이런식으로도 가능(추후 자세히 배울 예정)
dic = {'apple':'사과', 'ten' : "10"}
print(f"apple은 {dic['apple']}, ten은 {dic['ten']}")

#문자열에서 문자 최초 인덱스 찾기
a = "Python is funny!"
print(a.find('y'))
#없으면 -1 반환(find 대신 index를 쓰면 -1 반환이 아닌 오류가 발생)
print(a.find('x'))

#문자 삽입
a = "abcd"
print(",".join(a))

#공백 지우기
#좌측 공백 지우기
print("            hi".lstrip())
#우측 공백 지우기
print("hi            ".rstrip())
#양쪽 공백 지우기
print("      hi      ".strip())

#문자열 치환 : 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
a = "Python is funny"
print(a.replace("funny","suck"))

#문자열 나누기
a = "Life is too short"
print(a.split())