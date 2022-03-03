from datetime import datetime


times=datetime.now()
print(times)

string=times.strftime("%d/%m/%Y")
print(f"formato LATAM: {string}")


string=times.strftime("%m/%d/%Y")
print(f"formato LATAM: {string}")


string=times.strftime("Estamos en el año %Y")
print(f"formato LATAM: {string}")
