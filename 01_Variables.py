my_variable = "Lua<3"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

print(my_variable, my_int_variable)

int_to_str = str(my_int_variable)
print(int_to_str)
print(type(int_to_str))
print(type(my_int_variable))

print(len(my_variable))

#podemos crear distintas variables en una sola linea pero hay que tener cuidado con el orden y no es recomendable por que no es una buena practica
name, surn, alias, age = "Luana", "Cuello", 'Lua', 23
print("me llamo:", name, surn, " mi edad es:",
      age, " y mi alias es:", alias)

name = input('Cual es tu nombre? ')
age = input('Cuántos años tienes? ')
print(name)
print(age)



"""
Una buena practica a la hora de definir variables es no seguir forma de camel case, sino definir las varibales toda con minuscula y separar las palabras con " _ " asi como tampoco hacer variables muy largas.

print() puede tomar mas de 1 argumento.

con la funcion str() podemos convertir un dato al tipo string

len() nos da la cantidad de caracteres de una variable

input() nos sirve para pedir datos al usuario y estamos cambiando el valor las variables de name y age definidas anteriormente

python no es de tipado fuerte por lo que podemos cambiar el tipo de dato de una variable sin ningun paso anterior
"""