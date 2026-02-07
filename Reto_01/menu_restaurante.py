import csv
from datetime import datetime

#Nombre del archivo
menu_cvs = 'menu.csv'
log_compras = 'log_compras.csv'

#Funciones del menu
def mostrar_menu():
    print('Menu del Restaurante:')
    with open(menu_cvs, mode='r', encoding='utf8') as archivo:
        leer_archivo = csv.reader(archivo)
        for fila in leer_archivo:
            print(" | ".join(fila))
        print("\n")

def comprar_platillo():
    mostrar_menu()
    articulos_comprados = []
    costo_total = 0.0
    while True:
        id_platillo = input("Ingrese el ID del platillo que quiere comprar:")
        dato_encontrado = False
        with open(menu_cvs,mode='r',encoding='utf8') as archivo:
            leer_archivo = csv.DictReader(archivo)
            for fila in leer_archivo:
                if fila["ID"] == id_platillo:
                    platillo_comprado = (fila["NOMBRE_COMIDA"])
                    costo_platillo = fila["PRECIO"]
                    articulos_comprados.append((platillo_comprado, costo_platillo))
                    costo_total += float(costo_platillo)
                    print("Compra agregada")
                    dato_encontrado = True
                    break
        if not dato_encontrado:
            print("El ID no existe, ingrese un ID valido")  
        print("\n") 
        continuar = input("Desea comprar otro platillo? (s/n): ")
        if continuar.lower() != 's':
            break
    #Imprimir los articulos comprados
    if articulos_comprados:
        print("****** Orden de compra ******")
        for articulo, precio in articulos_comprados:
            print(f"{articulo} - ${precio}")
        print(f"Total a pagar: ${costo_total:.2f}")
        print("\n") 
    #Guardar datos en el log
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #productos= ", ".join(articulos_comprados)
    productos = ", ".join([f"{articulo} (${precio})" for articulo, precio in articulos_comprados])
    with open(log_compras,mode="a", encoding='utf8', newline='') as archivo_log:
        escribir_log = csv.writer(archivo_log)
        escribir_log.writerow([fecha, productos, f"${costo_total:.2f}"])

while True:
    print("***** BIENVENIDO AL SISTEMA *****")
    print("1-Crear un menu")
    print('2-Ver el menu')
    print('3-Comprar articulos del menu')
    print('4-Salir')
    print("\n")
    opcion = input("Seleccione una opcion: ")
    print("\n")
    if opcion == '1':
        #Abrimos el archivo
        with open(menu_cvs, mode='w', newline='', encoding='utf8') as archivo:
            escribir_csv = csv.writer(archivo)
            #Titulos para las columnas
            escribir_csv.writerow(['ID','NOMBRE_COMIDA', 'PRECIO'])
            print("Ingrese los articulos que desea agregar al menu:")
            while True:
                id = input("ID del alimento:")
                articulo = input("Nombre del alimento:")
                precio = input("Precio del alimento:")
                escribir_csv.writerow([id, articulo, precio])    
                salir = input("Desea agregar otro articulo? (s/n): ")
                print("\n")
                if salir != 's':
                    break       
    elif opcion == '2':
        mostrar_menu()
    elif opcion == '3':
        comprar_platillo()
    elif opcion == '4':
        break      
