# mostrar_menu_inicio() = muestra el menu de inicio, a menos que se decida salir
# crear_cuenta() = establece nuevo usuario, nueva contraseña correspondiente, avisa al programa que existe una cuenta, asigna el saldo default a esa cuenta, e imprime que se creo la cuenta 
# iniciar_sesion() = analiza si existe cuenta, si esto es así, crea variables input para comparar datos existentes de cuentas ya creadas con los ingresados ahora. si estos son los correctos ingresar a el menu principal, si no lo son imprimirle al usuario que no lo son y darle repetitivamente la oportunidad de ingresar.
# mostrar_menu_principal() = muestra el menu principal, a menos que se decida cerrar sesión
# consultar_saldo()
# depositar()
# retirar()
# ver_info_personal()
# mostrar_info_personal()
# mostrar_menu_personal()
# cambiar_nombre_usuario()
# cambiar_contraseña()
# transferir()



def consultar_saldo(saldo):
    print(f"Su saldo es de: {saldo}")
    print()

def depositar(saldo,monto_a_depositar):
    return saldo + monto_a_depositar

def retirar(saldo, monto_a_retirar):
    if saldo >= monto_a_retirar:
        saldo = saldo - monto_a_retirar
        exito = True
    else:
        exito = False
    return saldo, exito

def transferir(saldo, monto_a_transferir):
    if saldo >= monto_a_transferir:
        saldo = saldo - monto_a_transferir
        exito = True
    else: 
        exito = False
    return saldo, exito

def cambiar_nombre_usuario(nombre_nuevo):
    return nombre_nuevo

def cambiar_contraseña(contraseña_nueva):
    return contraseña_nueva

print("Bienvenido al Banco de Python")
opcion_inicio = 0
cuenta_existente = False
while opcion_inicio != 3 : 
    print("1 - Iniciar Sesión.")
    print("2 - Crear cuenta.")
    print("3 - Salir.")
    opcion_inicio = int(input("Qué desea hacer?: "))
    if opcion_inicio not in [1,2,3]:
        print("Opción inválida")
    elif opcion_inicio == 1 and cuenta_existente == True:
        inicio_sesion_usuario = input("Usuario: ").strip()
        inicio_sesion_contraseña = input("Cotraseña: ")
        while inicio_sesion_usuario != usuario or inicio_sesion_contraseña != contraseña:
            print("Los datos ingresados son incorrectos")
            inicio_sesion_usuario = input("Usuario: ").strip()
            inicio_sesion_contraseña = input("Cotraseña: ")
            print()     
        print("Iniciando sesión...")
        print()
        opcion = 0
        print(f"Bienvenido, {usuario}")  
        while opcion != 6 :
            print("1 - Consultar saldo")
            print("2 - Depositar dinero")
            print("3 - Retirar dinero")
            print("4 - Ver información personal")
            print("5 - Transferir")
            print("6 - Cerrar sesión")
            print()
            opcion = int(input("Que desea hacer?: "))
            if opcion not in [1,2,3,4,5,6]:
                print("Opción inválida")
            elif opcion == 1:
                consultar_saldo(saldo)
            elif opcion == 2:
                monto_a_depositar = int(input("Cuanto desea depositar?: "))
                while monto_a_depositar <= 0:
                    print("El depósito debe ser de una cantidad mayor a 0.")
                    monto_a_depositar = int(input("Cuanto desea depositar?: "))
                saldo = depositar(saldo,monto_a_depositar)
                print(f"Ha depositado {monto_a_depositar} exitosamente")
                print(f"Su saldo actual es de {saldo}")
                print()
            elif opcion == 3:
                monto_a_retirar = int(input("Cuanto desea retirar?: "))                
                while monto_a_retirar <= 0:
                    print("La cantidad de dinero a retirar debe ser mayor a 0.")
                    monto_a_retirar = int(input("Cuanto desea retirar?: "))
                saldo,exito = retirar(saldo, monto_a_retirar)
                if exito :
                    print(f"Ha retirado {monto_a_retirar} exitosamente")
                    print(f"Su saldo actual es de: {saldo}")
                    print()
                else:
                    print("Fondos insuficientes para retirar la cantidad indicada.")
                    print()
            elif opcion == 4:
                print("Información Personal:")
                print(f"Nombre de usuario: {usuario}")
                #print(f"Contraseña: {contraseña}")
                print(f"Saldo: {saldo}")
                print()
                opcion_inf_personal = 0
                while opcion_inf_personal != 3: 
                    print("1 - Cambiar nombre de usuario")
                    print("2 - Cambiar contraseña")
                    print("3 - Salir")
                    print()
                    opcion_inf_personal = int(input("Opcion: "))
                    if opcion_inf_personal not in [1,2,3] :
                        print("Seleccione una opción válida.")
                    elif opcion_inf_personal == 1:
                        print("Escriba su nuevo nombre de usuario")
                        nombre_nuevo = input().strip()
                        usuario = cambiar_nombre_usuario(nombre_nuevo)
                        print(f"Su nombre de usuario ha sido modificado correctamente, {usuario}")
                        print()
                    elif opcion_inf_personal == 2:
                        print("Para modificar su contraseña, primero tiene que ingresar su contraseña actual, por cuestiones de seguridad")
                        intento_contraseña = input("Ingrese su contraseña: ")
                        while intento_contraseña != contraseña:
                            print("Contraseña incorrecta.")
                            intento_contraseña = input("Ingrese su contraseña: ")
                        contraseña_nueva = input("Nueva Contraseña: ")
                        contraseña = cambiar_contraseña(contraseña_nueva)
                        print(f"Su contraseña ha sido modificada correctamente, {usuario}")
                        print()
                    elif opcion_inf_personal == 3:
                        print("Volviendo al menú principal")
            elif opcion == 5:
                receptor_transferencia = input("A quien deseas transferirle: ")
                monto_a_transferir = int(input("Monto a transferir: "))
            while monto_a_transferir <= 0:
                print("El monto a transferir debe ser mayor a 0")
                monto_a_transferir = int(input("Monto a transferir: "))
                print()
            saldo, exito = transferir(saldo,monto_a_transferir)
            if exito:
                print("Transferencia realizada")
                print(f"Se transfirió {monto_a_transferir} a {receptor_transferencia}")
                print(f"Saldo actual: {saldo}")
                print()
            else:
                print("Fondos insuficientes")
                print()
    elif opcion_inicio == 1 and cuenta_existente == False:
        print("Para iniciar sesión, tienes que crear una cuenta primero.")
        print()
    elif opcion_inicio == 2:
        usuario = input("Establece nuevo nombre de usuario: ").strip()
        contraseña = input("Establece una nueva contraseña: ")
        print("Cuenta creada exitosamente.")
        cuenta_existente = True
        saldo = 100000
        print()
