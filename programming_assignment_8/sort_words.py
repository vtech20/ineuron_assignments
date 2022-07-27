import logging
import cmath

logging.basicConfig(level=logging.DEBUG,filename="sort_words.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class Word_sort:
    
    def __init__(self,a):
        self.a = a
        

    
    def sort_words(self):
        words = [word.lower() for word in self.a.split()]
        words.sort()
        print("The sorted words are:")
        for word in words:
           print(word)
        
    

try:
    a = input("Enter a string : ")
    ws = Word_sort(a)
    ws.sort_words()
    
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))