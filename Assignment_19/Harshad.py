class Harshad:

    def __init__(self,number):
        self.number = number
    
    def check_harshad(self):
        num = self.number
        digit_sum = 0
        harshad_num = False
        while num:
            digit_sum += num%10
            num //= 10
        
        if self.number%digit_sum == 0:
            harshad_num = True
            return harshad_num         
        else:
            harshad_num = False
            return harshad_num
            
inpnum = int(input("Enter the number to identify Harshad number : "))
h = Harshad(inpnum)
har = h.check_harshad()
if har:
    print('%d is Harshad Number' % (inpnum))
else:
    print('%d is Not Harshad Number' % (inpnum))