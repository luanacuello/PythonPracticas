empty_list = []
other_empty_list = list()
names_list = ['lua','luis','vico']

print(len(names_list))

my_other_list = [23, 1.70, "Lua", "Cuello"]

print(my_other_list[2])
print(type(my_other_list))

age, height, name, surn = my_other_list[0], my_other_list[1], my_other_list[2], my_other_list[3]

print(name)

names_list.append("luana")
names_list.insert(1, "azul")
print(names_list)
names_list.remove("azul")
print(names_list)

"""
Podemos tener listas vacias para ir alamacenando datos o definir listas con datos adentro, y tenemos 2 formas de crearlas, sus constructores pueden ser [] o list()
con un print y un len adentro podemos ver la longitud de la lista, osea cuantos elementos contiene.

Las listas al igual que los arrays comienzan con indice 0
en una misma lista podemos almacenar distintos tipos de datos y podmeos acceder a sus elementos dandole print al indice de dicho elemento

tambien como podiamos definir una variable en una sola linea de codigo lo podemos hacer con las listas, podemos definir variables y asignarles como valor un elemento de la lista, esto lo hacemos accediendo a su indice, esto de todas formas no es una buena practica

las listas son un tipo de objetos.

para acceder a las funciones con las que podemos interactuar con las listas escribimos el nombre de la lista y nos da el listado, yo utilice append que es con la que podemos agrear elementos a la lista y los agrega al final y si queremos aregarlo en una posicion especifica podemos usar insert, con remove podemos eliminar elementos
"""