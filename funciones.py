import os
import time
import msvcrt
trabajadores=[]
def menu():
    os.system("cls")
    print("MENÚ:")
    print("1. Registrar Trabajador.")
    print("2. Listar todos los trabajadores.")
    print("3. Imprimir planilla de sueldos.")
    print("4. Salir del programa.")
def opc_1 ():
    d_salud=0
    d_afp=0
    sueldo_l=0
    print("\t-REGISTRAR TRABAJADOR-")
    nombre=input("Ingrese el nombre del trabajador: ")
    while True:
        cargo=input("Ingrese el cargo del trabajador (CEO, Desarrollador o Analista de datos): ")
        if cargo.upper()=="CEO" or cargo.upper()=="DESARROLLADOR" or cargo.upper()=="ANALISTA DE DATOS":
            break
        else:
            print("ERROR! DEBE INGRESAR 'CEO', 'DESARROLLADOR' O 'ANALISTA DE DATOS'")
            time.sleep(1.5)
    while True:
        try:
            sueldo_b=int(input("Ingrese el sueldo bruto: "))
            if sueldo_b<0:
                print("ERROR! EL SUELDO NO PUEDE SER MENOR A '0'!")
                time.sleep(1.5)
            else:
                break
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            time.sleep(1.5)
    d_salud=sueldo_b*0.07
    d_afp=sueldo_b*0.12
    sueldo_l=sueldo_b-d_salud-d_afp
    trabajador={
        "Trabajador":nombre,
        "Cargo":cargo.upper(),
        "Sueldo Bruto":sueldo_b,
        "Desc. Salud":round(d_salud),
        "Desc. AFP":round(d_afp),
        "Líquido a pagar":round(sueldo_l)
    }
    trabajadores.append(trabajador)
    print("Trabajador agregado con éxito!")
    time.sleep(1.5)
def opc_2 ():
    print("\t-LISTAR TODOS LOS TRABAJADORES-")
    for x in range (len(trabajadores)):
        print(trabajadores[x])
    print("Presione una tecla para continuar.")
    msvcrt.getch()
def opc_3():
    while True:
        print("\t-IMPRIMIR PLANILLA DE SUELDOS-")
        print("MENÚ:")
        print("1. Imprimir todos los sueldos: ")
        print("2. Imprimir los sueldos de un cargo: ")
        opc_2=int(input("Ingrese un número del menú: "))
        if opc_2==1:
            for x in range (len(trabajadores)):
                print(trabajadores[x])
                break
        else:
            print("Ingrese el cargo:")
            print("1. CEO.")
            print("2. Desarrollador.")
            print("3. Analista de datos.")
            opc_3=int(input("Ingrese el número del cargo: "))
            if opc_3==1:
                for x in range(len(trabajadores)):
                    if trabajadores[x]["Cargo"]=="CEO":
                        with open ("Lista sueldos CEO.txt", "w", newline="") as archivo:
                            escritor=archivo.write(str(trabajadores[x]))
            elif opc_3==2:
                for x in range(len(trabajadores)):
                    if trabajadores[x]["Cargo"]=="DESARROLLADOR":
                        with open ("Lista sueldos Desarrollador.txt", "w", newline="") as archivo:
                            escritor=archivo.write(str(trabajadores[x]))
            else:
                for x in range(len(trabajadores)):
                    if trabajadores[x]["Cargo"]=="ANALISTA DE DATOS":
                        with open ("Lista sueldos Analista de datos.txt", "w", newline="") as archivo:
                            escritor=archivo.write(str(trabajadores[x]))
            print("Archivo creado con éxito!")
            time.sleep(1.5)
            break
def opc_4():
    print("Hasta la próxima!")