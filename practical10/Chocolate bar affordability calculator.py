class Staff(object):
    def __init__(self,price,money):
        self.price=price
        self.money=money
    def number(self):
        n=int(self.money/self.price)
        return n
c=Staff(7,100)
print(c.number())
