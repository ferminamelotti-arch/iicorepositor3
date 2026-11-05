ancho = int(input("dime el ancho del lugar:  "))
largo = int(input("Dime el largo del lugar:    "))
precio = int(input("dime el precio del metro cuadrado:   "))
preciototal = ancho * largo * precio
print("el precio total es:", preciototal)
perimetro= ancho*2 + largo*2
alambre = perimetro*3
print("necesitas", alambre, "de alambre")
