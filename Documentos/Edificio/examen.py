import os
import numpy as np
import time
from datetime import date
import funciones_examen as fe

# ----Variables----

rut=np.empty(40,dtype=int)
nombre=np.empty(40,dtype=object)
a=np.empty(10,dtype=object)
b=np.empty(10,dtype=object)
c=np.empty(10,dtype=object)
d=np.empty(10,dtype=object)
valor_departamentoa=0
valor_departamentob=0
valor_departamentoc=0
valor_departamentod=0
contador_cant=0
opcion_menu=0 
fila=0
columna=""
acum_subtotal=0
nombre1=""
rut1=0
rut2=[]
cantidad_a=0
cantidad_b=0
cantidad_c=0
cantidad_d=0
cantidad_total=0
total_a=0
total_b=0
total_c=0
total_d=0
total_ganancias=0

for k in range (0,10):
    a[k]="D"
    b[k]="D"
    c[k]="D"
    d[k]="D"

# ----Codigo----
while True:
    os.system("cls")
    print('''
    -------------Bienvenidos a Casa Feliz-------------
    
    1. Comprar departamento
    2. Mostrar departamentos disponibles
    3. Ver listado de compradores
    4. Mostrar ganancias totales
    5. Salir''')
    opcion_menu=int(input('''
    Ingrese opción: '''))
    while  opcion_menu!=1 and opcion_menu!=2 and opcion_menu!=3 and opcion_menu!=4 and opcion_menu!=5:
       opcion_menu=int(input('''
    Ingrese opción: '''))

    if opcion_menu==1:
        os.system("cls")
        print("\n------------Comprar departamento------------")
        fe.imprimir_departamentos(a,b,c,d)
        fe.imprimir_precio()
        os.system("pause")
        os.system("cls")
        
        rut1=int(input("Ingrese rut del pasajero: "))
        
        nombre1=str(input("Ingrese nombre del pasajero: ")).strip().capitalize()
          
        fila=int(input("Ingrese piso(1 al 10): "))
        while fila<0 or fila>10:
            fila=int(input("Ingrese piso(1 al 10): "))

        columna=input("Ingrese tipo de departamento(a-b-c-d): ").lower()
        while columna!="a" and columna!="b" and columna!="c" and columna!="d":
            columna=input("Ingrese tipo de departamento(a-b-c-d): ").lower()
        
        if columna=="a":
            for k in range (0,10):
                if k==fila-1:
                    if a[k]=="D":
                        a[k]="X"
                        rut[k]=rut1
                        nombre[k]=nombre1
                        rut2.append(rut1)
                        valor_departamentoa=3800 
                        cantidad_a+=1
                        print("Departamento comprado") 
                    else:
                        print("No esta disponible")
                        break  
            os.system("pause")
        
        if columna=="b":
            for k in range (0,10):
                if k==fila-1:
                    if b[k]=="D":
                        b[k]="X"
                        rut[k+10]=rut1
                        nombre[k+10]=nombre1
                        rut2.append(rut1)
                        valor_departamentob=3000
                        cantidad_b+=1
                        print("Departamento comprado") 
                    else:
                        print("No esta disponible")
                        break  
            os.system("pause")
        
        if columna=="c":
            for k in range (0,10):
                if k==fila-1:
                    if c[k]=="D":
                        c[k]="X"
                        rut[k+20]=rut1
                        nombre[k+20]=nombre1
                        rut2.append(rut1)
                        valor_departamentoc=2800
                        cantidad_c+=1
                        print("Departamento comprado") 
                    else:
                        print("No esta disponible")
                        break   
            os.system("pause")

        if columna=="d":
            for k in range (0,10):
                if k==fila-1:
                    if d[k]=="D":
                        d[k]="X"
                        rut[k+30]=rut1
                        nombre[k+30]=nombre1
                        rut2.append(rut1)
                        valor_departamentod=3500
                        cantidad_d+=1
                        print("Departamento comprado") 
                    else:
                        print("No esta disponible")
                        break    
            os.system("pause")

        cantidad_total= cantidad_a + cantidad_b + cantidad_c + cantidad_d
        
        total_a=valor_departamentoa*cantidad_a
        total_b=valor_departamentob*cantidad_b
        total_c=valor_departamentoc*cantidad_c
        total_d=valor_departamentod*cantidad_d

        total_ganancias = total_a + total_b + total_c + total_d     

    if opcion_menu==2:
        os.system("cls")
        print("\n--------Mostrar departamentos disponibles--------")
        fe.imprimir_departamentos(a,b,c,d)
        os.system("pause")
        
    if opcion_menu==3:
        os.system("cls")
        print("\n------------Ver listado de compradores------------")
        rut2.sort()
        for k in range (len(rut2)):
            print(f'''
    {rut2[k]}
    ''')
        os.system("pause")

    if opcion_menu==4:
        os.system("cls")
        print("\n------------Mostrar ganancias totales------------")
        print(f'''

    |Tipo de Departamento |Cantidad  |Total   
    |Tipo A 3.800 UF      |{cantidad_a}         |{total_a}    
    |Tipo B 3.000 UF      |{cantidad_b}         |{total_b}    
    |Tipo C 2.800 UF      |{cantidad_c}         |{total_c}    
    |Tipo D 3.500 UF      |{cantidad_d}         |{total_d}     
    |TOTAL                |{cantidad_total}         |{total_ganancias}     
    ''')

        os.system("pause")

    
    if opcion_menu==5:
        now = date.today()
        print(f'''
    Tomás Encina
    {now}
    Cerrando Sesión  
    ''')
        time.sleep(3)
        break