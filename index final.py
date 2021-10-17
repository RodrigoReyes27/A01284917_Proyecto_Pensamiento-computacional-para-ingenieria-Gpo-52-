from random import randrange
import time

datos_reporte = [0,0,0]
base_datos_preguntas = []
"""
base_datos_preguntas = [
    ["Id: 1","Area: matematicas","Pregunta: 1+1","Opcion A: 1","Opcion B: 2","Opcion C: 3","Opcion D: 4","Respuesta: B"],
    ["Id: 2","Area: matematicas","Pregunta: 2+2","Opcion A: 1","Opcion B: 2","Opcion C: 3","Opcion D: 4","Respuesta: D"],
    ["Id: 3","Area: matematicas","Pregunta: 2+1","Opcion A: 1","Opcion B: 2","Opcion C: 3","Opcion D: 4","Respuesta: C"],
    ["Id: 4","Area: matematicas","Pregunta: 3+1","Opcion A: 4","Opcion B: 5","Opcion C: 6","Opcion D: 7","Respuesta: A"],
    ["Id: 5","Area: matematicas","Pregunta: 4+1","Opcion A: 4","Opcion B: 5","Opcion C: 6","Opcion D: 7","Respuesta: B"],
    ["Id: 6","Area: matematicas","Pregunta: 5+1","Opcion A: 4","Opcion B: 5","Opcion C: 6","Opcion D: 7","Respuesta: C"],
    ["Id: 7","Area: ciencias","Pregunta: fuente de energia de la celula","Opcion A: mitocondria","Opcion B: nucleo","Opcion C: nucleolus","Opcion D: ninguna","Respuesta: A"],
    ["Id: 8","Area: ciencias","Pregunta: elige el halogeno ","Opcion A: Pb","Opcion B: F","Opcion C: C","Opcion D: Mg","Respuesta: B"],
    ["Id: 9","Area: lectura","Pregunta: Algo le ocurrió al personaje de la historia la noche anterior. ¿Qué fue lo que le pasó?","Opcion A: El mal tiempo había estropeado la moto. ","Opcion B: El mal tiempo había impedido salir al personaje. ","Opcion C: El personaje había comprado una moto nueva.","Opcion D: El personaje había tenido un accidente de moto","Respuesta: D"],
    ["Id: 10","Area: matematicas","Pregunta: 2 * 2","Opcion A: 4","Opcion B: 5","Opcion C: 6","Opcion D: 7","Respuesta: A"]
]
"""

def main():
    
    while True:
        opcion = menu()

        opcion_existente = opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6
        nombre_archivo = "preguntas_guardadas.txt" # nombre del archivo de texto

        if opcion_existente != True:
            print("Opcion Incorrecta")
            continue
        elif opcion == 1:
            registrar_preguntas(nombre_archivo)
        elif opcion == 2:
            actualizar_pregunta(nombre_archivo)
        elif opcion == 3:
            estudiar_area(nombre_archivo)
        elif opcion == 4:
            presentar_quiz(nombre_archivo)
        elif opcion == 5:
            reportar_calificaciones()
        elif opcion == 6:
            salir()
            break


def menu():
    # Muestra las opciones y REGRESA la OPCION seleccionada
    print("\n----------------------------------------")
    print("Seleccione una de las siguientes opciones ")
    print("1. Alta de preguntas de prueba PISA")
    print("2. Actualizar preguntas de la prueba PISA")
    print("3. Estudiar preguntas de cierta área")
    print("4. Presentar quiz")
    print("5. Reporte de calificaciones")
    print("6. Salir")

    opcion = int(input("Ingrese el número de la opcion que eligio: "))
    return opcion


def leer_archivo(nombre):
    lista_preguntas = []

    with open(nombre, "r") as archivo:
        contenido = archivo.readlines() # lee todas las líneas del archivo de texto

        for elemento in contenido: # para recorrer cada línea del contenido
            linea = elemento.split(",") # crear una lista con todos los elementos de la línea, cada coma es un elemento
            linea[7] = linea[7][:-1] # borrar la \n del último elemento
            lista_preguntas.append(linea) # agregar la línea (lista) a la lista de preguntas
    
    return lista_preguntas # regresa la lista de preguntas
  

def grabar_archivo(nombre, lista): 

    with open(nombre, "w") as archivo:
        for pregunta in lista: # recorrer pregunta por pregunta la lista de preguntas
            texto = ",".join(pregunta) # crear un texto o string con todos los elementos de la lista, separados por coma
    
            archivo.write(texto + "\n")


