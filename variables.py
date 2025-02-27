nombre = "Moralens"
print(nombre)

# Type se utiliza para saber el tipo de dato que estamos utilizando
print(type(nombre)) # <class 'str'>

a = 50
b = a
print(b) # la variable b hace referencia al mismo valor
print(id(a)) # 140726948204504
print(id(b)) # 140726948204504: Tienen el mismo identificador

# Valor reasignado
a = 500
print(id(a)) # 2122402540976. El id es el identificador.

nombre = "James"
print(id(nombre))
edad = 20
print(type(edad))
print(id(edad))
altura = 1,90

"""Variables locales: Las variables que se declaran dentro
   de una funcion se llaman variables locales 
"""
def local():
    nom = "Joe"
    apellido = "Doe"
    print(f"Nombre completo: {apellido} {nom}")

local()

# Valores maximos en Python

x = 1000000
y = x + 1
print(y)
print(type(y)) # <class 'int'>