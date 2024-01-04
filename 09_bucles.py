#While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("el numero es mayor o igual que 10")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("el numero es igual que 15")
        break

print("continua la ejecucion")

#For
my_list = [35, 24, 62, 52, 30, 30, 17]

for x in my_list:
    print(x)

my_tuple = (23, 1.70, "Luana", "Cuello", "Lua")

for x in my_tuple:
    print(x)

my_set = {"Luana", "Cuello", 23}

for x in my_set:
    print(x)

my_dict = {"Nombre": "Luana", "Apellido": "Cuello", "Edad": 23, 1: "Python"}

for x in my_dict:
    print(x)

for x in my_dict.values():
    print(x)

for x in my_dict:
    print(x)
    if x == "Edad":
        break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")




"""
Los bucles son una serie de instrucciones que se ejecutan en un ciclo sin fin hasta que se cumpla la condicion que le pasamos.

En el while lo que hacemos es decirle que nos imprima en consola la variable my_condition y que le sume 1, si no le pusieramos que le sume 1, my_condition se va a imprimir en consola infiniteamente ya que siempre va a ser 0 y menor que 10 porque no le estamos indicando que haga nada mas, solamente que nos imprima la variable, ahora si le sumamos 1, el valor se va a incrementar en 1 y cuando llegue a 10 va a parar porque se cumple la condicion. 
Los while con como los if, con condicionales y hasta que una condicion se cumpla o sea cierta ejecutara las instrucciones que contenga, pero al igual que en los if,tambien contamos con else, que nos servira para ejecutar instrucciones cuando la condicion no se cumpla o deje de ser cierta.
Si necesitamos que por algun motivo el bucle deje de ejecutarse aun que la condicion aun no se cumpla o sea cierta, contamos con el break, que deja de ejecutar el bucle y continua ejecutando el resto del programa.

Tenemos los bucles de For tambien, estos nos sirven para recorrer estructuras de informcion que almacenan datos(listas, sets y tuplas), el for va a recorrer estas estructuras ejecutando las instrucciones que contenga hasta que llegue al final de la lista, osea que se ejecutara tantas veces como elementos haya.

en el caso de los diccionarios si le damos print a los elementos solo nos va a imprimir las claves, pero para acceder a los valores utilizamos el .values(). Al igual que con while contamos con else(acompañado antes de un if) y con un break para poder agregar condiciones y frenar el recorrido en caso de ser necesario, si el break se frena antes de el else, el else no se va a imprimir pero porque el else corresponde al for, y el for se rompio.

"""