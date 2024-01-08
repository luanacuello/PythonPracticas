import mi_modulo
from mi_modulo import sumValue


mi_modulo.sumValue(5, 8, 7)
mi_modulo.printValue("Hola Lua")


sumValue(5, 8, 7)




"""
Los modulos nos permiten importar ficheros(en realidad esto es amplio ya que modulos son pedazos de codigo, y esto no siempre va a ser un fichero) para poder reutilizar el codigo sin la necesidad de tener que copiar y pegar, para ello primero ponemos import y el nombre del fichero al que queremos acceder, luago para utilizar, por ejemplo, una funcion colocamos mi_fichero.funcion.

tambien si no queremos importar todo el fichero para optimizar e importar solo una funcion podemos hacerlo poniendo from mi_fichero import funcion.

Tenemos que tener cuidado con la sintaxis de los ficheros, ya que para poder importar el nombre del fichero tiene que comenzar con minuscula y no con numero o mayuscula
"""