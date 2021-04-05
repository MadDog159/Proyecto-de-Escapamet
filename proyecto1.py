from jugadores import Jugador
from jugadores import puntuaciones
import json
import time
import os
import tkinter as tk
import datetime as dt
import Habitaciones
import random
import minijuegos
import sys
import temporizador
import requests
from cuartos import cuartos
import datetime
import pygame

pygame.init()
pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound("TheFatRat-Xenogenesis.wav")
pygame.mixer.Sound.play(sonido_fondo,-1)

def extraccion_API():
    res = requests.get('https://api-escapamet.vercel.app/')
    son = res.json()
    with open('API.json') as file:
        data = json.load(file)
        data1 = son
        with open('API.json', 'w') as file:
            json.dump(data1, file, indent=4)


def menu():
    print("""
    Bienvenido al ESCAPEMET de Gabriel Useche

    1.Iniciar Juego
    2.Instrucciones del juego
    3.Records de partidas
    4.Salir
    """)

def verificar():
    if os.path.isfile('data.json'):
        return True
    else:
        data = {}
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
    if os.path.isfile('status.json'):
        return True
    else:
        data = {}
        with open('status.json', 'w') as file:
            json.dump(data, file, indent=4)
    if os.path.isfile('records.json'):
        return True
    else:
        data = {}
        with open('records.json', 'w') as file:
            json.dump(data, file, indent=4)

def primera_narrativa(tiempo, personaje ):
    print("""
    Hoy en dia, la Universidad sigue en cuarentena (esto no es novedad), lo que sí es novedad es que se robaron un Disco Duro
    de la Universidad del cuarto de redes que tiene toda la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos
    que nos ayudes a recuperar el disco, para eso tienes", tiempo,"minutos, y solo se encuentra", personaje," para
    resolverlo antes de que el servidor se caiga y no se pueda hacer más nada.
    """)

def Segunda_Narrativa(usuario):
    print("""
    Bienvenido", usuario," gracias por tu disposición a ayudarnos a resolver este inconveniente, te encuentras actualmente
    ubicado en la biblioteca, revisa el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo corre más
    rápido que un trimestre en este reto.""")

def Narrativa_Final(usuario):
    print("""
    ¡Felicidades! Has logrado evitar una catástrofe en la Unimet, entonces, ya te puedes relaja tomar un cafecito, ver si quedaste entre los
    TOP 5!! revisa los records de los jugadores,  BIEN HECHO!!
    """)


def administrador(data):
    open('data.json') 
    data['admin'].append({
        'password': 27770633})
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)



def Base_datos(usuarios):
    entro = False
    with open('data.json') as file:
        data = json.load(file)
        data1 = {}
        with open('data.json', 'w') as file:
            json.dump(data1, file, indent=4)

        if len(data) < 1:
            
            data = {"usuarios":[]}
            entro =True
        data['usuarios'].append({
            'nombre': usuarios.usuario,
            'edad': usuarios.edad,
            'password': usuarios.password})
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        
    with open('status.json') as file:
        data = json.load(file)
        data1 = {}
        with open('status.json', 'w') as file:
            json.dump(data1, file, indent=4)
            usu = usuarios.usuario
        if entro:    
            data = {}
        data2 ={usu:[]}
        data.update(data2)
        data[usu].append({
            'inventario': [],
            'Biblioteca_left': "0",
            'Biblioteca_center': "0",
            'Biblioteca_right': "0",
            'Plaza Rectorado_left':'0',
            'Plaza Rectorado_center':'0',
            'Plaza Rectorado_right':'0',
            'Pasillo Laboratorios _center':'0',
            'Laboratorio SL001_left': '0',
            'Laboratorio SL001_center': '0',
            'Laboratorio SL001_right': '0',
            'Cuarto de Servidores _left':'0',
            'Cuarto de Servidores _center':'0',
            'Cuarto de Servidores _right':'0',
            'ahorcado_pista1': "0",
            'ahorcado_pista2': "0",
            'ahorcado_pista3': "0",
            'Quizizz_Cultura_Unimetana_pista1':"0",
            'Quizizz_Cultura_Unimetana_pista2':"0",
            'Quizizz_Cultura_Unimetana_pista3':"0",
            'memoria_con_emojis_pista1':"0",
            "Adivinanzas_pista1":"0",
            "Adivinanzas_pista2":"0",
            "Adivinanzas_pista3":"0",
            "preguntas_pista1":"0",
            "preguntas_pista2":"0",
            "escoge_un_numero_entre_pista1":"0",
            "contador_Biblioteca":"0",
            "contador_Plaza Rectorado":"0",
            "contador_Cuarto de Servidores ":"0",
            "contador_Laboratorio SL001":"0",
            "contador_Pasillo Laboratorios ":"0",
            "contador_Puerta_Laboratorio":"0",
            "sopa_letras_pista1":"0",
            "sopa_letras_pista2":"0",
            "sopa_letras_pista3":"0"
            })
        with open('status.json', 'w') as file:
            json.dump(data, file, indent=4)

def desicion_SN(pregunta):
    ciclo = True
    salir = False
    while ciclo:
        respuesta = input(f"{pregunta} S/N: ").lower()
        if respuesta == "s":
            salir = True
            ciclo = False
        elif respuesta == "n":
            ciclo = False
        else:
            print("Respuesta incorrecta")
    return salir
    
