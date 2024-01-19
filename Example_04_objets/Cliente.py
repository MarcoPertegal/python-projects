class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

c = Cliente('3214243', 'si', 'no')
print(c)
print(c.nombre)

c.nombre = 'Juan'
print(c.nombre)

#A un objeto le podemos añadir atributos