def registrar_preguntas(nombre):
    # Añade preguntas a la base de datos
    # INDICES del array de PREGUNTAS
    # 0 ID de la pregunta
    # 1 Area en minuscula
    # 2 Pregunta 
    # 3 OPCION A 
    # 4 OPCION B 
    # 5 OPCION C 
    # 6 OPCION D 
    # 7 Letra de la Respuesta en mayuscula

    # La base_datos_preguntas queda tal que 
        # base_datos_preguntas[numero de pregunta][id = 0 , area = 1, pregunta = 2, opcion a = 3, opcion b = 4, opcion c = 5, opcion d = 6 respuesta = 7]

    base_datos_preguntas = leer_archivo(nombre) # va a leer los datos de las preguntas que hay en el archivo de texto, y los va a almacenar en una lista

    print("\nComplete los siguientes datos para la nueva pregunta\nOpciones para area: lectura, matematicas, ciencias. Favor de no usar tildes")
    id_nuevo = len(base_datos_preguntas) + 1
    pregunta = [
        "Id: " + str(id_nuevo),
        "Area: " + input("Area: ").lower(), 
        "Pregunta: " + input("Pregunta: "), 
        "Opcion A: " + input("Opcion A: "),
        "Opcion B: " + input("Opcion B: "),
        "Opcion C: " + input("Opcion C: "),
        "Opcion D: " + input("Opcion D: "),
        "Respuesta: " + input("Respuesta: ").upper()
    ]

    base_datos_preguntas.append(pregunta) # añadir datos pregunta a la base de datos
    
    print("\nRespuesta registrada correctamente con los siguientes datos:")
    for num in range(len(pregunta)): # imprime los datos de la pregunta recien creada
        print(base_datos_preguntas[id_nuevo -1][num])
    
    grabar_archivo(nombre, base_datos_preguntas) # Llama a la funcion grabar archivo, con parametros (nombre del archivo txt, nombre de la lista)
                                                 # despues de haber cambiado la lista dentro del programa, se manda a actualizar el archivo txt 
                                                 # con la nueva pregunta


def actualizar_pregunta(nombre):
    
    base_datos_preguntas = leer_archivo(nombre) # va a leer los datos de las preguntas que hay en el archivo de texto, y los va a almacenar en una lista

    print("\nSección para actualizar preguntas\nSelecciona una de las siguientes opciones para actualizar: \n")

    for num in range(len(base_datos_preguntas)):
        print(f"{base_datos_preguntas[num][0]} {base_datos_preguntas[num][2]}") # imprime el id y pregunta de todas las preguntas en la base de datos
    
    id_pregunta_actualizar = int(input("\nIngrese el id de la pregunta que desee actualizar: "))

    pregunta_temp = [] # funcionara como la lista pregunta temporal

    if id_pregunta_actualizar <= len(base_datos_preguntas) and id_pregunta_actualizar > 0: # checa que el ID ingresado exista y que no sea 0 o menos
        print("\nDatos pregunta a actualizar: \nSi desea actualizar la pregunta, escriba los nuevos datos, sino solo de enter")
        
        pregunta_temp.append("Id: " + str(id_pregunta_actualizar))

        for num in range(1, len(base_datos_preguntas[id_pregunta_actualizar - 1])): # recorre la lista de la pregunta seleccionada empezando desde 1 (area)
            print(base_datos_preguntas[id_pregunta_actualizar - 1][num]) #imprime la informacion existente

            nuevo_dato_string = base_datos_preguntas[id_pregunta_actualizar - 1][num]
            nuevo_dato_tipo = nuevo_dato_string.split(":") # conseguira el texto id: , area: , pregunta: etc

            dato_temp = input() # recibira el dato a actualizar o el skip

            if(dato_temp != ""): # si SE escribio un nuevo dato se ejecuta
                if nuevo_dato_tipo[0] != "Respuesta": # este if es para el caso de escribir la RESPUESTA CORRECTA
                                                      # porque en el programa se trabaja con que ese valor siempre
                                                      # tiene que ser en letra mayuscula
                    pregunta_temp.append(nuevo_dato_tipo[0] + ": " + str(dato_temp)) # agregara el texto id: , area: + el dato tecleado por el usuario
                else: # Aqui se cambio la letra de la RESPUESTA CORRECTA a Mayuscula
                    pregunta_temp.append(nuevo_dato_tipo[0] + ": " + str(dato_temp).upper()) # agregara el texto id: , area: + el dato tecleado por el usuario

            else: # si NO se escribio nuevo dato se ejecuta
                pregunta_temp.append(base_datos_preguntas[id_pregunta_actualizar - 1][num]) # agregara el dato existente

        print(f"\nLos nuevos datos de la pregunta id {id_pregunta_actualizar} son: ")
        for num in range(1, len(pregunta_temp)): # imprimira los nuevos datos de la pregunta
            print(pregunta_temp[num])

        while True: # ciclo para elegir si actualizar la pregunta 
            seleccion_ingresar = input("Esta seguro de querer actualizar esta pregunta? y/n ").lower()
            seleccion_existente = seleccion_ingresar == "y" or seleccion_ingresar == "n"

            if seleccion_existente == True: # checa si la opcion ingresada es valida

                if seleccion_ingresar == "y":
                    base_datos_preguntas[id_pregunta_actualizar - 1] = pregunta_temp # actualiza la pregunta con respecto a su id en la lista con 
                                                                                     # todas las preguntas

                    grabar_archivo(nombre, base_datos_preguntas)# Llama a la funcion grabar archivo, con parametros (nombre del archivo txt)
                                                                # (nombre de la lista) 
                                                                # despues de haber cambiado la lista dentro del programa, se manda a actualizar el archivo txt con los nuevos valores
                    print("Pregunta actualizada exitosamente")
                    break
                else:
                    print("Los cambios no fueron guardados")
                    break   

            else:
                print("Ingrese una opcion existente")
                continue
        

    else:
        print("\nNo existe ninguna pregunta con ese id")


