# h=["Nomre","Est. Dat", "Prog Func", "Ingles"]
# al=["Hugo", "paco", "Luis", "Bob"]
# m1=(9,8,2,1)
# m2=(5,8,3,1)
# m3=(7,5,2,1)

# def reporte(fmt: int):
#     print(f"{h[0]:^{fmt}}{h[1]:^{fmt}}{h[2]:^{fmt}}{h[3]:^{fmt}}")
#     for i in range(len(al)):
#         print(f"{al[i]:*<{fmt}}{m1[i]:^{fmt}}{m2[i]:+>{fmt}}{m3[i]:^{fmt}}")


# if __name__=="__main__":
#     reporte(15)

# numeroBig = 12039292912
# print(f"{numeroBig:,d}")
'''fijar cantidad de decimales'''
# NumeroPI = 3.14159267
# print(f"{NumeroPI:.4f}") 
'''Dependiendo el Numero de la f va redondeando el numero asignado notacion cientifica'''  
# NumeroPI = 3.14159267
# print(f"{NumeroPI:e}")
# print(f"{NumeroPI:.2e}") 
'''Porcentaje'''
# numeroPorciento = 0.3234321
# print(f"{numeroPorciento:%}")
# print(f"{numeroPorciento:.2%}")

'''Numero Binario'''
# print(f"{25:b}")
'''Unicodes'''
# print(f"{65:c}")
'''Hexadecimal'''
# print(f"{255:x}")
'''Octal'''
# print(f"{255:0}")

def tabla(n:int,t:int, fmt: int):
    for i in range(1,n+1):
        print(f"{t:^{fmt}}x{i:^{fmt}}={i*t:^{fmt}}")

if __name__ == "__main__":
    tabla(10,5,6)

def one(n:int,t:int, fmt: int):
    for i in range(1,n+1):
        print(f"{t:^{fmt}}x{i:^{fmt}}={i*t:^{fmt}}")
if __name__ == "__main__":
    one(10,1,6)

def two(n:int,t:int, fmt: int):
    for i in range(1,n+1):
        print(f"{t:^{fmt}}x{i:^{fmt}}={i*t:^{fmt}}")
if __name__ == "__main__":
    two(10,2,6)


