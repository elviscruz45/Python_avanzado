while True:
    try:
        x = int(input("Por favor ingrese un número \n> "))
        print(x)
        break
    
    except ValueError:
        print("Oops! No era válido. Intente nuevamente \n>")