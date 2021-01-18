i = 1
res = 0
while True:
    if i > 1000:
        break
    else:
        if i % 3 == 0:
            res +=i
    i += 1
print(res)