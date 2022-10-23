import math

class Happy1:
    def numSquareSum(self,n):
        squareSum = 0
        while(n):
            squareSum += (n % 10) * (n % 10)
            n = int(n / 10)
        return squareSum

    def check_happy(self):
        happy_numbers = []

        for i in range(1,101):     
            squareSum = 0
            squareSum = self.numSquareSum(i)
            while squareSum >= 10:
                squareSum = self.numSquareSum(squareSum)
                #print(squareSum)
            if squareSum == 1:
                happy_numbers.append(i)
        return happy_numbers

h = Happy1()
c = h.check_happy()
print(f"The Happy numbers between 1 and 100 are : {c}")