def desicion3(variable):
        if variable == "1" :
            return "Facil"
        elif variable == "2":
            return "Normal"
        elif variable== "3":
            return "Dificil"
        else:
            return False

def partida(self):
    if self == 'Facil':
        return 1
    elif self == 'Normal':
        return 2
    elif self == 'Dificil':
        return 3
    else:
        return False

def personajes():
    print(
    """
    1.PapiCharifker
    2.Enugenio Mendoza
    3.LeopoldoPreso
    4.El Chavista
    5.El Veneco
    6.El frikki del LOl
    7.Yo mismo porque soy arrecho
    """)

def seleccion_personaje(personaje):
    if personaje == "1":
        return "PapiCharifker"
    elif personaje == "2":
        return "Enugenio Mendoza"
    elif personaje == "3":
        return "LeopoldoPreso"
    elif personaje == "4":
        return "El Chavista"
    elif personaje == "5":
        return "El Veneco"
    elif personaje == "6":
        return "El frikki del LOl"
    elif personaje == "7":
        return "Yo mismo porque soy arrecho"


def validacion_juego(cuarto, lado,usuario, tiempo_partida, rooms):
   
    x = temporizador.tiempo.hora_actual()
    y = tiempo_partida
    if x >= y:
        print("Mala suerte se te acabo el tiempo XD, intentalo de nuevo")
        return main()
    entrar = True
    with open('status.json','r') as file:
        data = json.load(file)
        for nombre in data[usuario]:
            if lado == "":
                entrar = False
            elif nombre[cuarto+"_"+lado] == "1":
                print("Ya completo este nivel")
                entrar = False
                return False
    if entrar:
        rooms.cuarto_regla(lado)
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                actividad = juegos['name']
                preguntas = juegos['questions']
        respuesta = desicion_SN("Deseas intentarlo: ")
        if respuesta:
            if actividad == "ahorcado":
                minijuegos.minijuegos.ahorcado(rooms,preguntas,lado,usuario)
            elif actividad == "Adivinanzas":
                minijuegos.minijuegos.adivinanzas(rooms,preguntas,lado,usuario)
            elif actividad == "Preguntas sobre python":
                minijuegos.minijuegos.preguntas(rooms,preguntas,lado,usuario)
            elif actividad == "escoge un número entre":
                minijuegos.minijuegos.escoge_un_numero_entre(rooms,preguntas,lado,usuario)
            elif actividad == "Palabra mezclada":
                minijuegos.minijuegos.Palabra_mezclada(rooms,preguntas,lado,usuario)
            elif actividad == "Preguntas matemáticas":
                minijuegos.minijuegos.Preguntas_matematicas(rooms,preguntas,lado,usuario)
            elif actividad == "Criptograma":
                minijuegos.minijuegos.Criptograma(rooms,preguntas,lado,usuario)
            elif actividad == "memoria con emojis":
                minijuegos.minijuegos.memoria(rooms,preguntas,lado,usuario)
            elif actividad == "Quizizz Cultura Unimetana":
                minijuegos.minijuegos.Quizizz_Cultura_Unimetana(rooms,preguntas,lado,usuario)
            elif actividad == "Encuentra la lógica y resuelve":
                minijuegos.minijuegos.Encuentra_la_lógica_y_resuelve(rooms,preguntas,lado,usuario)
            elif actividad == "Lógica Booleana":
                minijuegos.minijuegos.Lógica_Booleana(rooms,preguntas,lado,usuario)
            elif actividad == "Juego Libre":
                minijuegos.minijuegos.Pipes(rooms,preguntas,lado,usuario)
            elif actividad == "sopa_letras":
                minijuegos.minijuegos.sopa_letras(rooms,preguntas,lado,usuario)
            else:
                return validacion_juego(cuarto, lado,usuario,tiempo_partida,rooms)

def guardar_tiempo(usuario,z):
    with open('status.json') as file:
        data = json.load(file)
        for nombre in data[usuario]:
            nombre['tiempo']= z
        with open('status.json', 'w') as file:
            json.dump(data, file, indent=4)

def guardar_contador(cuarto,player):
    with open('status.json') as file:
        data = json.load(file)
        for nombre in data[player.usuario]:
            n=int(nombre['contador_'+cuarto])
            n+=1
            nombre['contador_'+cuarto]= n
            break
        with open('status.json', 'w') as file:
            json.dump(data, file, indent=4)

def inventario(usuario,tiempo_partida,registro):
    x = temporizador.tiempo.hora_actual()
    y = tiempo_partida
    z = y - x
    if x >= y:
        print("Mala suerte se te acabo el tiempo XD, intentalo de nuevo")
        puntuaciones.Base_datos_records(registro)
        return main()

    with open('status.json', 'r') as file:
        data = json.load(file)
        for nombre in data[usuario]:
            x = temporizador.tiempo.hora_actual()
            y = tiempo_partida
            z = y - x
            print("\nEstos son los objetos que tienes:\n",nombre['inventario'])
            print("\nHora actual:",x.hour,':',x.minute,':',x.second)
            print("Tienes hasta las:",tiempo_partida.hour,':',tiempo_partida.minute,':',tiempo_partida.second,"\nPor lo que te queda para terminar el juego:", z)
            print("\nTe queda de vida:",nombre['vida'])
            print("\nCantidad de pistas disponibles:",nombre["pista"],"\n")
            nombre["tiempo"] = str(z)
            with open('status.json', 'w') as file:
                json.dump(data, file, indent=4)
     


