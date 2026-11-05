suma = 0

for i in range(5):
  
    nota = float(input("Ingrese una nota (0 al 10): "))
    
    
    while nota < 0 or nota > 10:
        print("Nota incorrecta. Tiene que ser entre 0 y 10.")
        nota = float(input("Ingrese la nota otra vez: "))
        
   
    suma = suma + nota


promedio = suma / 5
print("El promedio de las notas es:", promedio)