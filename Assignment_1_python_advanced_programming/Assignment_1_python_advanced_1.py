class symbol_values:
    def __init__(self, lst):
        self.lst = lst
    
    def calculate_sym_score(self):
        check_dict = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
        out_num = 0
        check_nested = any(isinstance(i, list) for i in self.lst)
        if check_nested:
            for ele in self.lst:
                for sub_ele in ele:
                    out_num += check_dict[sub_ele]
        else:
            for elem in self.lst:
                out_num += check_dict[elem]
        
        return out_num

lst_inp = eval(input("Enter the list with symbols : "))
s = symbol_values(lst_inp)
print(s.calculate_sym_score())
