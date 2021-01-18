#클래스에 변수를 전달하고 싶으면 __init__을 사용하여 변수를 설정(a = FourCal(4, 2))
#클래스에 속한 인스턴스에 변수를 전달하고 싶다면 setdata와 같이 변수를 설정해주는 인스턴스 따로 생성(a = FourCal()  a.setdata(4, 2))

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def divide(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
#a.setdata(4, 2)

#b = FourCal()
#b.setdata(3, 7)

print("4 + 2 = %d" %a.add())
print("4 - 2 = %d" %a.sub())
print("4 * 2 = %d" %a.mul())
print("4 / 2 = %d" %a.divide())
