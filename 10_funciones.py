def my_function():
    print("mi función")

my_function()

def sum_two_values(a, b):
    print(a + b)

sum_two_values(1, 2)

def print_name(name, surn):
    print(f"{name} {surn}")

print_name(surn = "Cuello", name = "Luana")
print_name("Cuello" , "Luana")

def print_upper (*texts):
    for text in texts:
        print(text.upper())

print_upper("Hola", "Lua", "Cuello")

"""
Para definir una funcion  lo hacemos colocando def y el nombre de nuestra funcion y para llamarla simplemente escribimos la funcion sin el def.
"""