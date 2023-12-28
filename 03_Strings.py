line_string = "Este es un string\ncon salto de línea"
print(line_string)

tab_string = "\tEste es un String con tabulación"
print(tab_string)

scape_string = "\\tEste es un string \\n escapado"
print(scape_string)

name, surn, age = "Lua", "Cuello", 23
print("Mi nombre es {} {} y mi edad es {}".format(name, surn, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surn, age))
print(f"Mi nombre es {name} {surn} y mi edad es {age}")

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

"""
Como vimos antes la funcion len() me ayuda a ver la cantidad de caracteres que tiene mi variable.
con \n hacemos un salto de linea, \t tabulacion(sangria)

FORMATEAR
sustituir en lugares correspondientes por los valores asignados, en el codigo puse distintas formas de hacerlo, se me resulta mejor la primer y tercer forma

podemos deletrear un string asignando sus caracteres en variables y metiendola en otra variable para luego recorrerla como una lista, como mostramos arriba con la palabra python

luego tenemos muchas mas funciones propias de python para poder manejar strings y las podemos enocntrar aqui
https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md
"""


