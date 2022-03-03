  
listB = ['Cat', 'Bat', 'Sat', 'Mat'] 
  
  
iter_listB = listB.__iter__() 
  
try: 
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) 
    print(iter_listB.__next__()) 
except: 
    print(" \nThrowing 'StopIterationError' \n",
                     "I cannot count more.") 