def pasar(usuario, rooms, lado):

    def inventario_oculto(usuario):
        with open('status.json', 'r') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                return nombre['inventario']

    
    objeto = rooms.objeto
    mensaje_requerido = "" 
    for lugar in objeto:
        if lugar['position']== lado:
            juegos = lugar['game']
            necesita = juegos['requirement']
            if necesita != False:
                mensaje_requerido = juegos["message_requirement"]
            break

    tengo = inventario_oculto(usuario)
    salir = False
    if type(necesita) == list:
        count = 0    
        tamano_R = len(necesita)
        if tamano_R > 1:
            for obtenido in tengo:
                for necesario in necesita:
                    if count <= tamano_R:
                        
                        if necesario == obtenido:
                            count +=1
                        elif "Titulo Universitario" in obtenido and "Mensaje" in necesario:
                            count +=1

                        if count == tamano_R:
                            salir = True
                            break
    elif necesita == "introducir contrase\u00f1a de la computadora":
        for obtenido in tengo:
            if "contraseña" in obtenido:
                print("En los cuartos estan enumeradas las letras de la contraseña")
                contrasena = input(">>>123456: ").lower()
                if contrasena == "pbclas":
                    salir = True

    else:
        for obtenido in tengo:
            if necesita == obtenido:
                salir = True
                break
    
    if salir:
        print("Tienes todo lo requerido")
    else:
        print(mensaje_requerido)
    return salir




