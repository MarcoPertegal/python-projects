print("tu puta madre")

#En java no tenemos variables que se pueden usar tanto dentro de la funcion como fuera en java habia que pasarsela por parametro
saludo = "Cangondio vare"

def saludar():
    #Para modificarla a nivel global usamos global
    global saludo

    #Si modificamos una variable dentro de un metodo no se modifica la variable global
    saludo = "Hola a todos"
    print(saludo)

saludar()



def coord(ciudadBuscar):
    if ciudadBuscar == 'Sevilla':
        #Podemos hacer un retorno multiple
        return 473, -50659345
    else:
        return 0,0

lat, long = coord('Sevilla')

print(lat)
print(long)

#El orden de los apametros puede variar si no especificamos las variables sigue el orden
def sumar(a,b):
    return a+b

print(sumar(b=1, a=2))

#Podemos pasar un numero variable de argumentos a una funcion que lo tratara cxomo una especie de lista que podemos
#recorrer como un for, estos argumentos pueden ser de distinto tipo
def sumar2(*args):
    result = 0
    for n in args:
        result +=n
    return result

print(sumar2(2,3))
print(sumar2(2,3,4,5,6))





