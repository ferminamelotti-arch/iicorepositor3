horario = int(input("Dime la hora actuaL:    "))
if horario <= 5:
    print("Es la madrugada")
if horario <= 11:
    print("es la mañana")
elif horario <= 13:
    print("es el mediodia")
elif horario <= 19:
    print("es la tarde")
elif horario <= 23:
    print("es la noche")
elif horario <= 0:
    print("ERROR")
else:
    print("ERROR")
