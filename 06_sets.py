my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Lua", "Cuello", 23}

print(type(my_other_set))

my_other_set.add("Luana")
print(my_other_set)
print("Luana" in my_other_set)
print("Luani" in my_other_set)

my_other_set.clear()
print(len(my_other_set))

my_set = {"Lua", "Cuello", 23}
my_list = list(my_set)

print(my_list)
print(my_list[0])

"""
los sets son un tipo de dato como las listas y tuplas, nos sirven para almacenar datos, y al igual que estas tiene funciones propias de python para interactuar con los sets.

como sabemos python es un lenguaje de alto nivel, y no es de tipado fuerte, por lo que como podemos ver podemos definir una variable de un tipo y al ponerle datos se torne a otro tipo como en el caso de my_other_set.

Los sets no son de estructura ordenada, por lo que no podemos acceder a sus elementos por medio de un indice, es como si metieramos cosas dentro de una bolsa. Los sets tampoco admiten duplicados.

Para comprobar si un elemento forma parte de un set lo podemos hacer con print y con la funcion in preguntamos si dicho elemento se encuentra en el set, y nos lo dira con un booleano, para acceder a sus elementos, como no podemos hacerlo por su indice, lo hacemos colocando el dato directamente.

Con la funcion de Clear() podemos vaciar el set dejandolo vacio.

Si quisieramos hacer determinadas funcionalidades con los sets y por su comportamiento no pudieramos lo podriamos convertir en una lista y por ejemplo, ahi podriamos obtener una estructura ordenada y acceder a los elementos por su indice. Y asi con los demas tipo de variable que sirve para almacenar datos.
"""