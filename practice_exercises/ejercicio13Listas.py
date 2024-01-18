#Escribir un programa que pregunte por una muestra de números, separados por comas,
# los guarde en una lista y muestre por pantalla su media y desviación típica.

list = []
listTotal = 0

numbers = input("Introduzca una serie de números separados por comas:")
list = numbers.split(',')
print(list)

for num in list:
    listTotal += int(num)

print(listTotal)
media = listTotal / len(list)
print(media)