def estudiar_area(nombre):
    print("\nEstudiar area")

    base_datos_preguntas = leer_archivo(nombre) # va a leer los datos de las preguntas que hay en el archivo de texto, y los va a almacenar en una lista
    while True:

        print("----------------------------------------")
        print("Ingrese el número del area que desee estudiar:")
        print("1. Lectura")
        print("2. Matemáticas")
        print("3. Ciencias")
        
        area_presentar = int(input("Número de área: "))
        num_preguntas_practicar = int(input("Escriba el número de preguntas que quiere estudiar de esta area: "))
        num_lectura = 0
        num_mate = 0
        num_ciencia = 0
        
        area_presentar_existente = area_presentar == 1 or area_presentar == 2 or area_presentar == 3
        
        for num in range(0, len(base_datos_preguntas)): #contar cuantas preguntas tiene cada area
            if base_datos_preguntas[num][1] == "Area: lectura":
                num_lectura += 1
            elif base_datos_preguntas[num][1] == "Area: matematicas":
                num_mate += 1
            elif base_datos_preguntas[num][1] == "Area: ciencias":
                num_ciencia += 1

        # Esta SECCION de IF y ELIF, eligen el AREA de donde agarrar las preguntas
        if area_presentar_existente != True:
            print("\nOpcion invalida")
            continue

        elif area_presentar == 1:
            print("\nArea lectura")

            if num_preguntas_practicar > num_lectura:
                print(f"Lo sentimos pero no tenemos esa cantidad de preguntas para esta area, por lo que se usaran el maximo que tenemos: {num_lectura}")
                correctas = mostrar_preguntas("Area: lectura", num_lectura, base_datos_preguntas)
                
            else:
                correctas = mostrar_preguntas("Area: lectura", num_preguntas_practicar, base_datos_preguntas)

            break

        elif area_presentar == 2:
            print("\nOpcion matematicas")

            if num_preguntas_practicar > num_mate:
                print(f"Lo sentimos pero no tenemos esa cantidad de preguntas para esta area, por lo que se usaran el maximo que tenemos: {num_mate}")
                correctas = mostrar_preguntas("Area: matematicas", num_mate,base_datos_preguntas)
                
            else:
                correctas = mostrar_preguntas("Area: matematicas", num_preguntas_practicar,base_datos_preguntas)

            break

        elif area_presentar == 3:
            print("\nOpcion ciencias")

            if num_preguntas_practicar > num_ciencia:
                print(f"Lo sentimos pero no tenemos esa cantidad de preguntas para esta area, por lo que se usaran el maximo que tenemos: {num_ciencia}")
                correctas = mostrar_preguntas("Area: ciencias", num_ciencia,base_datos_preguntas)
                
            else:
                correctas = mostrar_preguntas("Area: ciencias", num_preguntas_practicar,base_datos_preguntas)

            break


