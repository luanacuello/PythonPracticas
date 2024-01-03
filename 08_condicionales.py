my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")

my_condition =  5/5

if my_condition:
    print("Se ejecuta la condicion del 2do if")

if my_condition > 10 and my_condition < 20:
    print("es mayor a 10 y menor que 20")
elif my_condition == 1:
    print("es igual a 1")
else:
    print("es menor o igual que 10 o mayor o igual que 20")

my_string = "luaa"

if my_string:
    print("mi string no esta vacio")
else:
    print("mi string esta vacio")

if my_string == "luaa":
    print("mi string esta igual a luaa")

print("Continua la ejecucion")

##Ejercicio de condicional 
age = input("ingrese su edad : ")

if int(age) >= 18:
    print("es mayor de edad, es apto para conducir")
else: 
    years = 18 - int(age)
    if years != 0:
        print(f"es menor de edad, te faltan {years} años para conducir")

"""
En el condicional lo que siga despues del if tiene que ser verdadero para que el if se ejecute.

en el segundo if no le estamos pasando un valor booleano por lo que python lo toma como un valor y lo pasa como true, pero si nosotros le decimos por ejemplo que si my_condition sea igual a 11 la condicion no se cumple y no entra en el if.

si queremos que el condicional salte en caso de que el valor sea false podemos utilizar un else, entonces si el valor es true ingresa en el if, y si es false ingresa en el else. En un if podemos tener mas de una condicion y las podemos agregar con and 

Contamos con elif, que es una combinacion del else y el if, esto nos sirve par cuando dentro del condicional queremos agregar otra condicion y que haga algo especifico en ese caso, entonces si la condicion se cumple en el elif, entra ahi y no ejecuta ni lo del if ni lo del else.
"""