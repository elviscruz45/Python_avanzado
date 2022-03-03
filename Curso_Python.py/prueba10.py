lst = [11, 22, 33, 44, 55] 
  
iter_lst = iter(lst) 
while True: 
    try: 
        print(iter_lst.__next__())  
    except StopIteration: 
        break