#constructor
'''class demo():
    def __init__(self):
        print("Init method")
obj=demo()'''

'''class calc():
    def __init__(self):
        self.no1=20
        self.no2=30
    def add(self):
        print(self.no1+self.no2)
    def sub(self):
        print(self.no1-self.no2)
    def mul(self):
        print(self.no1*self.no2)
    def div(self):
        print(self.no1/self.no2)
        
obj1=calc()
obj2=calc()
obj3=calc()
obj3.add()
obj3.sub()
obj3.mul()
obj3.div()'''

class calc():
    def __init__(self,a,b):
        self.no1=a
        self.no2=b
    def show(self):
        print(self.no1+self.no2)
obj1=calc(30,6)
obj1.show()