def habitacion(cuarto,juego,usuario,tiempo_partida,registro,player):
    #time.sleep(5)
    #global rooms
    if cuarto == "Puerta_Laboratorio":
        scuarto = cuarto
    else:
        with open('API.json') as file:
            data = json.load(file)
            for ncuarto in data:
                scuarto = ncuarto['name']
                if scuarto == cuarto:
                    objeto = ncuarto['objects']    
                    rooms = cuartos(cuarto,objeto)
    
    while juego:
        
        guardar_contador(cuarto,player)
        x = temporizador.tiempo.hora_actual()
        y = tiempo_partida
        z = y - x
        if x >= y:
            print("Mala suerte se te acabo el tiempo XD, intentalo de nuevo")
            registro.Base_datos_records()
            time.sleep(4)
            borrar_guardado(usuario)
            return main()

        with open('status.json', 'r') as file:
            data = json.load(file)
        for nom in data[usuario]:
            vida = nom["vida"]
            if vida <= 0:
                print("TE QUEDASTE SIN VIDA< HAZ PERDIDO :(")
                time.sleep(4)
                borrar_guardado(usuario)
                return main()
            Fin = nom["Cuarto de Servidores _center"]
            if Fin == "1":
                z = str(z)
                registro =puntuaciones(registro.dificultad,registro.personaje,z,registro.usuario,registro.password,registro.edad)
                registro.Base_datos_records()
                Narrativa_Final(usuario)
                borrar_guardado(usuario)
                time.sleep(3)
                return main()
                

        lado = ""
        if cuarto == "Biblioteca":
            print(Habitaciones.Biblioteca)
            rooms.cuarto_objetos()
            desicion = input("\nIntroducir el numero de la opcion deseada: ")
            if desicion == "0":
                juego = False
            elif desicion == "1":
                lado = "left"
                if pasar(usuario, rooms, lado):
                    pass
                else:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
            elif desicion == "2":
                lado = "center"
                
            elif desicion == "3":
                lado = "right"
                if pasar(usuario, rooms, lado):
                    pass
                else:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                
            elif desicion == "4":
                juego = habitacion("Plaza Rectorado", juego,usuario, tiempo_partida,registro,player)
            elif desicion == "5":
                juego = habitacion("Pasillo Laboratorios ",juego,usuario, tiempo_partida,registro,player) 
            elif desicion == "p":
                inventario(usuario,tiempo_partida,registro)
                continuar = desicion_SN("Desea continuar en la partida?: ")
                if continuar:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                else:
                    return main()

            if juego:    
                validacion_juego(cuarto, lado,usuario, tiempo_partida,rooms)
        
        elif cuarto == "Pasillo Laboratorios ":

            print(Habitaciones.Puerta_Laboratorio_C)
            rooms.cuarto_objetos()
            desicion = input("\nIntroducir el numero de la opcion deseada: ")
            if desicion == "0":
                juego = False
            elif desicion == "2":
                lado = "center"
                if pasar(usuario, rooms, lado):
                    pass
                else:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                
            elif desicion == "4":
                juego = habitacion("Biblioteca", juego,usuario, tiempo_partida,registro,player)

            elif desicion == "5":
                lado = "center"
                if pasar(usuario, rooms, lado):
                    habitacion("Puerta_Laboratorio", juego,usuario, tiempo_partida,registro,player)
                else:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                
            elif desicion == "p":
                inventario(usuario,tiempo_partida,registro)
                continuar = desicion_SN("Desea continuar en la partida?: ")
                if continuar:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                else:
                    return main()
            if juego:    
                validacion_juego(cuarto,lado,usuario, tiempo_partida, rooms)
                    
        
        elif cuarto == "Puerta_Laboratorio":
            print(Habitaciones.Puerta_Laboratorio_A)
            print("1)Laboratorio SL001\n2)Biblioteca\nP)Inventario")
            desicion = input("\nIntroducir el numero de la opcion deseada: ")
            if desicion == "0":
                juego = False
            elif desicion == "1":
                juego = habitacion("Laboratorio SL001", juego,usuario, tiempo_partida,registro,player)
            elif desicion == "2":
                juego = habitacion("Biblioteca", juego,usuario, tiempo_partida,registro,player)
            elif desicion == "p":
                inventario(usuario,tiempo_partida,registro)
                continuar = desicion_SN("Desea continuar en la partida?: ")
                if continuar:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                else:
                    return main()
            
        elif cuarto == "Plaza Rectorado":

            print(Habitaciones.Plaza_Rectorado)
            rooms.cuarto_objetos()
            desicion = input("\nIntroducir el numero de la opcion deseada: ")
            if desicion == "0":
                juego = False
            elif desicion == "1":
                lado = "left"
            elif desicion == "2":
                lado = "center"
                if pasar(usuario, rooms, lado):
                    pass
                else:
                    with open('status.json') as file:
                        data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 1
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            juego = False
                    return habitacion(cuarto,juego,usuario,tiempo_partida,registro,player)
            elif desicion == "3":
                lado = "right"
            elif desicion == "4":
                juego = habitacion("Biblioteca", juego,usuario, tiempo_partida,registro,player)
            elif desicion == "p":
                inventario(usuario,tiempo_partida,registro)
                continuar = desicion_SN("Desea continuar en la partida?: ")
                if continuar:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                else:
                    return main() 
            if juego:    
                validacion_juego(cuarto, lado, usuario, tiempo_partida,rooms)

        elif cuarto == "Cuarto de Servidores ":

            print(Habitaciones.Cuarto_de_Servidores)
            rooms.cuarto_objetos()
            desicion = input("\nIntroducir el numero de la opcion deseada: ")
            if desicion == "0":
                juego = False
            elif desicion == "1":
                lado = "left"
                
            elif desicion == "2":
                lado = "center"
                if pasar(usuario, rooms, lado):
                    pass
                else:
                    return habitacion(cuarto,juego,usuario,tiempo_partida,registro,player)
            elif desicion == "3":
                lado = "right"
                
            elif desicion == "4":
                juego = habitacion("Laboratorio SL001", juego, usuario, tiempo_partida,registro,player)
            elif desicion == "p":
                inventario(usuario,tiempo_partida,registro)
                continuar = desicion_SN("Desea continuar en la partida?: ")
                if continuar:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                else:
                    return main()  
            if juego:    
                validacion_juego(cuarto, lado, usuario, tiempo_partida,rooms)

        elif cuarto == "Laboratorio SL001":

            print(Habitaciones.Laboratorios_SL001)
            rooms.cuarto_objetos()
            desicion = input("\nIntroducir el numero de la opcion deseada: ")
            if desicion == "0":
                juego = False
            elif desicion == "1":
                lado = "left"
                if pasar(usuario, rooms, lado):
                   pass
                else:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
            elif desicion == "2":
                lado = "center"
            elif desicion == "3":
                lado = "right"
                if pasar(usuario, rooms, lado):
                    pass
                else:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
            elif desicion == "4":
                juego = habitacion("Biblioteca", juego, usuario, tiempo_partida,registro,player)
            elif desicion == "5":
                juego = habitacion("Cuarto de Servidores ", juego, usuario, tiempo_partida,registro,player)
            
            elif desicion == "p":
                inventario(usuario,tiempo_partida,registro)
                continuar = desicion_SN("Desea continuar en la partida?: ")
                if continuar:
                    return habitacion(cuarto,juego,usuario, tiempo_partida,registro,player)
                else:
                    return main()   
            if juego:    
                validacion_juego(cuarto, lado, usuario, tiempo_partida,rooms)       

    return juego




