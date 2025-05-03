import os


def menu():
    error=0
    opcion=1
    #carreras diurnas
    listaDSd=[]
    listaLd=[]
    listaEd=[]
    listaCed=[]
    #carreras nocturnas
    listaDSn=[]
    listaLn=[]
    listaEn=[]
    listaCen=[]
    fil=0 #desarrollo diurno
    fil2=0 #desarrollo nocturno
    fil3=0 #electronica diurno
    fil4=0 #electronica nocturno
    fil5=0 #logistica diurno
    fil6=0 #logistica nocturno
    fil7=0 #comercio diurno
    fil8=0 #comercio nocturno
    os.system('cls')
    while opcion!=0:
        print("---Bienvido al programa de asistencia---\n services asistant AL")
        opcion=int(input("que opcion desea elegir: \n (0)-cerrar programa \n (1)-realizar asistencia\n (2)-administrador\n"))
    
        if opcion==1:
            os.system('cls')
            carrera= int(input("seleccion su carrera:\n 1- Desarrollo de software \n 2- Electronica\n 3- Logistica \n 4- Comercio Exterior\n "))
            if carrera== 1:
                os.system('cls')
                horario=int(input("cual horario pertence:\n 1- diurno \n 2- nocturno\n"))

                if horario==1:
                    os.system('cls')
                    listaDSd.append([])
                    nombred=input("ingrese el nombre completo\n").upper()
                    listaDSd[fil].append("Nombre:"+ nombred)
                    codigod=input("ingrese el codigo de estudiante\n")
                    listaDSd[fil].append("Codigo: "+codigod)
                    fil= fil+1
                elif horario==2:
                    os.system('cls')
                    listaDSn.append([])
                    nombre=input("ingrese el nombre completo\n").upper()
                    listaDSn[fil2].append("Nombre: "+ nombre)
                    codigo=input("ingrese el codigo de estudiante\n")
                    listaDSn[fil2].append("Codigo: "+ codigo)
                    fil2= fil2 + 1
            if carrera== 2:
                horario=int(input("cual horario pertence:\n 1- diurno \n 2- nocturno\n"))

                if horario==1:
                    os.system('cls')
                    listaEd.append([])
                    nombred=input("ingrese el nombre completo\n").upper()
                    listaEd[fil3].append("Nombre: "+ nombred)
                    codigod=input("ingrese el codigo de estudiante\n")
                    listaEd[fil3].append("Codigo: "+ codigod)
                    fil3= fil3+1
                elif horario==2:
                    os.system('cls')
                    listaEn.append([])
                    nombre=input("ingrese el nombre completo\n").upper()
                    listaEn[fil4].append("Nombre:"+ nombre)
                    codigo=input("ingrese el codigo de estudiante\n")
                    listaEn[fil4].append("Codigo: "+ codigo)
                    fil4= fil4 + 1
            if carrera== 3:
                horario=int(input("cual horario pertence:\n 1- diurno \n 2- nocturno\n"))

                if horario==1:
                    os.system('cls')
                    listaLd.append([])
                    nombred=input("ingrese el nombre completo\n").upper()
                    listaLd[fil5].append("Nombre: "+ nombred)
                    codigod=input("ingrese el codigo de estudiante\n")
                    listaLd[fil5].append("Codigo: "+ codigod)
                    fil5= fil5+1
                elif horario==2:
                    os.system('cls')
                    listaLn.append([])
                    nombre=input("ingrese el nombre completo\n").upper()
                    listaLn[fil6].append("Nombre: "+ nombre)
                    codigo=input("ingrese el codigo de estudiante\n")
                    listaLn[fil6].append("Codigo: "+ codigo)
                    fil6= fil6 + 1
            if carrera== 4:
                horario=int(input("cual horario pertence:\n 1- diurno \n 2- nocturno\n"))

                if horario==1:
                    os.system('cls')
                    listaCed.append([])
                    nombred=input("ingrese el nombre completo\n").upper()
                    listaCed[fil7].append("nombre: "+ nombred)
                    codigod=input("ingrese el codigo de estudiante\n")
                    listaCed[fil7].append("codigo: "+ codigod)
                    fil7= fil7+1
                elif horario==2:
                    os.system('cls')
                    listaCen.append([])
                    nombre=input("ingrese el nombre completo\n").upper()
                    listaCen[fil8].append("nombre: "+ nombre)
                    codigo=input("ingrese el codigo de estudiante\n")
                    listaCen[fil8].append("codigo: "+ codigo)
                    fil8= fil8 + 1
        elif opcion==2:
              inicionSesion(listaDSd,listaEd,listaLd,listaCed,listaDSn,listaEn,listaLn,listaCen)
    print("---hasta pronto, fin del programa---")
    return error 
    
