class Pronic:

   def check_pronic(self, num):
        flag = False;  
      
        for j in range(1, num+1):  
            if((j*(j+1)) == num):  
                flag = True  
                break  
        return flag
   
   def all_numbers(self):
    for i in range(1, 101):
        if(self.check_pronic(i)):
            print(i, " ")


p = Pronic()
p.all_numbers()
            
