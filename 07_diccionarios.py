my_dict =  dict()
my_other_dict = {}

print(type(my_dict))

my_other_dict = {"nombre":"Luana", "apellido":"Cuello", "edad": 23}

my_dict = {
    "nombre":"Luana",
    "apellido":"Cuello",
    "edad": 23,
    "lenguajes" : {"Python", "Java", "JavaScript"}
}
print(my_dict["nombre"])

my_dict["nombre"] = "Lua"
print(my_dict["nombre"])

my_dict["calle"] = "LuaStreet"
print(my_dict)

print("Lua" in my_dict)

"""
Los diccionarios son otro tipo de dato que nos sirve para almacenar datos, pero es lo hace en forma de relacion clave-valor, es decir que para cada dato podemos asignar un valor, osea que guarda la informacion en formato de pares.

cada clave solo puede tener un valor por lo que si queremos pasar varios lo podemos hacer pasandolo como un objeto de tipo lista por ejemplo.

Los diccionarios son mutables, por lo que podemos modificar el valor de una clave, ademas podemos acceder a los valores pasando la clave como lo hariamos con los indices en una lista.

Tambien podemos agregar una nueva clave-valor asignando un valor a una clave, y para consultar si un elemento se encuentra en el diccionario lo hacemos al igual que en los sets.

al igual que con los demas podemos acceder a los valores por medio de la clave en lugar del indice.
"""