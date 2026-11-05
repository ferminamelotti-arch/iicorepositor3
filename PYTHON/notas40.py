op = 0



print("1. Ingresar Notas")
print("2. Calcular Promedios")
print("3. mejor promedio")
print("4. Salir")
 
op = int(input("Elegi una opcion:  "))
while op !=4:
 match op:
     case 1:
       mayor = 0
       menor = 0
      
 
 for alumno in range(1,41):
     suma = 0
     print("alumno", alumno)

 for nota in range (1,11):
     n = float(input("Ingrese la nota: "))
     suma = suma + n
     promedio = suma / 10
     print("Promedio:", promedio)
     if promedio >= 7:
        print("Esta aprobado")
     else:
        print("esta desaprobado")
        if promedio > mayor:
             mayorprom = promedio
             mejoralum = alumno
     
 
 match op:
    case 2: 
     print("Las notas ya fueron cargadas")
 

 match op: 
    case 3:
     print("el alumno con mayor promedio es", mejoralum, "y su promedio es", mayorprom)


 match op:
    case 4:
    
     print("final del programa")




