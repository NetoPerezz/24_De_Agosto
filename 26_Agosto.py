'''Ernesto Perez 3D
 26 de Agosto 2022'''
# Importar modulos desde otros archivos en una carpeta
import ops.operaciones as op  # Importar el modulo con (import) con un punto(.) y (as) para hacer una referencia al modulo
import ops.sumar as s
import ops.cuadrado as c
import ops.multiplicar as m  # Importar el modulo con (from) luego el nombre del modulo y despues (import) y el nombre del archivo para tener una funcion como si estuviera nativa

if __name__ == "__main__":
    a = 5    # Asignamos un valor a la variable a= 5
    b = 10    # Asignamos un valor a la variable b=10
    print(s.sumar(a,b))   # Imprimo el resultado de mandar a llamar la funcion dada con los parametros asignados arriba
    print(op.restar(a,b))
    print(op.dividir(a,b))
    print(c.cuadrado(a))
    print(multiplicar(a,b))