from funciones import *
while True:
    menu()
    opc=int(input("Ingrese el número del menú: "))
    if opc==1:
        opc_1()     
    elif opc==2:
        opc_2()
    elif opc==3:
        opc_3()
    else:
        opc_4()
        break