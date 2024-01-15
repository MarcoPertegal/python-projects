palabras = {}

def import_words():
    with open('palabras.txt', 'r') as archivo:
        for linea in archivo:
            palabra = linea.strip()
            #comprueba si la palabra recorrida en el bucle está en el
            #diccionario usando in
            if palabra in palabras:
                #si la palabra se encuentra amumenta el valor de la frecuencia asociada
                #a esa palabra en uno, la frecuencia es el valor asociado a cada palabra
                #se agrega 1 al valor asociado a esa palabra en el diccionario.
                palabras[palabra] += 1
            else:
                #Agregar la palabra al diccionario con frecuencia 1
                palabras[palabra] = 1
    return palabras

def show_words():
    contador = 0
    #usamos los pares de valores del diccionario
    #el .items es un metodo de los diccionarios y podemos extraer los elementos clave valor
    #Los bucles for in no nos permiten recoger partes de la lista sino que toda la lista entera
    for palabra, frecuencia in palabras.items():
        #usando la f podemos imprimir variables
        #para imprimir variables que son int debemos pasarlas a str sino peta
        #como esto es poco legible se usa f-string para imprimir variables int y str al mismo tiempo
        #print(palabra+":" +str(frecuencia)+ "veces")
        print(f"{palabra}: {frecuencia} veces")
        contador += 1
        if (contador == 3):
            input("Pulse una tecla para continuar")
            contador = 0

while True:
        print("1. Importar palabras clave")
        print("2. Mostrar palabras clave")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            palabras = import_words()
            print("Palabras añadidas")

        elif opcion == '2':
            if palabras:
                show_words()
            else:
                print("No hay palabras claves añadidas")

        elif opcion == '0':
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

