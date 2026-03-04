print(" Bienvenido seas al parqueadero ")

espacio_total = 10
carros_parqueados = 5
espacio_disponible = 5

print("1-Elegir espacio \n2-Retirar carro \n3-Salir del sistema")
eleccion = input("seleccione una opcion: ")

opcion_1 = "1"
opcion_2 = "2"
opcion_3 = "3" 
while True:
 if eleccion == "1":
    
    if carros_parqueados <= espacio_disponible:
        carros_parqueados += 1
        print("Carro parqueado")

 if eleccion == "2":
    if carros_parqueados > 0:
        
       carros_parqueados -= 1
       print("Carro retirado")
        
 if eleccion == 3:
       print("Bye")  
    
 else:
        print("Error")
        break
