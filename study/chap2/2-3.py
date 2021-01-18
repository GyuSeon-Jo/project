#배열 스플릿
a = ['a', 'b', 'c', 'd']
b = a[0:2]
c = a[2:]

print('a = ', a)
print('b = ', b)
print('c = ', c)

#중첩 배열 스플릿
a = [1, 2, ['a', 'b'], 3, 4]
b = a[:2]
c = a[2][:2]
d = a[3:]

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

#배열 연산
a = [1, 2, 3]
b = [4, 5]

print(a+b)

#배열 길이
a = [1, 2, 3]
print(len(a))

#배열 요소 삭제
a = [1, 2, 3]
del a[0]
print(a)

#배열 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)

#배열 특정 인덱스에 삽입
#arr.insert(x,y) -> arr[x]에 y값 추가
a = [1, 2, 3]
a.insert(0,0)
print(a)


#배열 정렬, 역정렬
a = [1, 3, 2]
a.sort()
print(a)
a.reverse()
print(a)

#배열 요소 끄집어내기
#arr.pop(x) -> x번째 인덱스를 출력하고 삭제(미입력시 마지막 인덱스에 적용됨)
a = [1,2,3]
print(a.pop())
print(a)

#배열확장
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7, 8]
b.extend(a)
print(b)
#a.extend([4, 5])는 a += [4, 5]와 동일하다