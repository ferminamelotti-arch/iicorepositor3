
opcion = 0


while opcion != 4:
    
    print("MENU DE OPCIONES" )
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
 
    opcion = int(input("Elegi una opcion (1-4): "))
    
    
    if opcion == 1:
        print("Elegiste la Opción 1.")
    elif opcion == 2:
        print("Elegiste la Opción 2.")
    elif opcion == 3:
        print("Elegiste la Opción 3.")
    elif opcion == 4:
        print("Saliste del programa")
    else:
        print("Opcion Invalida")