def inicionSesion(listaDSd,listaEd,listaLd,listaCed,listaDSn,listaEn,listaLn,listaCen):
    
    opcion=1
    error=0
    while opcion!=0:
        os.system('cls')
        opcion=int(input("1 para continuar, 0 para salir: "))
        usuario="alexis"
        Contrasena="12345"
        USUARIO=input("ingrese el usuario: ")
        if USUARIO==usuario:
            Pass=input("ingrese contraseña: ")
            if Pass==Contrasena:
                os.system('cls')
                print(adminOp(listaDSd,listaEd,listaLd,listaCed,listaDSn,listaEn,listaLn,listaCen))
            else:
                print("contraseña incorrecta")
        else:
            print("usuario incorrecto")
        
        return error

           
def adminOp(listaDSd,listaEd,listaLd,listaCed,listaDSn,listaEn,listaLn,listaCen):
    adminO=1
    while adminO!=0:
        adminO=int(input("bienvenido administrador, ¿que opcion desea?\n 1- mostrar listado diurno\n 2- mostrar listado nocturno\n 3- volver a menu\n"))
        if adminO==1:
            os.system('cls')
            carrera=int(input("selecciona la carrera:\n 1- Desarrollo de software \n 2- Electronica\n 3- Logistica \n 4- Comercio Exterior\n "))
            if carrera==1:
                print("la lista de estudiantes es: ")
                for element in listaDSd:
                        print(f'''
 ------------                       {element[0]}--------{element[1]}''')
                n1=(len(listaDSd))
                print("cantidad de alumnos: ",n1)

            elif carrera==2:
                for element in listaEd:
                        print(f'''
------------                       {element[0]}--------{element[1]}''')
                n2=(len(listaEd))
                print("cantidad de alumnos: ",n2)
            elif carrera==3:
                for element in listaLd:
                        print(f'''
------------                        {element[0]}-------{element[1]}''')
                n3=(len(listaLd))
                print("cantidad de alumnos: ",n3)
            elif carrera==4:
                for element in listaCed:
                        print(f'''
-------------                       {element[0]}------{element[1]}''')
                n4=((len(listaCed)))
                print("cantidad de alumnos: ",n4)
        elif adminO==2:
            carrera=int(input("selecciona la carrera:\n 1- Desarrollo de software \n 2- Electronica\n 3- Logistica \n 4- Comercio Exterior\n "))
            if carrera==1:
                os.system('cls')
                print("la lista de estudiantes es: ")
                for element in listaDSn:
                    print(f'''
------------                        {element[0]}-------{element[1]}''')
                n5=print(len(listaDSn))
                print("cantidad de alumnos: ",n5)
            elif carrera==2:
                for element in listaEn:
                        print(f'''
-------------                       {element[0]}-------{element[1]}''')
                n6=(len(listaEn))
                print("cantidad de alumnos: ",n6)
            elif carrera==3:
                for element in listaLn:
                        print(f'''
------------                        {element[0]}--------{element[1]}''')
                n7=(len(listaLn))
                print("cantidad de alumnos: ",n7)
            elif carrera==4:
                for element in listaCen:
                        print(f'''
-------------                       {element[0]}--------{element[1]}''')
                n8=(len(listaCen))
                print("cantidad de alumnos: ",n8)
        elif adminO==3:
            menu()
menu()


                
