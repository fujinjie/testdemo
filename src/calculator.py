# -*- coding: utf-8 -*-

class Calculator:

    def __init__(self):
        pass

    def addFunc(self,a,b):
        return a + b

    def minFunc(self,a,b):
        return a - b

    def mulFunc(self,a,b):
        return a * b

    def divFunc(self,a,b):
        return a / b

    def assertNumInput(self,num):
        try:
            float(num)
            return True
        except:
            return False

    def mainFunc(self,num_1=None,f=None,num_2=None):
        if num_1 == None:
            num_1 = input ("请输入数字： ")
        while self.assertNumInput(num_1) == False:
            num_1 = input("请输重新入正确的数字： ")
        if f == None:
            f = input ("请输入（+、-、*、/)任一运算符： ")
        while f not in ["+","-","*","/"]:
            f = input("输入的运算符不正确，请输入（+、-、*、/)任一运算符： ")
        if num_2 == None:
            num_2 = input ("请输入数字： ")
        while self.assertNumInput(num_2) == False :
            num_2 = input("请输重新入正确的数字： ")

        if f == "+":
            result = self.addFunc(a=float(num_1),b=float(num_2))
            print("结果： " + str(result))
            return result
        elif f == "-":
            result = self.minFunc(a=float(num_1),b=float(num_2))
            print("结果： " + str(result))
            return result
        elif f == "*":
            result = self.mulFunc(a=float(num_1),b=float(num_2))
            print("结果： " + str(result))
            return result
        elif f == "/":
            if num_2 == "0":
                num_2 = input("输入的除数不能为0，请重新输入非0数字： ")
            result = self.divFunc(a=float(num_1),b=float(num_2))
            print("结果： " + str(result))
            return result

if __name__ == '__main__':
    run = Calculator().mainFunc('0.01','+','0.1')