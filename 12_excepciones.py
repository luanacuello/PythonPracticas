numb_one, numb_two, numb_three = 5, "1", 1

try:
    print(numb_one + numb_two)
except:
    print("Se ha produciodo un error")

try:
    print(numb_one + numb_three)
except:
    print("Se ha produciodo un error")
else:  #se ejecuta si no se produce una excepcion
    print("se ha ejecutado todo correctamente")
finally: #se ejecuta si o si
    print("continua el programa")

try:
    print(numb_one + numb_two)
except Exception as error:
    print("Se ha produciodo un TypeError")
    print(error)

"""
Las excepciones nos sirven para poder manejar errores.
Para controlar los errores con excepciones lo hacemos por medio de un try except, donde le decimos que intente ejecutar lo que le pasamos y si salta un error nos de la excepcion en lugar del error, contamos tambien con un else para decirle que si se ejecuto lo que estaba en el try haga determinada accion y un finally para decirle que realice determinada accion ya sea que se produzca o no una excepcion.

Tambien podemos manejar errores puntuales, lo hacemos aclarando cual es la excepcion al lado del except, ahora si ponemos un print y algo como "Se ha produciodo un error" nos imprimira solo eso pero no nos dira que clase de error o que fue lo que lo causo, para esto luego de nombrar al error le ponemos as error y le damos a que nos imprima error para poder visualizar los detalles de este.

para controlar cualquier tipo de excepcion en caso de no saber que la esta provocando o querer atajar cualquiera en donde ponemos el tipo de excepcion ponemos Exception.


"""