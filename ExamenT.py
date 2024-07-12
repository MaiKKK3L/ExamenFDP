import random
import csv
trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
sueldo_trabajadores=['Nombre','Sueldo']
sueldo=100
sueldos=[]
sueldoB=[]
sueldoM=[]
sueldoA=[]
        

lista_de_estadisticas = """
1. Sueldos Bajos
2. Sueldos Promedios
3. Sueldos Altos
"""
    

def asignar_sueldo(trabajadores):
    for i in range(len(trabajadores)):
        sueldo=sueldo.randint(300000, 2500000)
        sueldo_trabajadores[trabajadores[i]] = sueldos
        sueldo=sueldos.append
        sorted(sueldos)
        


def clasificar_sueldo(trabajadores):
    if sueldo <800000:
        print("Su sueldo es bajo")
        sueldoB.append
    elif sueldo <=2000000:
        print("Su sueldo está dentro del promedio")
        sueldoM.append
    else:
        print("Su sueldo es alto")
        sueldoA.append
        
def salir_del_programa():
    pass

while True:
    print('''
        1. Asignar sueldos aleatorios
        2. Clasificar sueldos
        3. Ver Estadisticas
        4. Reporte de sueldos
        5. Salir del programa

        ''')
    opc=int(input("Elija una opción: "))

    if opc ==1: 
        asignar_sueldo(trabajadores)
    elif opc ==2:
        clasificar_sueldo(trabajadores)
    elif opc ==5:
        salir_del_programa()
        break
## Me faltaron 2 funciones, la de ver estadisticas y la de el reporte de sueldos ##