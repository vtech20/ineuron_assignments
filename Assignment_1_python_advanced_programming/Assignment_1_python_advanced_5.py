class Bool_list:
    def __init__(self, str1):
        self.str1 = str1
    
    def bool_list(self):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        out_list = []
        for ele in self.str1:
            out_list.append(bool((alphabets.index(ele)+1)%2))
        print(f'to_boolean_list({self.str1}) ➞ {out_list}')

n = input("Enter the string to convert to Bool list : ")
b = Bool_list(n)
print(b.bool_list())