palabras = []

def import_words():
    #abre el archivo en modo lectura
    with open('palabras.txt', 'r') as archivo:
        #Recorre cada linea del archivo y lo añade al array de palabras
        for linea in archivo:
            palabra = linea.strip()  # Elimina espacios en blanco y saltos de línea alrededor de la palabra
            palabras.append(palabra)
    return palabras

def show_words(palabras):
    #vemos la longitud de la lista
    total_palabras = len(palabras)
    #iniciamos variable i
    i = 0
    while i < total_palabras:
        #este bucle itera 20 veces el signo _ inidica que no se usa dentro del bucle
        #en range va lo que se va a recorrer y tras el for va cada elemento recorrido
        for _ in range(20):
            #indico si hay palabras para mostrar en la lista sino hace break
            if i < total_palabras:
                print(palabras[i])
                i += 1
            else:
                break
        input("Presiona Enter para mostrar las siguientes 20 palabras clave...")


#break romple el bucle ya que al usar while true la condicion siempre es verdadera,
#se podria hacer con una variable que cambiase a false al entrar en la opcion 0 pero
#asi se ahorran lineas

while True:
        print("1. Importar palabras clave")
        print("2. Mostrar palabras clave")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabras = import_words()
            print("Palabras añadidas")

        elif opcion == '2':
            #Podemos verificar si la lista palabras esta vacia o no
            #ya que si está vacia se considera como false y una no vacia
            #como true
            #TENEMOS que declarar la lista antes
            if palabras:
                show_words(palabras)
            else:
                print("No hay palabras claves añadidas")

        elif opcion == '0':
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

