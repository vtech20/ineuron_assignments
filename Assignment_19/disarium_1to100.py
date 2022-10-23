import math

class disarium_1:

    def print_disarium(self):
        disarium_num = []
        for i in range(1,100):
            count_digits = len(str(i))
            sum = 0
            x = i
            while (x!=0):
                r = x % 10
                sum = sum + math.pow(r,count_digits)
                count_digits = count_digits - 1
                x = x//10
            if sum == i:
                disarium_num.append(i)
        return disarium_num

print("Program to print the Disarium number between 1 to 100 : ")
ds = disarium_1()
c = ds.print_disarium()
print(f"The Disarium numbers between 1 and 100 are : {c}")