def borrar_guardado(usuario):
    with open('status.json') as file:
        data = json.load(file)
        for nombre in data[usuario]:
            nombre["inventario"] = []
            nombre['Biblioteca_left']= "0"
            nombre['Biblioteca_center']= "0"
            nombre['Biblioteca_right']= "0"
            nombre['Plaza Rectorado_left']='0'
            nombre['Plaza Rectorado_center']='0'
            nombre['Plaza Rectorado_right']='0'
            nombre['Pasillo Laboratorios _center']='0'
            nombre['Laboratorio SL001_left']= '0'
            nombre['Laboratorio SL001_center']= '0'
            nombre['Laboratorio SL001_right']= '0'
            nombre['Cuarto de Servidores _left']='0'
            nombre['Cuarto de Servidores _center']='0'
            nombre['Cuarto de Servidores _right']='0'
            nombre["ahorcado_pista1"]= '0'
            nombre["ahorcado_pista2"]= '0'
            nombre["ahorcado_pista3"]= '0'
            nombre['Quizizz_Cultura_Unimetana_pista1']="0"
            nombre['Quizizz_Cultura_Unimetana_pista2']="0"
            nombre['Quizizz_Cultura_Unimetana_pista3']="0"
            nombre['memoria_con_emojis_pista1']="0"
            nombre["Adivinanzas_pista1"]="0"
            nombre["Adivinanzas_pista2"]="0"
            nombre["Adivinanzas_pista3"]="0"
            nombre["preguntas_pista1"]="0"
            nombre["preguntas_pista2"]="0"
            nombre["escoge_un_numero_entre_pista1"]="0"
            nombre["contador_Biblioteca"]="0"
            nombre["contador_Plaza Rectorado"]="0"
            nombre["contador_Cuarto de Servidores "]="0"
            nombre["contador_Laboratorio SL001"]="0"
            nombre["contador_Pasillo Laboratorios "]="0"
            nombre['contador_Puerta_Laboratorio']= "0"
            nombre["sopa_letras_pista1"]="0"
            nombre["sopa_letras_pista2"]="0"
            nombre["sopa_letras_pista3"]="0"
            with open('status.json', 'w') as file:
                json.dump(data, file, indent=4)

def revision(usuario):
    continuar = True
    while continuar:
        with open('status.json','r') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                if nombre["inventario"] == [] and nombre['Biblioteca_left']== "0" and nombre['Biblioteca_center']== "0" and nombre['Biblioteca_right']== "0":
                    if nombre['Plaza Rectorado_left']=='0' and nombre['Plaza Rectorado_center']=='0' and nombre['Plaza Rectorado_right']=='0' and nombre['Pasillo Laboratorios _center']=='0':
                        if nombre['Laboratorio SL001_left']== '0' and nombre['Laboratorio SL001_center']== '0' and nombre['Laboratorio SL001_right']== '0':
                            if nombre['Cuarto de Servidores _left']=='0' and nombre['Cuarto de Servidores _center']=='0' and nombre['Cuarto de Servidores _right']=='0':
                                continuar = False
                            break
                        break
                    break
                break
            break
    return continuar

def instrucciones():
    print("""
            -Al empezar se te explicara la situacion en la que te encuentras.
            -Dependiendo de la dificultad que elijas, obtendras cierta cantidad de vida, tiempo para terminar
            y pistas globales:
            Facil = 5 vidas, 5 pistas, 30 minutos,
            Normal = 3 vidas 3 pistas, 20 minutos
            Dificil = 1 vida, 2 pistas, 10 minutos
            - Siempre que estes en una habitacion, tienes la opcion de seleccionar los objetos de dicha habitacion
            o trasladarte a otra habitacion,
            en cada una se encuentra un menu de las opciones disponible que tiee cada habitacion
            (selecciona el numero de la accion que deseas tomar),
            - Cada juego viene con un premio  y una regla, 
            - El premio puede variar entre obtener mas vida u obtener un objeto, si logras resolver el juego
            - En caso contrario la Regla te dice la penitencia de no ser capaz de resolver el juego,
            - las pistas son a nivel global (la cantidad depende de la dificultad) por lo que si elegiste Normal,
            solo podras pedir 3 pistas durante
            todo el juego, asi que hay que saber administrarlas
            - Los objetos a veces te pediran un requerimiento para usarlos, los cuales son los premios de otros objetos,
            una pista sera mensaje 
            que te de cada objetos cuando no tengas los requerimientos qe se te pidan
            -El juego dependera mucho de tu habilidad como progrmador, de Cultura general de la
            Universidad Metropolitana y de tus habilidades matematicas
            -
            """)
    input("Listo  para juagar? presion una tecla y continuemos")