def presentar_quiz(nombre):
    print("\nPresentar quiz\nPara este quiz tendra 20 minutos, despues de eso aunque ingrese la repuesta, esta no se guardara\n")
    
    correctas = 0
    contador_preguntas = 1
    lista_rand_num = []
    timeout = time.time() + 60*1   # hora actual + 20 minutos
    base_datos_preguntas = leer_archivo(nombre) # va a leer los datos de las preguntas que hay en el archivo de texto, y los va a almacenar en una lista

    while True:
    
        if contador_preguntas == 10 + 1:
            break
        elif time.time() > timeout:
            break
        else:
            rand_num = randrange(0, len(base_datos_preguntas)) # genera un numero random ente 0 y la longitud de la base de datos de preguntas

            # este ciclo while sirve para checar que no se repitan preguntas
            while True:
                if rand_num not in lista_rand_num: # si rand_num no esta en la lista de numeros random ya generados se rompe el ciclo
                    break
                                
                else: # si rand_num  esta en la lista de numeros random ya generados se genera otro rand_num y se continua el ciclo
                    rand_num = randrange(0, len(base_datos_preguntas))
                    continue    

            print("Numero " + str(contador_preguntas)) # incrementa el numero de la pregunta
            for num_dato in range(2, len(base_datos_preguntas[rand_num]) - 1): # imprimira los  datos de la pregunta
                print(base_datos_preguntas[rand_num][num_dato])

            opcion_seleccionda = "Respuesta: " + input("Ingrese la letra de la opción de la respuesta: ").upper()

            if (opcion_seleccionda == base_datos_preguntas[rand_num][7]):
                print("\nCorrecto!!\n")

                if time.time() > timeout:
                    print("Esta respuesta no fue guardada, porque se excedio de tiempo")
                else:
                    correctas += 1
            else:
                print("\nIncorrecto!!\n")

                if time.time() > timeout:
                    print("Esta respuesta no fue guardada, porque se excedio de tiempo")
                else:
                    pass
                                    
            contador_preguntas += 1
            lista_rand_num.append(rand_num)

    print("Examen Finalizado \nPreguntas Correctas:", correctas, "de 10")

    # añadir datos para reporte de calificaciones
    datos_reporte_temp = []
    datos_reporte_temp.append(datos_reporte[0] + 1)
    datos_reporte_temp.append(datos_reporte[1] + correctas)
    datos_reporte_temp.append(datos_reporte[2] + (10 - correctas))

    for num in range(0, 3):
        datos_reporte[num] = datos_reporte_temp[num]


def reportar_calificaciones():
    print("\nReportar calificaciones")
    usuarios = datos_reporte[0]
    correctas = datos_reporte[1]
    incorrectas = datos_reporte[2]

    if usuarios >= 1:
        promedio_calif =  int((correctas / (correctas + incorrectas)) * 100)
        print(f'{"Total de usuarios":<30}{usuarios}\n{"Promedio de calificaciones":<30}{promedio_calif}%\n{"Respuestas correctas":<30}{correctas}\n{"Respuestas incorrectas":<30}{incorrectas}')
    else:
        print("No se pueden mostrar datos de calificaciones, porque aun no hay datos")

def salir():
    print("\nSalir\nGracias por usar el programa. Que tenga buen dia")
    

def mostrar_preguntas(area, cant_preguntas, lista_preguntas):
    correctas = 0
    contador_preguntas = 1
    preguntas_area = []
    id_pregunta_temp = 0
    lista_rand_num = []

    # con este loop se crea una lista temporal solo con las preguntas del area seleccionada
    for num in range(0, len(lista_preguntas)):
    # Este loop recorre todas las preguntas
        
        pregunta_temp = []
        if lista_preguntas[num][1] == area:
            # Cuando el loop recorre todas las preguntas ESTE IF, se ejecuta cuando el AREA es la seleccionada

            pregunta_temp.append("id: " + str(id_pregunta_temp)) # le agrega el id empezando de 0
            for num_dato in range(1, len(lista_preguntas[num])): # guarda los valores de la pregunta en una lista temporal
                pregunta_temp.append(lista_preguntas[num][num_dato])
                    
            preguntas_area.append(pregunta_temp) # añade la pregunta temporal(lista) a una lista con varias preguntas de esa area
            id_pregunta_temp += 1
    
    
    for num in range(0, cant_preguntas): # se corre la cantidad de veces que el usuario ingreso
        rand_num = randrange(0, len(preguntas_area)) # genera un numero random ente 0 y la longitud de la lista que contiene preguntas del area seleccionada

        # este ciclo while sirve para checar que no se repitan preguntas
        while True:
            if rand_num not in lista_rand_num: # si rand_num no esta en la lista de numeros random ya generados se rompe el ciclo
                break
                
            else: # si rand_num  esta en la lista de numeros random ya generados se genera otro rand_num y se continua el ciclo
                rand_num = randrange(0, len(preguntas_area))
                continue    

        print("Numero " + str(contador_preguntas)) # incrementa el numero de la pregunta
        for num_dato in range(2, len(preguntas_area[rand_num]) - 1): # imprimira los  datos de la pregunta
            print(preguntas_area[rand_num][num_dato])

        opcion_seleccionda = "Respuesta: " + input("Ingrese la letra de la opción de la respuesta: ").upper()

        if (opcion_seleccionda == preguntas_area[rand_num][7]):
            print("\nCorrecto!!\n")
            correctas += 1
        else:
            print("\nIncorrecto!!\n")
                    
        contador_preguntas += 1
        lista_rand_num.append(rand_num)

    print("Practica Finalizada \nPreguntas Correctas:", correctas, "de", cant_preguntas)
    return correctas
    
main()