class combinations:
    def __init__(self, *args):
        self.args = args[0]
        print(self.args)
    
    def combinations(self):
        out_num = 1
        for ele in self.args:
            out_num *=ele
        
        return (f'combinations of {self.args} -> {out_num}')

tup_inp = eval(input("Enter the number of items in a group : "))
c = combinations(tup_inp)
print(c.combinations())