def Records_juegos():
    ciclo = True
    while ciclo:
        print('''
        1) Top 5 (por nivel)
        2) Cuartos mas visitados
        3) Quienes son los que mas juegan
        ''')
        desicion = input("ingrese el numero de lo que desea ver: ")
        if desicion =="1":
            ciclo1 = True
            while ciclo1:
                lista_normal_T =[] 
                lista_facil_T =[]
                lista_dificil_T=[]
                lista_normal_U =[] 
                lista_facil_U =[]
                lista_dificil_U=[]
                with open('records.json') as file:
                    data = json.load(file)
                
                for usuarios in data:  
                    for datos1 in data[usuarios]:  
                        for datos2 in datos1:  
                            #for datos2 in datos1:
                            datosD = datos2['dificultad']
                            datosT = datos2['tiempo']
                            
                            if datosT != "":
                                if datosD == "Normal": 
                                    lista_normal_T.append(datosT)
                                    lista_normal_U.append(usuarios)
                                if datosD == "Facil":
                                    lista_facil_T.append(datosT)
                                    lista_facil_U.append(usuarios)
                                if datosD == "Dificil":
                                    lista_dificil_T.append(datosT)
                                    lista_dificil_U.append(usuarios)
                lista_valores_n =[]
                tamano = len(lista_normal_T)
                if tamano > 0:
                    for n in range(0,tamano):
                        x_normal = time.strptime(lista_normal_T[n],'%X')
                        hora_normal = time.strptime("0:35:00",'%X')
                        x = hora_normal.tm_sec - x_normal.tm_sec
                        y = 0
                        if x < 0:
                            x +=60
                            y=1
                        z = hora_normal.tm_min - x_normal.tm_min
                        z -= y
                        tiempo = str(z)+":"+str(x)
                        lista_valores_n.append(tiempo)
                    for n1 in range(0,tamano-1):
                        for n2 in range(1+n1,tamano):
                            valor1 = lista_normal_T[n1]
                            valor2 = lista_normal_T[n2]
                            if valor2 > valor1:
                                lista_normal_T[n1] = valor2
                                lista_normal_T[n2] = valor1  
                                valor3 = lista_normal_U[n2]
                                lista_normal_U[n2] = lista_normal_U[n1]
                                lista_normal_U[n1] = valor3  
                                valor3 = lista_valores_n[n2]
                                lista_valores_n[n2] = lista_valores_n[n1]
                                lista_valores_n[n1] = valor3
                    
                lista_valores_f =[]
                tamano = len(lista_facil_T)
                if tamano > 0:
                    for n in range(0,tamano):
                        x_normal = time.strptime(lista_facil_T[n],'%X')
                        hora_normal = time.strptime("0:50:00",'%X')
                        x = hora_normal.tm_sec - x_normal.tm_sec
                        y = 0
                        if x < 0:
                            x +=60
                            y=1
                        z = hora_normal.tm_min - x_normal.tm_min
                        z -= y
                        tiempo = str(z)+":"+str(x)
                        lista_valores_f.append(tiempo)
                    for n1 in range(0,tamano-1):
                        for n2 in range(1+n1,tamano):
                            valor1 = lista_facil_T[n1]
                            valor2 = lista_facil_T[n2]
                            if valor2 > valor1:
                                lista_facil_T[n1] = valor2
                                lista_facil_T[n2] = valor1  
                                valor3 = lista_facil_U[n2]
                                lista_facil_U[n2] = lista_facil_U[n1]
                                lista_facil_U[n1] = valor3  
                                valor3 = lista_valores_f[n2]
                                lista_valores_f[n2] = lista_valores_f[n1]
                                lista_valores_f[n1] = valor3
                    
                lista_valores_d =[]
                tamano = len(lista_dificil_T)
                if tamano > 0:
                    for n in range(0,tamano):
                        x_normal = time.strptime(lista_dificil_T[n],'%X')
                        hora_normal = time.strptime("0:20:00",'%X')
                        x = hora_normal.tm_sec - x_normal.tm_sec
                        y = 0
                        if x < 0:
                            x +=60
                            y=1
                        z = hora_normal.tm_min - x_normal.tm_min
                        z -= y
                        tiempo = str(z)+":"+str(x)
                        lista_valores_d.append(tiempo)
                    for n1 in range(0,tamano-1):
                        for n2 in range(1+n1,tamano):
                            valor1 = lista_dificil_T[n1]
                            valor2 = lista_dificil_T[n2]
                            if valor2 > valor1:
                                lista_dificil_T[n1] = valor2
                                lista_dificil_T[n2] = valor1  
                                valor3 = lista_facil_U[n2]
                                lista_dificil_U[n2] = lista_dificil_U[n1]
                                lista_dificil_U[n1] = valor3  
                                valor3 = lista_valores_f[n2]
                                lista_valores_d[n2] = lista_valores_d[n1]
                                lista_valores_d[n1] = valor3
                
                usuarioD =lista_dificil_U
                valoresD =lista_valores_d
                usuarioN =lista_normal_U
                valoresN =lista_valores_n
                usuarioF =lista_facil_U
                valoresF =lista_valores_f

                print("\nTOP_5 de Nivel Dificil\n")
                tamano1 = 1
                tamano = len(valoresD)
                count =0
                for n1 in range(0,tamano):
                    count +=1
                    print(f"{count})-->  {usuarioD[n1]} --- {valoresD[n1]}")
                    tamano1 += 1
                    if tamano1 >5:
                        break

                print("\nTOP_5 de Nivel Normal\n")
                tamano1 = 1
                tamano = len(valoresN)
                count =0
                for n2 in range(0,tamano):
                    count +=1
                    print(f"{count})-->  {usuarioN[n2]} --- {valoresN[n2]}")
                    tamano1 += 1
                    if tamano1 >5:
                        break

                print("\nTOP_5 de Nivel Facil\n")
                tamano1 = 1
                tamano = len(valoresF)
                count =0
                for n3 in range(0,tamano):
                    count +=1
                    print(f"{count})-->  {usuarioF[n3]} --- {valoresF[n3]}")
                    tamano1 += 1
                    if tamano1 >5:
                        break


                continuar = desicion_SN("\nDesea seguir viendo los estadisticos: ")
                if not continuar:
                    ciclo1 = False        
        
        elif desicion == "2":
            orden1= []
            orden2= []
            print("\nCUARTOS MAS VISITADOS POR JUGADOR\n")         
            print("Nombre del Usuario        Cuarto              Cantidad") 
            with open('records.json') as file:
                data = json.load(file)
                for datos in data:
                    contador_Biblioteca = 0
                    contador_Laboratorio_SL001 = 0
                    contador_Plaza_Rectorado = 0
                    contador_Pasillo_Laboratorios = 0
                    contador_Cuarto_de_Servidores = 0
                    usuarios = datos
                    for datos1 in data[datos]:
                        for datos2 in datos1:
                            contador_Biblioteca += int(datos2['Biblioteca'])
                            contador_Laboratorio_SL001 += int(datos2['Laboratorio SL001'])
                            contador_Plaza_Rectorado += int(datos2['Plaza Rectorado'])
                            contador_Pasillo_Laboratorios += int(datos2['Pasillo Laboratorios '])
                            contador_Cuarto_de_Servidores += int(datos2['Cuarto de Servidores '])
                    orden1 = [contador_Biblioteca, contador_Laboratorio_SL001, contador_Plaza_Rectorado, contador_Pasillo_Laboratorios, contador_Cuarto_de_Servidores]
                    orden2 = [
                        " BIBLIOTECA           ",
                        " LABORATORIO SL001    ",
                        " PLAZA RECTORADO      ",
                        " PASILLO LABORATORIOS ",
                        " CUARTO DE SERVIDORES ",
                        ]  
                    for n1 in range(0,3):
                        for n2 in range(n1+1,4):
                            valor1 = int(orden1[n1])
                            valor2 = int(orden1[n2])
                            if valor2 > valor1:
                                orden1[n1] = valor2
                                orden1[n2] = valor1  
                                valor3 = orden2[n2]
                                orden2[n2] = orden2[n1]
                                orden2[n1] = valor3                                 
                             
                    print("   ",usuarios,"            ",orden2[0],"    ",orden1[0])
                    #print("Cantidad de veces que los jugadores vitan BIBLIOTECA:           ",contador_Biblioteca)
                    #print("Cantidad de veces que los jugadores vitan LABORATORIO SL001:    ",contador_Laboratorio_SL001)
                    #print("Cantidad de veces que los jugadores vitan PLAZA RECTORADO:      ",contador_Plaza_Rectorado)
                    #print("Cantidad de veces que los jugadores vitan PASILLO LABORATORIOS: ",contador_Pasillo_Laboratorios)
                    #print("Cantidad de veces que los jugadores vitan CUARTO DE SERVIDORES: ",contador_Cuarto_de_Servidores)
            continuar = desicion_SN("\nDesea seguir viendo los estadisticos: ")
            if not continuar:
                ciclo = False
        elif desicion == "3":
            print("\nJUGADORES EN EL ORDEN EN LO QUE MAS JUEGAN\n")         
            print("Nombre del Usuario     Cantidad") 
            with open('records.json') as file:
                data = json.load(file)
                orden1= []
                orden2= []
                for datos in data:
                    contador = 0
                    
                    
                    for datos1 in data[datos]:
                        usuarios = datos
                        
                        for datos2 in datos1:
                            contador +=1
                    
                    
                    orden2.append(usuarios)
                    orden1.append(contador)
                    
                tamano = len(orden1)
                
                for n1 in range(0,tamano-1):
                    
                    for n2 in range(1+n1,tamano):
                        
                        valor1 = int(orden1[n1])
                        valor2 = int(orden1[n2])
                        
                        if valor2 > valor1:
                            orden1[n1] = valor2
                            orden1[n2] = valor1  
                            valor3 = orden2[n2]
                            orden2[n2] = orden2[n1]
                            orden2[n1] = valor3      
                                               
                for n1 in range (0,tamano):    
                    print("   ",orden2[n1],"         ",orden1[n1])
    
            continuar = desicion_SN("\nDesea seguir viendo los estadisticos: ")
            if not continuar:
                ciclo = False
        else:
            return main()


