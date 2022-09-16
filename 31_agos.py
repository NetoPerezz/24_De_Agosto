n1=10
msg="Hola"
print(n1,msg)
print(str(n1)+msg)
#fstrings
print(f"{n1} {msg}")
'''Hacer una funcion que reciba el nombre de una persona , el año de nacimiento y el año actual
retonarno el mensaje "Hola <nombre>, tienes <edad> años" '''

# def mensaje1(name:str, a_nacim:int, a_actual:int)->str:
#     edad= a_actual - a_nacim
#     return f"Hola {name}, tienes {edad} años"

# def mensaje2(name:str, a_nacim:int, a_actual:int)->str:
#     return f"Hola{name}, tienes {a_actual - a_nacim} años"

# def calcular_edad(name:str, a_nacim:int, a_actual:int)->str:
#     return a_actual - a_nacim

# def mensaje3(name:str, a_nacim:int, a_actual:int)->str:
#     return f"Hola"

# if __name__ == "__main__":
#     print(mensaje1("Ernesto",2000,2022))
#     res=mensaje1("Alex",1999,2022)
#     print(res)
#     print(mensaje2("Luis",2001,2030))

#Listas
alumnos=["Hugo", "paco", "Luis"]
print(f"Alumnos: {alumnos}")
for i in range(len(alumnos)):
    print(f"Alumnos: {alumnos[i]}")
    '''La forma de acceder '''
#tuplas
'''Son estructuras ejecutables'''
# alumnos=("Hugo", "paco", "Luis")
# print(f"Alumnos: {alumnos}")
# for i in range(len(alumnos)):
#     print(f"Alumnos {i+1}: {alumnos[i]}")

#Sets
#alumnos={"Hugo", "paco", "Luis"}
#print(f"Alumnos: {alumnos}")

#Diccionarios
'''Estructura llave valor que tiene 2 elementos, accede a cada uno de los elementos o variabels'''
#alumnos={"nombre": "Hugo", "Materia1":10, "Materia2":5}
#print(f"Alumnos: {alumnos}")
#print(f"Alumnos: {alumnos['nombre']}")

'''las listas se pueden repetir los valores y los sets no'''

# numeros_list=[1,2,3,4,5,6,7,8,9,12,2,2,2,1]
# numeros_set={1,2,3,4,5,6,7,8,9,12,2,2,2,1}
# print(numeros_list)
# print(numeros_set)

e=["Nomre","Est. Dat", "Prog Func", "Ingles"]
alumnos=["Hugo", "paco", "Luis", "Bob"]
m_e_d=(9,8,2,1)
m_p_f=(5,8,3,1)
m_i=(7,5,2,1)
print(f"{e[0]}{e[1]}{e[2]}{e[3]:>10}")
for i in range(len(alumnos)):
    print(f"{alumnos[i]:^10}{m_e_d[i]:^10}{m_p_f[i]:^10}")