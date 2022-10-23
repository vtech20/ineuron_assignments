import numpy as np

class list_operations:
    def __init__(self,lst1):
        self.lst1 = lst1
    
    def sum_elements(self):
        return sum(self.lst1)
    
    def mul_elements(self):
        return np.prod(self.lst1)
    
    def small_elements(self):
        return min(self.lst1)
    
    def largest_elements(self):
        return max(self.lst1)
    
    def second_largest(self):
        new_lst = list(set(self.lst1))
        new_lst.sort()
        return new_lst[-2]
    
    def even_numbers(self):
        new_list_even = list(filter(lambda x: (x % 2 == 0), self.lst1))
        return new_list_even

    def odd_numbers(self):
        new_list_odd = list(filter(lambda x: (x % 2 == 1), self.lst1))
        return new_list_odd

    def n_largest(self,n):
        new_lst_n = list(set(self.lst1))
        new_lst_n.sort()
        return new_lst_n[-n]
    
    def remove_empty_list(self):
        res = [ele for ele in self.lst1 if ele != []]
        return res
    
    def copy_list(self):
        new_list_cpy = self.lst1.copy()
        return new_list_cpy

    def count_occurance(self):
        occurrence = {item: self.lst1.count(item) for item in self.lst1}
        return occurrence


print('!'*10, " find sum of elements in list ", '!'*10)
lst_sum_inp = eval(input("Enter a list to perform sum : "))
lsum = list_operations(lst_sum_inp)
print(lsum.sum_elements())
print("#"*20)
print('!'*10, " Multiply all numbers in the list ", '!'*10)
lst_mul_inp = eval(input("Enter a list to perform product : "))
lmul = list_operations(lst_mul_inp)
print(lmul.mul_elements())
print("#"*20)
print('!'*10, " find smallest number in a list ", '!'*10)
lst_sma_inp = eval(input("Enter a list to find smallest number : "))
lsma = list_operations(lst_sma_inp)
print(lsma.small_elements())
print("#"*20)
print('!'*10, " find largest number in a list ", '!'*10)
lst_lar_inp = eval(input("Enter a list to find largest number : "))
llar = list_operations(lst_lar_inp)
print(llar.largest_elements())
print("#"*20)
print('!'*10, " find second largest number in a list ", '!'*10)
lst_second_lar_inp = eval(input("Enter a list to find second largest number : "))
lslar = list_operations(lst_second_lar_inp)
print(lslar.second_largest())
print("#"*20)
print('!'*10, " find N largest elements from a list ", '!'*10)
lst_nlar_inp = eval(input("Enter a list to find nth largest number : "))
lsnlar = list_operations(lst_nlar_inp)
n_val = int(input("Enter the n value to find nth largest number : "))
print(lsnlar.n_largest(n_val))
print("#"*20)
print('!'*10, " print even numbers in a list ", '!'*10)
lst_even_inp = eval(input("Enter a list to find even number : "))
lseven = list_operations(lst_even_inp)
print(lseven.even_numbers())
print("#"*20)
print('!'*10, " print odd numbers in a list ", '!'*10)
lst_odd_inp = eval(input("Enter a list to find odd number : "))
lsodd = list_operations(lst_odd_inp)
print(lsodd.odd_numbers())
print("#"*20)
print('!'*10, " Remove empty List from List ", '!'*10)
lst_empty_inp = eval(input("Enter a list to remove empty list : "))
lsempty = list_operations(lst_empty_inp)
print(lsempty.remove_empty_list())
print("#"*20)
print('!'*10, " Cloning or Copying a list ", '!'*10)
lst_clone_inp = eval(input("Enter a list to clone list : "))
lsclone = list_operations(lst_clone_inp)
print(lsclone.copy_list())
print("#"*20)
print('!'*10, " Count occurrences of an element in a list ", '!'*10)
lst_count_inp = eval(input("Enter a list to count occurances : "))
lscount = list_operations(lst_count_inp)
print(lscount.count_occurance())
print("#"*20)

            


