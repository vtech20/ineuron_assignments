class Prime:
    def __init__(self, num):
        self.num = num
    
    def check_prime(self):
        out_bool = False
        if ((self.num-1)%6 == 0) or ((self.num+1)%6 == 0):
            out_bool = True
        print(f'prime({self.num}) ➞ {out_bool}')

n = int(input("Enter the number to check prime : "))
p = Prime(n)
print(p.check_prime())