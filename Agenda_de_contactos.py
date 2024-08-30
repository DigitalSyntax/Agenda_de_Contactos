#Powered By Hernan Martinez 30/08/2024



def Mostrar_Menu():
    
    print("\nAgenda de contactos")
    print("1. Agregar nuevo contacto") 
    print("2. Eliminar contacto existente") 
    print("3. Buscar contacto") 
    print("4. Lista de contactos") 
    print("5. Salir de la Agenda") 
    print("\n")
    
    

def Agregar_Contacto(agenda):
    
    nombre = input("Por favor ingrese el nombre del contacto: ")
    Email = input("Por favor ingrese el email del contacto: ")
    Telefono = input("Por favor ingrese el telefono del contacto: ")
    print("\n")
    agenda[nombre] = {"telefono": Telefono , "email": Email}
    print(f"Se ha agregado el contacto {nombre} Exitosamente")
    



def Eliminar_Contacto(agenda):
    
    nombre = input("Ingrese el nombre del contacto a eliminar:")
    print("\n")
    if nombre in agenda:
      del agenda[nombre]
      print(f"El contacto {nombre} ha sido eliminado Exitosamente")
    else: 
        print(f"No se ha encontrado un contacto con el nombre: {nombre}")

    
    
    
def Buscar_Contacto(agenda):
    
    nombre = input("Por favor ingrese el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Nombre del contacto: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"No se encontró el contacto: '{nombre}' en la Agenda")
        
      
      
      
    
def Listado_Agenda(agenda):
    
    if agenda:
        print("\nLista de contactos: ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info['telefono']}")
            print(f"Email: {info['email']}")
            print("\n")
    else:
        print("La Agenda se encuentra vacia")
            
    
    
    


def Agenda_Contactos():
    
    agenda = {}
    
    while True:
        
        Mostrar_Menu()
        opcion = input("Por favor elija una opción:")
        print("\n")
        if opcion == "1":
            Agregar_Contacto(agenda)
        elif opcion == "2":
            Eliminar_Contacto(agenda)
        elif opcion == "3":
            Buscar_Contacto(agenda)
        elif opcion == "4":
            Listado_Agenda(agenda)
        elif opcion == "5":
            print("Saliendo de la Agenda, ¡Hasta pronto!")
            break
        else:
            print("Por favor seleccione una de las opciones valida ( 1 al 5)")                      
    



Agenda_Contactos()