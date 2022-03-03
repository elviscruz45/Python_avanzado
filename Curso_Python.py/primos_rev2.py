def primo(numero:int)->bool:
    lista=[x for x in range(2,numero) if numero%x==0]
    return len(lista)==0


print(primo("casa"))