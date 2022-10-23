import math

class Happy:
    def __init__(self,number):
        self.number = number

    def numSquareSum(self,n):
        squareSum = 0
        while(n):
            squareSum += (n % 10) * (n % 10)
            n = int(n / 10)
        return squareSum

    def check_happy(self):
        squareSum = self.numSquareSum(self.number)
        while squareSum >= 10:
            squareSum = self.numSquareSum(squareSum)
            #print(squareSum)
        if squareSum == 1:
            print(self.number, " - is a Happy number")
        else:
            print(self.number, " - is not a Happy number")

num = int(input("Enter the number to Check Happy number : "))
h = Happy(num)
c = h.check_happy()