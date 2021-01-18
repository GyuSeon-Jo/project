f1 = open("./chap4/Q#4/test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("./chap4/Q#4/test.txt", 'r')
print(f2.read())
f2.close()