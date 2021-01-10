#주식 코드
class stock :

    def __init__(self, name, price):
        self.name=name
        self.price=price

    def info(self):
     print("{0}의 가격은 {1}원 입니다.".format(self.name, self.price))

    def change(self, price) :
        self.price = price
        print("가격은 : {0}원 입니다.".format(self.price))

#액면분할
class div_stock(stock):
    def __init__(self, name, price, amount) :
        stock.__init__(self, name, price)
        
        self.amount=amount

    def divide_stock(self):
        self.afterprice = self.price/self.amount
        print("{0}의 액면분할 후 가격은 {1}원 입니다.".format(self.name, self.afterprice))

Samsung = div_stock("삼성전자", 80000, 10)
Samsung.divide_stock()

#가격변동 : 퍼센트로

class stock_updown:
    def __init__(self, name, start_price, percent):
        self.name=name
        self.start_price=start_price
        self.percent=percent
    
    def end_price(self):
        after_price = 0
        after_price = self.start_price * (1+self.percent/100)
        print("{0}의 종가는 {1}%오른 {2}원 입니다.".format(self.name, self.percent, after_price))

Samsung = stock_updown("삼성전자", 80000, 2.23)
Samsung.end_price()


#손절, 익절 프로그램


