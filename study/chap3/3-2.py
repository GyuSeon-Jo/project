'''
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number :
"""
number = 0;
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = True

while money:
    print("커피를 한 잔 주문하였습니다.")
    coffee -= 1
    print("남은 커피는 모두 %d잔 입니다.\n"%coffee)
    if coffee > 0 :
        pass
    elif coffee == 0:
        print("sold out : 모든 커피가 판매되었습니다.")
        break

coffee = 10
while True:
    money = 300
    cnt = int(input('몇 잔을 주문하시겠습니까? : '))
    money *= cnt
    print("%d잔을 주문하셨습니다. 가격은 %d원입니다.\n" % (cnt, money))
    coffee -= cnt
    if coffee == 0:
        print("모든 커피가 판매되었습니다.")
        break
'''

coffee = 10
price = 300
while True:
    coin = int(input("돈을 넣어주세요 : "))
    order = int(input("몇 잔을 주문하시겠습니까? : "))
    total_price = price * order
    if order > coffee:
        print("현재 %d잔 미만으로 주문 가능합니다.")
    if total_price > coin:
        print("%d원이 부족합니다." %(total_price-coin))
    elif order <= coffee :
        charge = coin - total_price
        print("%d잔을 주문하셨습니다. %d원입니다. 잔돈은 %d원입니다."%(order, total_price, charge))
        coffee -= order
    if coffee == 0:
        print("모든 커피가 판매되었습니다.")
        break
