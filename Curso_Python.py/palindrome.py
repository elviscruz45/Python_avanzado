
def palindrome(entrada):
    a=entrada
    c=list(a)
    b=[]
    
    for i in range(len(c)):
        b.append(c[len(c)-1-i])
            
    if c==b:
        print("Es un palindrome")
    else:
        print("No es un palindrome")
        
    

if __name__=="__main__":
    entrada=input("Ingrese el nombre a revisar: ")
    palindrome(entrada)