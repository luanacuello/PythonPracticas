def sumValue(numberOne, numberTwo, numberThree):
    print(numberOne + numberTwo + numberThree)


def printValue(value):
    print(value)

def main():
    printValue("hello")

if __name__ == '__main__':    
    main()

"""
if __name__ == '__main__': 

Esto nos sirve para ayudar a organizar el script a la hora de que se quiera importar como modulo para reutilizar el codigo, lo que hacemos es que fuera de la funcion main() vamos a poner las cosas que queremos que se reutilicen y lo que no dentro del main, entonces 
if __name__ == '__main__':    
    main()
lo que va a hacer es ejecutar el main solo si se ejecuta directamente y no desde un archivo donde se utiliza como modulo

"""