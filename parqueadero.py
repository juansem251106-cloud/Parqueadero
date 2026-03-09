def mostrar_parqueadero():
      print(parqueadero)

print(" Bienvenido seas al parqueadero ")
cupos = 10
opcion = 1
parqueadero = ["vacio"] * cupos

while opcion < 4:
   opcion = int(input("escoge la accion:\n1-ingresar\n2-retirar\n3-mostrar parqueadero\n4-salir\n"))

if opcion == 1:
      if "vacio" in parqueadero:
            placa = input("ingresa la placa: ")
            if placa in parqueadero:
                  print("el carro ya esta ingresado")
            else:
                  index = parqueadero.index("vacio")
                  parqueadero[index] = placa
                  
      else:
            print("parqueadero lleno")
            
      mostrar_parqueadero()
      
elif opcion == 2:
      if parqueadero.count("vacio") != 10:
            placa = input("ingresa la placa a retirar: ")
            if placa in parqueadero:
                 index = parqueadero.index("vacio")
                 parqueadero[index] = placa
            else:
                  print("el carro no esta ingresado")
      else:
       print("parqueadero esta vacio")
       mostrar_parqueadero
elif opcion == 3:
      mostrar_parqueadero

else:
      print("hasta luego")
