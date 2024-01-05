class EmptyPerson:
    pass
 
class Person:
    def __init__(self, name, surn):
        self.name = name
        self.surn = surn

my_person = Person("Luana", "Cuello")
print(my_person.name)

class Person1:
    def __init__(self, name, surn, alias = "sin alias"):
        self.fullname = f"{name} {surn} ({alias})"

    def walk(self):
        print(f"{self.fullname} está caminando")

my_person1 = Person1("Luana", "Cuello")
print(my_person1.fullname)

my_person1.walk()

my_person1.fullname = "LuanaCuello++"
print(my_person1.fullname)


"""
LAS CLASES COMIENZAN CON MAYUSCULA y es recomendable que vaya todo junto, por ejemplo MyPerson

Para definir una clase simplemente ponemos antes del nombre la clase "class" y si aun esa clase no va a contener funciones, para que python no nos tire un error le ponemos pass, que lo que hace es decir que ignore el error y pase a lo que sigue de codigo, es decir ue el pass nos sirve para decir que mas tarde vamos a rellenar esa clase.

para construir una clase vamos a necesitar que tenga un constructor para poder definir sus atributos, para ello lo hacemos con def __init__(self): , __init__ funciona como constructor para inicializar los atributos de la clase y self hace referencia a que lo es de la misma clase donde se esta colocando, al lado de self vamos a ir colocando el resto de atributos que vaya a tener la clase

una vez definida la clase vamos a crear un objeto de esa clase que heredara sus atriibutos, en este caso name y surn, y le tendremos que asignar un valor a estos. A la hora de querer ver en consola nuestro objeto tendremos que indicar que atributo queremos ver osea clase.atributo.
Ahora como quise que me imprima el nombre completo lo que hice fue pasar como parametro deñ constructor el name y el surn y hacer un atributo fullname donde me los alamcene en un string, luego le paso los valores de los parametros al objeto y lo imprimo con el atributo fullname

ahora dentro del constructor le podemos agregar funciones propias de la clase que luego heredaran los objetos, para indicar que la funcion va a ser de la clase como parametro tambien le tendremos que pasar el self asi tambien podremos acceder a los atributos de esta.

tambien puedo cambiar el valor de un atributo, y poner un valor predeterminado encaso de que no se vaya a definir un valor para ese atributo
"""