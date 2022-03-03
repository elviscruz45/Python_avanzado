  
class Counter: 
    def __init__(self, start, end): 
        self.num = start 
        self.end = end 
  
    def __iter__(self): 
        return self
  
    def __next__(self):  
        if self.num > self.end: 
            raise StopIteration 
        else: 
            self.num += 1
            return self.num - 1
              
              
if __name__ == '__main__' : 
      
    a, b = 1, 5
      
    c1 = Counter(a, b) 
    c2 = Counter(a, b) 
      
    
    print ("Print the range without iter()") 
      
    for i in c1: 
        print ("Eating more Pizzas, couting ", i, end ="\n") 
        
        
        
              
        
      
    print ("\nPrint the range using iter()\n") 
    
    obj = iter(c2) 
    try: 
        while True: 
            print ("Eating more Pizzas, couting ", next(obj)) 
    except:  
        
        print ("\nDead on overfood, GAME OVER")