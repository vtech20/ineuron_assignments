import math

class disarium:
    def __init__(self,number):
        self.number = number

    def check_disarium(self):
        count_digits = len(str(self.number))
        sum = 0
        x = self.number
        while (x!=0):
            r = x % 10
            sum = sum + math.pow(r,count_digits)
            count_digits = count_digits - 1
            x = x//10
        if sum == self.number:
            return 1
        else:
            return 0

num = int(input("Enter the number to Check Disarium : "))
ds = disarium(num)
c = ds.check_disarium()
if c == 1:
    print("This is a Disarium number")
else:
    print("This is not a Disarium number")