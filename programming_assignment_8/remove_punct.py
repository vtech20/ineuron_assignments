import logging
import cmath

logging.basicConfig(level=logging.DEBUG,filename="remove_punctuation.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class Remove_punctuation:
    
    def __init__(self,a):
        self.a = a
        

    
    def remove_punct(self):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        no_punct = ""
        for char in self.a:
          if char not in punctuations:
             no_punct = no_punct + char
        
        print(no_punct)
        
    

try:
    a = input("Enter a string : ")
    rp = Remove_punctuation(a)
    rp.remove_punct()
    
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))