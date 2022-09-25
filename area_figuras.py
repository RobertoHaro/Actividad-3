import math

def triangle():
    base = float(input("\nBase: "))
    high = float(input("altura: "))
    print("\nEl area es: %.2f" % ((base*high)/2), "mtrs cuadrados")

def rectangle():
    base = float(input("\nBase: "))
    high = float(input("altura: "))
    print("\nEl area es: %.2f" % (base*high), "mtrs cuadrados")

def circle():
    radio = float(input("\nRadio: "))
    print("\nEl area es: %.3f" % (math.pi*(radio**2)), "mtrs cuadrados")

def menu():
    x = True
    while x == True:
        print("\nCalculo de areas en metros")
        print("1)Triangulo\n2)Rectangulo\n3)Circulo\nx)Salir")
        opc = str(input("->"))
        if opc == '1':
            triangle()
            menu()
        elif opc == '2':
            rectangle()
            menu()
        elif opc == '3':
            circle()
            menu()
        elif opc == 'x':
            x =False

menu()