print("Fin del programa.")   


# #if inicio_de_sesion == True:
# saldo = 100000
# opcion = 0
# print("Bienvenido," , usuario)
# while opcion != 5 :
#     print("1 - Consultar saldo")
#     print("2 - Depositar dinero")
#     print("3 - Retirar dinero")
#     print("4 - Ver información personal")
#     print("5 - Cerrar sesión")
#     print()
#     opcion = int(input("Que desea hacer?: "))
#     if opcion != 1 and  opcion != 2 and opcion!= 3 and opcion != 4 and opcion != 5:
#         print("Opción inválida")
#     elif opcion == 1:
#         print("Su saldo es de " , saldo)
#         print()
#     elif opcion == 2:
#         deposito = int(input("Cuanto desea depositar?: "))
#         saldo = saldo + deposito
#         print("Ha depositado" , deposito ,"exitosamente")
#         print("Su saldo actual es de" , saldo)
#         print()
#     elif opcion == 3:
#         retiro = int(input("Cuanto desea retirar?: "))
#         if saldo >= retiro:
#             saldo = saldo - retiro 
#             print("Ha retirado", retiro,"exitosamente")
#             print("Su saldo actual es de" , saldo)
#             print()
#         else:
#             print("Fondos insuficientes para retirar la cantidad indicada.")
#             print()
#     elif opcion == 4:
#         print("Información Personal:")
#         print("Nombre de usuario: " , usuario)
#         #print("Contraseña: " , contraseña)
#         print("Saldo: " , saldo)
#         print()
#         opcion_inf_personal = 0
#         while opcion_inf_personal != 3: 
#             print("1 - Cambiar nombre de usuario")
#             print("2 - Cambiar contraseña")
#             print("3 - Salir")
#             print()
#             opcion_inf_personal = int(input("Opcion: "))
#             if opcion_inf_personal != 1 and opcion_inf_personal != 2 and opcion_inf_personal != 3:
#                 print("Seleccione una opción válida.")
#             elif opcion_inf_personal == 1:
#                 print("Escriba su nuevo nombre de usuario")
#                 usuario = input()
#                 print("Su nombre de usuario ha sido modificado correctamente," , usuario)
#                 print()
#             elif opcion_inf_personal == 2:
#                 print("Para modificar su contraseña, primero tiene que ingresar su contraseña actual, por cuestiones de seguridad")
#                 intento_contraseña = input("Ingrese su contraseña: ")
#                 while intento_contraseña != contraseña:
#                     print("Contraseña incorrecta.")
#                     intento_contraseña = input("Ingrese su contraseña: ")
#                 contraseña = input("Escriba aquí su nueva contraseña: ")
#                 print("Su contraseña ha sido modificada correctamente," , usuario)
#                 print()
#             elif opcion_inf_personal == 3:
#                 print("Volviendo al menú principal")
# print("Fin del programa")
