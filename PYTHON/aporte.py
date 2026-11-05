edad = int(input("pone tu edad: "))
sueldo = float(input("pone el sueldo actual: "))

if sueldo < 10000:
    aporte = sueldo * 0.005
elif sueldo < 20000:
    aporte = sueldo * 0.01
elif sueldo < 30000:
    aporte = sueldo * 0.02
else:
    aporte = sueldo * 0.025


if edad <= 30:
    aporte = aporte * 1.20

print("El aporte sindical es: $", aporte)