def main():
    juego = True
    extraccion_API()
    verificar()
    while juego:
        players = []
        os.system("cls")
        menu() 
        opcion  = input("\nIntroducir el numero de la opcion deseada: ")
        if opcion == "1":
            print(("\nDATOS DEL JUGADOR"))
            usuario = input("Ingrese el Usuario: ")
            player = Jugador(usuario,False,False)  
            
            if player.buscar_usuario():
                print("Usuario Registrado")
                password = input("Ingrese su contrasena: ")
                player = Jugador(usuario,password,False)  
                if player.validar_contrasena(player.password):
                    revi =revision(usuario)
                    if revi:
                        continuar = desicion_SN("Tiene una partida guardada. Desea conituarla?: ")
                        if continuar:
                            with open('data.json') as file:
                                data = json.load(file)
                                for usuarios in data['usuarios']:
                                    if usuarios['nombre'] == usuario:
                                        edad = usuarios['edad']
                                        player = Jugador(usuario,password,edad)  
                                        players.append(player)
                                        with open('status.json') as file:
                                            data = json.load(file)
                                            for nombre in data[usuario]:
                                                tiempo = nombre['tiempo'] 
                                                dificultad = nombre['dificultad']
                                                personaje = nombre['personaje']
                                                break
                                            print(tiempo)
                                            tiempo_guardado = time.strptime(tiempo,'%X')
                                            x = tiempo_guardado.tm_min
                                            y = tiempo_guardado.tm_sec
                                            tiempo_partida = temporizador.tiempo.partida_guardada(x,y)
                                            registro  =puntuaciones(dificultad,personaje,"",player.usuario,player.password,player.edad)      
                                            habitacion("Biblioteca",True,usuario, tiempo_partida,registro,player)
                        if not continuar:
                            borrar_guardado(usuario)
                            print("Se borro la partida guardada")
                            dificultad = input('Selecciones la dificultad del juego: (1)Facil, (2)Normal, (3)Dificil: ')
                            if dificultad == "1" or dificultad == "2" or dificultad == "3":
                                if dificultad == "1":
                                    vidas = 8.0
                                    pistas = 5
                                    tiempo = 50
                                    
                                elif dificultad == "2":
                                    vidas = 5.0
                                    pistas = 3
                                    tiempo = 35
                                elif dificultad == "3":
                                    vidas = 2.0
                                    pistas = 2
                                    tiempo = 20

                                personajes()
                                personaje = input("Quien sera el salvador de la unimet: ")
                                if personaje.isnumeric():
                                    personaje = int(personaje)
                                    if 0 <= personaje <= 7:
                                        personaje = str(personaje)
                                        personaje = seleccion_personaje(personaje)
                                        dificultadn = desicion3(dificultad)
                                        with open('status.json') as file:
                                            data = json.load(file)
                                            for nombre in data[usuario]:
                                                nombre["dificultad"] = dificultadn
                                                nombre['vida'] = vidas
                                                nombre['pista'] = pistas
                                                nombre['tiempo'] = tiempo
                                                nombre['personaje'] = personaje
                                            with open('status.json', 'w') as file:
                                                json.dump(data, file, indent=4)
                                            
                                            
                                        dificultad = desicion3(dificultad)
                                    else:
                                        print("valores desconocidos")
                                        return main()
                                else:
                                    print("valores desconocidos")
                                    return main()

                                primera_narrativa(tiempo, personaje)
                                if desicion_SN("¿Aceptas el reto?"):
                                    with open('data.json') as file:
                                        data = json.load(file)
                                        for usuarios in data['usuarios']:
                                            if usuarios['nombre'] == usuario:
                                                edad = usuarios['edad']
                                    player = Jugador(usuario,password,edad)  
                                    players.append(player)
                                    tiempo_partida = temporizador.tiempo.cronometro(tiempo)
                                    registro =puntuaciones(dificultad,personaje,"",player.usuario,player.password,player.edad)
                                    Segunda_Narrativa(usuario)
                                    habitacion("Biblioteca",True,usuario,tiempo_partida,registro,player)
                    else:
                        print("No hay partidas guardadas")
                        dificultad = input('Selecciones la dificultad del juego: (1)Facil, (2)Normal, (3)Dificil: ')
                        if dificultad == "1" or dificultad == "2" or dificultad == "3":
                            if dificultad == "1":
                                vidas = 8.0
                                pistas = 5
                                tiempo = 50
                            elif dificultad == "2":
                                vidas = 5.0
                                pistas = 3
                                tiempo = 35
                            elif dificultad == "3":
                                vidas = 2.0
                                pistas = 2
                                tiempo = 20
    
                            
                            
                            personajes()
                            personaje = input("Quien sera el salvador de la unimet: ")
                            if personaje.isnumeric():
                                    personaje = int(personaje)
                                    if 0 <= personaje <= 7:
                                        personaje = str(personaje)
                                        personaje = seleccion_personaje(personaje)
                                        dificultadn = desicion3(dificultad)
                                        with open('status.json') as file:
                                            data = json.load(file)
                                            for nombre in data[usuario]:
                                                nombre["dificultad"] = dificultadn
                                                nombre['vida'] = vidas
                                                nombre['pista'] = pistas
                                                nombre['tiempo'] = tiempo
                                                nombre['personaje'] = personaje
                                                
                                            with open('status.json', 'w') as file:
                                                json.dump(data, file, indent=4)

                                    
                                        dificultad = desicion3(dificultad)
                                    else:
                                        print("valores incorrectos")
                                        return main()
                            else:
                                print("valores incorrectos")
                                return main()

                            
                            
                            primera_narrativa(tiempo, personaje)
                            if desicion_SN("¿Aceptas el reto?"):
                                with open('data.json') as file:
                                    data = json.load(file)
                                    for usuarios in data['usuarios']:
                                        if usuarios['nombre'] == usuario:
                                            edad = usuarios['edad']
                                player = Jugador(usuario,password,edad)  
                                players.append(player)
                                tiempo_partida = temporizador.tiempo.cronometro(tiempo)
                                registro  =puntuaciones(dificultad,personaje,"",player.usuario,player.password,player.edad)
                                Segunda_Narrativa(usuario)
                                habitacion("Biblioteca",True,usuario,tiempo_partida,registro,player)
                else:
                    print("clave invalida")
            else:
                if usuario != "":
                    print("Usuario no registrado")
                    password = input("Ingrese una contrasena: ")
                    edad = input("Ingrese su edad: ")
                    if edad.isnumeric():
                        edad = int(edad)
                    else:
                        ("valor invalido")
                        return main()
                    player = Jugador(usuario,password,edad)  
                    Base_datos(player)
                    players.append(player)
        elif opcion == "2":
            instrucciones()
        elif opcion == "3":
           Records_juegos()
        elif opcion == "4":
            sys.exit()
        else:
            True 
    
main()