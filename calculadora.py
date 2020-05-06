"""
PROGRAMADOR Hernandez Rojas Mara Alexandra
EDA I Grupo 13 Practica 9 introduccion a python
"""

def sumar(a, b):
    c = a + b
    return c

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def div_entera(a, b):
    if b == 0:
        print("Error division sobre CERO")
        return
    return a//b

def division(a, b):
    if b == 0:
        print("Error division sobre CERO")
        return
    return a/b

def modulo(a,b):
    if b == 0:
        print("Error divisioin sobre CERO")
        return
    return a%b

def potencia(a, b):
    return a**b
#A es la base B es la potencia

def main():

    print("Ingresa dos valores")
    x = int(input())#input es para leer desde teclado
    y = int(input())

    print("1.sumar\n2.restar\n3.division entera")
    print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
    op = int(input())

    while op !=8:
         if op == 1:
              print(sumar(x, y))
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())
         elif op == 2:
              print(restar(x, y))
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())
         elif op == 3:
              print(div_entera(x, y))
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())
         elif op == 4:
              print(division(x, y))
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())
         elif op == 5:
              print(modulo(x, y))
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())
         elif op == 6:
              print(potencia(x, y))
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())
         elif op == 7:
              print(multiplicar(x, y))
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())
         else:
              print("\nOpcion no valida\n")
              print("1.sumar\n2.restar\n3.division entera")
              print("4.division\n5.modulo\n6.potencia\n7.multiplicar\n8.Salir")
              op = int(input())

#en python no hay switch pero elif es su equivalente

if __name__ == "__main__":
    main()

