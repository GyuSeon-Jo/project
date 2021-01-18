def is_odd(a):
    if a % 2 == 1:
        txt = "홀수입니다."
    else:
        txt = "짝수입니다."
    return txt

num = 10
print(is_odd(num))