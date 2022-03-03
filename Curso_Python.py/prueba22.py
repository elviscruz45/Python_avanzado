
lista=[1,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,7,8]

a=lambda lista:list(set(lista))

print(a(lista))