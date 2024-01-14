palabras = {}

def import_words():
    with open('palabras.txt', 'r') as archivo:
        for linea in archivo:
            palabra = linea.strip()
            if palabra in palabras:
                palabras[palabra] += 1  # Incrementar la frecuencia si la palabra ya existe
            else:
                palabras[palabra] = 1  # Agregar la palabra al diccionario con frecuencia 1
    return palabras

def show_words(palabras):
    for palabra, frecuencia in palabras.items():
        print(f"{palabra}: {frecuencia} veces")

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
                show_words(palabras)
            else:
                print("No hay palabras claves añadidas")

        elif opcion == '0':
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

