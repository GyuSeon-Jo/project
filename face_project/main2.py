import cv2

#얼굴 인식 필터 추가
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#모자이크 해야할 사진 불러오기
src = cv2.imread('sample5.jpeg')
cv2.imshow('BEFORE', src)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

#모자이크 농도 설정
ratio = 0.06

for x, y, w, h in faces:
    small = cv2.resize(src[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    src[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

cv2.imwrite('result.jpg', src)
cv2.imshow('AFTER', src)
cv2.waitKey(0)