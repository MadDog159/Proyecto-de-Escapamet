from typing import Final, KeysView
from cuartos import cuartos
from os import error
import random
import json
import os
from scipy.misc import derivative
from sympy import *
from sympy import sympify
from sympy.parsing.sympy_parser import parse_expr
import math
from fractions import Fraction
import numpy as np
import pygame
from jugadores import Jugador
import temporizador
import time

class minijuegos():


    def ahorcado(rooms,preguntas,lado,usuario):    
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        x = random.randint(0,2)
        x1 = x+1
        pregunta = preguntas[x]
        with open('status.json') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                pista_contador = nombre["ahorcado_pista"+str(x1)]
                y = int(pista_contador) + 1
                if y >= 4:
                    y = 1
                pista_contador_G = nombre['pista']
                break
        print("Bienvenido al ahorcado")
        print(pregunta['question'])
        valor = pregunta['answer']
        valor = valor.lower()
        pista = pregunta['clue_'+str(y)]
        if pista_contador_G == 0:
            pista = ""
        
        tamano = len(valor)
        vector = []
        vector1 = []
        vector2 = []
        contador = 0
        imagen = 1
        while contador < tamano:
            vector.append("_")
            vector1.append(valor[contador])
            vector2.append("n")
            contador +=1
        ciclo = True
        while ciclo:
            minijuegos.imprimir_imagen(imagen)
            print(*vector)
            print("Para pedir una pista ingrese el caracter: * (asterisco)")
            respuesta = input("Ingrese una letra : ")
            if respuesta == "*":
                entrar = True
                if pista_contador_G != 0:
                    if nombre["ahorcado_pista"+str(x1)] == "3":
                        print("llegaste al limite de pistas")
                        entrar = False
                        pass
                if entrar:
                    print(pista)
                    grabar = False
                    if y <=3:
                        nombre["ahorcado_pista"+str(x1)] = str(y)
                        y += 1
                        grabar = True
                        if y <=3:
                            pista = pregunta['clue_'+str(y)]
                        if pista_contador_G >0:
                            pista_contador_G -=1
                            nombre['pista'] = pista_contador_G
                            grabar = True
                
                
                if grabar:
                    with open('status.json', 'w') as file:
                        json.dump(data, file, indent=4)


                if pista_contador_G == 0:
                    pista = "Ya usted no tienes mas posibilidad de pista"
                    
            else:    
                respuesta = respuesta.lower()
                contador = 0
                entro = False
                while contador < tamano:
                    if  vector1[contador] == respuesta:
                        entro = True
                        vector[contador] = respuesta
                        vector2[contador]= "s"
                    contador +=1
                if entro:
                    contador = 0
                    entro = True
                    while contador < tamano:
                        if vector2[contador] == "n":
                            entro = False
                            break
                        contador +=1
                    if entro:
                        print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                        if premio != "":
                            with open('status.json') as file:
                                data = json.load(file)
                                for nombre in data[usuario]:
                                    nombre["inventario"].append(premio)
                                    nombre[cuarto+'_'+lado] = "1"
                                    with open('status.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                        ciclo = False
                    else:
                        
                        print("respuesta correcta")
                    
                        
                else:
                    print("respuesta incorrecta")
                    imagen += 1
                    with open('status.json') as file:
                        data = json.load(file)
                        for nom in data[usuario]:
                            vida2 = nom['vida']
                            float(vida2)
                            vida3  = vida2 - 0.25
                            nom["vida"] = vida3
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            if nom["vida"] <= 0:
                                ciclo = False
                            else:
                                break
                    if imagen == 7:
                        print("perdio el juego")
                        ciclo = False    


    def imprimir_imagen(valor):

        error1 = """
               _______________
              |               |
              |               |
              |              / \ 
              |             /   \ 
              |            |     |
              |             \   /
              |              \ /
              |
              |
              |
              |
              |
              |
              |
              |
              |
        ______|_______
        """
        error2 = """
               _______________
              |             __|__
              |            / ___ \ 
              |           |/     \|
              |           |       |
              |            \_   _/
              |             \| |/
              |              \ /
              |
              |
              |
              |
              |
              |
              |
              |
              |
        ______|_______
    
        """
        error3 = """
               _______________
              |             __|__ 
              |            / ___ \ 
              |           |/     \|
              |           |       |
              |            \_   _/
              |             \| |/
              |            __\ /__
              |           /       \ 
              |            /|   |\ 
              |             |   |
              |             |___|
              |
              |
              |
              |
              |
        ______|_______
    
        """
        error4 = """
                   _______________
                  |             __|__ 
                  |            / ___ \ 
                  |           |/     \|
                  |           |       |
                  |            \_   _/
                  |             \| |/
                  |            __\ /__
                  |           /       \  
                  |       ___/ /|   |\ 
                  |      ||___/ |   |
                  |             |___|
                  |
                  |
                  |
                  |
                  |
            ______|_______
        
            """
        
        error5 = """
                   _______________
                  |             __|__ 
                  |            / ___ \ 
                  |           |/     \|
                  |           |       |
                  |            \_   _/
                  |             \| |/
                  |            __\ /__
                  |           /       \ 
                  |       ___/ /|   |\ \___
                  |      ||___/ |   | \___||
                  |             |___|
                  |
                  |
                  |
                  |
                  |
            ______|_______
        
            """
        error6 = """
                   _______________
                  |             __|__ 
                  |            / ___ \ 
                  |           |/     \|
                  |           |       |
                  |            \_   _/
                  |             \| |/
                  |            __\ /__
                  |           /       \ 
                  |       ___/ /|   |\ \___
                  |      ||___/ |   | \___||
                  |             |___|
                  |                  \ 
                  |                \  \ 
                  |                 \__\_
                  |                  |___|
                  |
            ______|_______
        
            """
        
        error7 = """
                   _______________
                  |             __|__ 
                  |            / ___ \ 
                  |           |/     \|
                  |           |       |
                  |            \_   _/
                  |             \| |/
                  |            __\ /__
                  |           /       \ 
                  |       ___/ /|   |\ \___
                  |      ||___/ |   | \___||
                  |             |___|
                  |            /     \ 
                  |           /  / \  \ 
                  |         _/__/   \__\_
                  |        |___|     |___|
                  |
            ______|_______
        
            """
        if valor == 1:
            print(error1)
        elif valor == 2:
            print(error2)
        elif valor== 3:
            print(error3)
        elif valor== 4:
            print(error4)
        elif valor== 5:
            print(error5)
        elif valor== 6:
            print(error6)
        elif valor == 7:
            print(error7)
    
    def adivinanzas(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        pregunta = preguntas
        x = random.randint(0,2)
        x1 = x+1
        pregunta = preguntas[x]
        with open('status.json') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                pista_contador = nombre["Adivinanzas_pista"+str(x1)]
                y = int(pista_contador)+1
                if y >= 4:
                    y = 1
                pista_contador_G = nombre['pista']
                break
        valor = pregunta['answers']
        print("\n",pregunta['question'])
        pista = pregunta['clue_'+str(y)]
        if pista_contador_G == 0:
            pista = ""
        ciclo = True
        while ciclo:
            print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
            respuesta = input("Escribe la respuesta que considere correcta: ")
            if respuesta == "*":
                entrar = True
                if pista_contador_G != 0:
                    if nombre["Adivinanzas_pista"+str(x1)] == "3":
                        print("llegaste al limite de pistas")
                        entrar = False
                        pass
                if entrar:
                    print("\n",pista)
                    grabar = False
                    if y <= 3:
                        nombre["Adivinanzas_pista"+str(x1)] = str(y)
                        y += 1
                        grabar = True
                        if y <=3:
                            pista = pregunta['clue_'+str(y)]
                        if pista_contador_G >0:
                            pista_contador_G -=1
                            nombre['pista'] = pista_contador_G
                            grabar = True
                    
                
                if grabar:
                    with open('status.json', 'w') as file:
                        json.dump(data, file, indent=4)


                if pista_contador_G == 0:
                    pista = "Ya usted no tienes mas posibilidad de pista"
                
            elif respuesta in valor:
                print("Respuesta correcta")    
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            nombre[cuarto+'_'+lado] = "1"
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                                break
                        ciclo = False
            else:      
                with open('status.json') as file:
                    data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 0.5
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            ciclo = False
                        break
                print("respuesta incorrecta\n Perdiste media vida, te queda",nom['vida'])
    
    def preguntas(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        pregunta = preguntas
        x = random.randint(0,1)
        x1 = x+1
        with open('status.json') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                pista_contador = nombre["preguntas_pista"+str(x1)]
                y = int(pista_contador)+1
                if y >= 4:
                    y = 1
                pista_contador_G = nombre['pista']
                break
        pregunta = preguntas[x]
        valor = pregunta['answer']
        print(pregunta['question'])
        if x == 1:
            y =1
        pista = pregunta['clue_'+str(y)]
        if pista_contador_G == 0:
            pista = ""
        ask = pregunta['question']
        n1 = len(ask)
        n = ask.find('"',0,n1)
        n+=1
        n2 = ask.find('"',n,n1)
        frase = ask[n:n2]
        ciclo = True
        while ciclo:
            print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
            respuesta= input("Escribe el codigo necesario para la respuesta: \n")
            if x == 0: 
                if respuesta == "*":
                    entrar = True
                    if pista_contador_G != 0:
                        if nombre["preguntas_pista"+str(x1)] == "3":
                            print("llegaste al limite de pistas")
                            entrar = False
                            pass
                    if entrar:
                        print("\n",pista)
                        grabar = False
                        if y <= 3:
                            nombre["preguntas_pista"+str(x1)] = str(y)
                            y += 1
                            grabar = True
                            if y <=3:
                                pista = pregunta['clue_'+str(y)]
                            if pista_contador_G >0:
                                pista_contador_G -=1
                                nombre['pista'] = pista_contador_G
                                grabar = True
                        
                    
                            if grabar:
                                with open('status.json', 'w') as file:
                                    json.dump(data, file, indent=4)
            
            
                    if pista_contador_G == 0:
                        pista = "Ya usted no tienes mas posibilidad de pista"
                elif respuesta != "*":
                    n = 0
                    y = 0
                    valor1 = 0
                    while n < n1:
                        n = ask.find(' ',y,n1)
                        if  n > 0:
                            frase = ask[y:n]
                            if frase.isnumeric():
                                valor1 = int(frase)
                                break
                        y = n+1
                    answer = str(valor1)
                    if respuesta == answer:
                        respuesta = ""
                    try:
                        respuesta = eval(respuesta)
                    except:
                        print("comando invalido")
                        
                    if respuesta == answer:
                        print("respuesta correcta")
                        print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                        if premio != "":
                            with open('status.json') as file:
                                data = json.load(file)
                                for nombre in data[usuario]:
                                    nombre["inventario"].append(premio)
                                    nombre[cuarto+'_'+lado] = "1"
                                    with open('status.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                                        break
                                ciclo = False
                    else:
                        with open('status.json') as file:
                            data = json.load(file)
                            for nom in data[usuario]:
                                vida2 = nom['vida']
                                float(vida2)
                                vida3  = vida2 - 0.5
                                nom["vida"] = vida3
                                with open('status.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                if nom["vida"] <= 0:
                                    ciclo = False
                                break
                        print("Respuesta incorrecta\n Perdiste media vida, te queda",nom['vida'])
                        seguir = input("Deseas seguir intentando?: (S/N)")
                        if seguir == "n":
                            ciclo = False

            
            elif x ==1:   
                if respuesta == "*":
                    entrar = True
                    if pista_contador_G != 0:
                        if nombre["preguntas_pista"+str(x1)] == "1":
                            print("llegaste al limite de pistas")
                            entrar = False
                            pass
                    if entrar:
                        print("\n",pista)
                        grabar = False
                        if y <= 1:
                            nombre["preguntas_pista"+str(x1)] = str(y)
                            y += 1
                            grabar = True
                            if y <=1:
                                pista = pregunta['clue_'+str(y)]
                            if pista_contador_G >0:
                                pista_contador_G -=1
                                nombre['pista'] = pista_contador_G
                                grabar = True
                        
                    
                                if grabar:
                                    with open('status.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                
                
                    if pista_contador_G == 0:
                        pista = "Ya usted no tienes mas posibilidad de pista"       

                elif respuesta != "*":
                    answer = "' '.join(list(map(lambda x: x[::-1], frase.split())))"
                    answer = eval(answer)
                    if respuesta == answer:
                        respuesta = ""
        
                    try:
                        respuesta = eval(respuesta)
                    except:
                        print("comando invalido")
    
                    if respuesta == answer:
                        print("respuesta correcta")
                        print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                        if premio != "":
                            with open('status.json') as file:
                                data = json.load(file)
                                for nombre in data[usuario]:
                                    nombre["inventario"].append(premio)
                                    nombre[cuarto+'_'+lado] = "1"
                                    with open('status.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                                        break
                                ciclo = False
                    else:
                        with open('status.json') as file:
                            data = json.load(file)
                            for nom in data[usuario]:
                                vida2 = nom['vida']
                                float(vida2)
                                vida3  = vida2 - 0.5
                                nom["vida"] = vida3
                                with open('status.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                if nom["vida"] <= 0:
                                    ciclo = False
                                break
                        print("Respuesta incorrecta\n Perdiste media vida, te queda",nom['vida'])
                        seguir = input("Deseas seguir intentando?: (S/N)")
                        if seguir == "n":
                            ciclo = False

 
    def Preguntas_matematicas(rooms,preguntas,lado,usuario):
        def derivar(ecuacion,evaluacion):
            x=Symbol('x') 
        
            #Parseamos de string a expresión
            y= parse_expr(ecuacion)
        
            derivada=(y.diff('x'))
            derivadas = str(derivada)
            derivada1 = ""
            for dentro in derivadas:
                dentro1 = dentro
                if dentro1 == "x":
                    dentro1 = evaluacion
                derivada1 +=dentro1  
            
            z = parse_expr(derivada1)
            resultado = z.evalf()
            resultado = str(resultado)
            final = str(Fraction(resultado))
            #print(derivada)
            #print(final)
            return final


        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        x = random.randint(2,2)
        pregunta = preguntas[x]
        ciclo = True
        while ciclo:
            if x == 0:
                ecuacion = pregunta['question']
                n1 = len(ecuacion)
                n = ecuacion.find('=',0,n1)
                n2=n+1
                n2 = ecuacion.find('"',n,n1)
                ecuacion1 = ecuacion[n+2:n2]
                ecuacion2 = ""
                for dentro in ecuacion1:
                    dentro1 = dentro
                    if dentro1 == "e":
                        dentro1 = "i"#evaluacion
                    ecuacion2 +=dentro1  
                ecuacion2 = str(ecuacion2)
                valor = derivar(ecuacion2,"pi")
                print(pregunta['question'])
                print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
                respuesta = input("Ingrese la respuesta de la funcion que considere correcta: (ingresela en formato fracccional)\n")
                
            elif x == 1:
                ecuacion = pregunta['question']
                n1 = len(ecuacion)
                n = ecuacion.find('=',0,n1)
                n2=n+1
                n2 = ecuacion.find('"',n,n1)
                ecuacion1 = ecuacion[n+2:n2-2]
                ecuacion2 = ""
                for dentro in ecuacion1:
                    dentro1 = dentro
                    if dentro1 == "e":
                        dentro1 = "i"#evaluacion
                    ecuacion2 +=dentro1  
                ecuacion2 = str(ecuacion2)
                valor = derivar(ecuacion2,"pi")
                print(pregunta['question'])
                print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
                respuesta = input("Ingrese la respuesta de la funcion que considere correcta: (ingresela en formato fracccional)\n")
    
               
            elif x == 2:
                ecuacion = pregunta['question']
                n1 = len(ecuacion)
                n = ecuacion.find('=',0,n1)
                n2=n+1
                n2 = ecuacion.find('"',n,n1)
                ecuacion1 = ecuacion[n+2:n2]
                ecuacion2 = ""
                for dentro in ecuacion1:
                    dentro1 = dentro
                    if dentro1 == "e":
                        dentro1 = "i"#evaluacion
                    ecuacion2 +=dentro1  
                ecuacion2 = str(ecuacion2)
                valor = derivar(ecuacion2,"pi/3")
                print(pregunta['question'])
                print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
                respuesta = input("Ingrese la respuesta de la funcion que considere correcta: (ingresela en formato fracccional)\n")
    
            if respuesta == valor:
                print("Respuesta correcta")
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            vida2 = nombre['vida']
                            float(vida2)
                            vida3  = vida2 + 1
                            nombre["vida"] = vida3
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                                ciclo = False
                            
            elif respuesta == "*":
                print(pregunta['clue_1'])
                break
            else:
                print("Respuesta incorrecta")
                with open('status.json') as file:
                    data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 0.25
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            ciclo = False
                        else:
                            break
            


    
        




    def memoria(rooms,preguntas,lado,usuario):
        
        def grafico():
            print("\nCARTAS DEL JUEGO DE MEMORIA ")
            print("==============================")
            print("||  1  ||  2  ||  3  ||  4  ||")
            #print(" ",grafico1[lista1[0]]," ",grafico1[lista1[1]]," ",grafico1[lista1[2]]," ",grafico1[lista1[3]])
            print("|| ",grafico2[0]," || ",grafico2[1]," || ",grafico2[2]," || ",grafico2[3]," || ")
            print("==============================")
            print("||  5  ||  6  ||  7  ||  8  ||")
            #print(" ",grafico1[lista1[4]]," ",grafico1[lista1[5]]," ",grafico1[lista1[6]]," ",grafico1[lista1[7]])
            print("|| ",grafico2[4]," || ",grafico2[5]," || ",grafico2[6]," || ",grafico2[7]," || ")
            print("==============================")
            print("||  9  || 10  || 11  || 12  ||")
            #print(" ",grafico1[lista1[8]]," ",grafico1[lista1[9]]," ",grafico1[lista1[10]]," ",grafico1[lista1[11]])
            print("|| ",grafico2[8]," || ",grafico2[9]," || ",grafico2[10]," || ",grafico2[11]," || ")
            print("==============================")
            print("|| 13  || 14  || 15  || 16  ||")
            #print(" ",grafico1[lista1[12]]," ",grafico1[lista1[13]]," ",grafico1[lista1[14]]," ",grafico1[lista1[15]])
            print("|| ",grafico2[12]," || ",grafico2[13]," || ",grafico2[14]," || ",grafico2[15]," || ")
            print("==============================")
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        pregunta = preguntas
        with open('status.json') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                pista_contador = nombre["memoria_con_emojis_pista1"]
                y = int(pista_contador)
                if y >= 2:
                    y = 1
                pista_contador_G = nombre['pista']
                break
        print("Bienvenido al juego de memoria")
        #print(juegos['memoria']["graficos"])
        grafico11= pregunta[0]['question']
        grafico1 = []
        grafico1.append(grafico11[3])
        grafico1.append(grafico11[8])
        grafico1.append(grafico11[13])
        grafico1.append(grafico11[18])
        grafico1.append(grafico11[82])
        grafico1.append(grafico11[87])
        grafico1.append(grafico11[92])
        grafico1.append(grafico11[225])
        lista1 =[0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
        grafico2 =["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]
        grafico3 =["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]
        #grafico4 = [grafico1[0],grafico1[1],grafico1[2],grafico1[3],grafico1[4],grafico1[5],grafico1[6],grafico1[7],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0],grafico1[0]]
        lista3 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #print(lista1,"lista 1")
        random.shuffle(lista1)
        #print(lista1,"lista 2")
        terminado = True
        while terminado:
            os.system("cls")
            grafico()
            
            ciclo = True
            entrada1 = 0
            entrada2 = 0
            if pista_contador_G == 0:
                pista = ""
            while ciclo:
                ciclo1 = True
                
                entrada1 = input("incluir el numero de la primera carta a voltear: ")
                if entrada1.isnumeric():
                    entrada1 = int(entrada1)
                    if entrada1 > 0 and entrada1 < 17:
                        ent = entrada1 - 1
                        if lista3[ent] ==1:
                            print("La carta ya esta volteada")
                            ciclo1 = False
                        else:
                            ciclo1 = False
                            ciclo = False
                if ciclo1:
                    print("valor introducido incorrecto")
            post1 = entrada1 - 1
            post11 = entrada1 - 1
            post1 = lista1[post1]
            
            grafico2[post11]= grafico1[post1]

            grafico()
            
            ciclo = True
            while ciclo:
                ciclo1 = True
                print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
                entrada2 = input("incluir el numero de la segunda carta a voltear: ")
                if entrada2 == "*":
                    if nombre["memoria_con_emojis_pista1"] == "1":
                        print("llegaste al limite de pistas")
                        ciclo1 = False
                        pass
                    grabar = False
                    if y <=1:
                        grabar = True
                        y += 1
                        nombre["memoria_con_emojis_pista1"] = str(y)
                        if y <=1:
                            n = 0
                            while n < 16:
                                if lista3[n] == 0:
                                    if entrada1-1 != n:
                                        post2 = n
                                        post22 = n
                                        post3 = lista1[post2]    
                                        if grafico1[post1] == grafico1[post3]:
                                            print("entro1")
                                            #grafico2[post11]= grafico1[post1]
                                            #grafico2[post22]= grafico1[post3]
                                            #grafico3[post11]= grafico2[post11]
                                            #grafico3[post22]= grafico2[post22]
                                            #lista3[post11]=1
                                            #lista3[post22]=1
                                            entrada2 = str(n+1)
                                            
                                            break
                                n+=1

                        if pista_contador_G >0:
                            pista_contador_G -=1
                            nombre['pista'] = pista_contador_G
                            grabar = True
                    if grabar:
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    if pista_contador_G == 0:
                        pista = "Ya usted no tienes mas posibilidad de pista"
                if entrada2.isnumeric():
                    entrada2 = int(entrada2)
                    if entrada2 > 0 and entrada2 < 17:
                        ent = entrada2 - 1
                        if entrada1 == entrada2:
                            print("ya esta carta fue seleccionada")
                            ciclo1 = False
                        elif lista3[ent] ==1:
                            print("La carta ya esta volteada")
                            ciclo1 = False
                        else:   
                            ciclo = False
                            ciclo1 = False
                            
                if ciclo1:
                    print("valor introducido incorrecto")
                    
            
            post2 = entrada2 - 1
            post22 = entrada2 - 1
            post2 = lista1[post2]
            
            if grafico1[post1] == grafico1[post2]:
                print("las cartas son identicas") 
                grafico2[post11]= grafico1[post1]
                grafico2[post22]= grafico1[post2]
                grafico3[post11]= grafico2[post11]
                grafico3[post22]= grafico2[post22]
                lista3[post11]=1
                lista3[post22]=1
                final = True
                for listo in lista3:
                    if listo == 0:
                        final = False
                        break
                if final:
                    print("JUEGO TERMINADO")
                    print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                    if premio != "":
                        with open('status.json') as file:
                            data = json.load(file)
                            for nombre in data[usuario]:
                                nombre["inventario"].append(premio)
                                nombre[cuarto+'_'+lado] = "1"
                                with open('status.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                    ciclo = False
                    terminado = False
                

            else:
                grafico2[post22]= grafico1[post2]
                grafico()
                print("las cartas son diferentes")
                
                grafico2[post11]=  grafico3[post11]
                grafico2[post22]=  grafico3[post22]
                with open('status.json') as file:
                    data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 0.25
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            ciclo = False
                        else:
                            break
                respuesta = input("Desea continuar con el juego de memoria de emojis: (S/N) ").lower()
                if respuesta == "n":
                    terminado = False
    

    def Quizizz_Cultura_Unimetana(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        x = random.randint(0,2)
        x1 = x+1
        pregunta = preguntas[x]
        with open('status.json') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                pista_contador = nombre["Quizizz_Cultura_Unimetana_pista"+str(x1)]
                y = int(pista_contador) + 1
                if y >= 2:
                    y = 1
                pista_contador_G = nombre['pista']
                break
        print("Bienvenido al Quizizz Cultura Unimetana")
        print('\n',pregunta['question'])
        pista = pregunta['clue_'+str(y)]
        valor = pregunta['correct_answer']
        valor1 = pregunta['answer_2']
        valor2 = pregunta['answer_3']
        valor3 = pregunta['answer_4']
        valores = [valor,valor1,valor2,valor3]
        random.shuffle(valores)
        if pista_contador_G == 0:
            pista = ""
        contador = 0
        for respuestas in valores:
            contador += 1
            print(f'{contador}){respuestas}',sep='\n')
        ciclo = True
        while ciclo:
            print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
            seleccion = input("Ingrese el numero de la respuesta que considere correcta:")
            if seleccion == "*":
                if nombre["Quizizz_Cultura_Unimetana_pista"+str(x1)] == "1":
                    print("llegaste al limite de pistas")
                    pass
                print(pista)
                grabar = False
                if y <=1:
                    nombre["Quizizz_Cultura_Unimetana_pista"+str(x1)] = str(y)
                    y += 1
                    grabar = True
                    if y <=1:
                        pista = pregunta['clue_'+str(y)]
                    if pista_contador_G >0:
                        pista_contador_G -=1
                        nombre['pista'] = pista_contador_G
                        grabar = True
                
                
                if grabar:
                    with open('status.json', 'w') as file:
                        json.dump(data, file, indent=4)
                if pista_contador_G == 0:
                    pista = "Ya usted no tienes mas posibilidad de pista"
            else:
                salir = False
                incorrecto = True
                if seleccion.isnumeric():
                    seleccion = int(seleccion)
                    if seleccion > 0 and seleccion <= contador:     
                        incorrecto = False
                        respuestas_d = valores[seleccion-1]
                        if respuestas_d == valor:
                            print("Respuesta correcta")
                            print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                            if premio != "":
                                with open('status.json') as file:
                                    data = json.load(file)
                                    for nombre in data[usuario]:
                                        nombre["inventario"].append(premio)
                                        nombre[cuarto+'_'+lado] = "1"
                                        with open('status.json', 'w') as file:
                                            json.dump(data, file, indent=4)
                            ciclo = False
                            
                        else:
                            print("Respuesta incorrecta")
                            with open('status.json') as file:
                                data = json.load(file)
                                for nom in data[usuario]:
                                    vida2 = nom['vida']
                                    float(vida2)
                                    vida3  = vida2 - 0.5
                                    nom["vida"] = vida3
                                    with open('status.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                                    if nom["vida"] <= 0:
                                        ciclo = False
                                    else:
                                        break
                            salir = True
                if incorrecto:
                    print("valor introducido incorrecto")
                if salir:
                    salir1 = input("Desea continuar: (S/N) ").lower()
                    if salir1 != "s":
                        ciclo = False
    
    def Encuentra_la_lógica_y_resuelve(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        pregunta = preguntas
        x = random.randint(0,1)
        pregunta = preguntas
        print('\n',pregunta[x])
        respuesta = input("ingrese la respuesta que considere correcta: ")
        if x == 0:
            if respuesta == "67":
                print("Respuesta correcta")
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            nombre[cuarto+'_'+lado] = "1"
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
            else:
                print("Respuesta incorrecta")
                with open('status.json') as file:
                    data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 0.5
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            ciclo = False
                        else:
                            break
        elif x == 1:
            if respuesta == "41":
                print("Respuesta correcta")
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            nombre[cuarto+'_'+lado] = "1"
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
            else:
                print("Respuesta incorrecta")
                with open('status.json') as file:
                    data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 0.5
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            ciclo = False
                        else:
                            break
    
    def Lógica_Booleana(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        pregunta = preguntas
        x = random.randint(0,1)
        pregunta = preguntas[x]
        valor = pregunta['answer']
        print(pregunta['question'])
        respuesta = input("ingrese la opcion que considere correcta:\n1)True\n2)False\n ")
        ciclo = True
        while ciclo:
            if respuesta == "1":
                respuesta = True
                ciclo = False
                break
            elif respuesta == "2":
                respuesta = False
                ciclo = False
                break
            else:
                print("respuesta no valida")
        respuesta = str(respuesta)
        valor = str(valor)
        if respuesta == valor:
            print("Respuesta correcta")
            print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
            if premio != "":
                with open('status.json') as file:
                    data = json.load(file)
                    for nombre in data[usuario]:
                        nombre["inventario"].append(premio)
                        nombre[cuarto+'_'+lado] = "1"
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
        else:
            print("Respuesta incorrecta")
            with open('status.json') as file:
                data = json.load(file)
                for nom in data[usuario]:
                    vida2 = nom['vida']
                    float(vida2)
                    vida3  = vida2 - 0.5
                    nom["vida"] = vida3
                    with open('status.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    if nom["vida"] <= 0:
                        ciclo = False
                    else:
                        break

    def escoge_un_numero_entre(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        pregunta = preguntas
        x = random.randint(1,15)
        with open('status.json') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                pista_contador = nombre["escoge_un_numero_entre_pista"+str(1)]
                y = int(pista_contador) + 1
                if y >= 2:
                    y = 1
                pista_contador_G = nombre['pista']
                break
        pregunta = preguntas
        pista = pregunta[0]['clue_'+str(y)]
        n1 = len(pista)

        n2 = pista.find(',',0,n1)
        pista1 = pista[0:n2]
        n=n2+1
        n2 = pista.find(',',n,n1)
        pista2 = pista[n+1:n2]
        n = n2+1
        n2 = pista.find(',',n,n1)
        pista3 = pista[n+2:n2]
        n= n2+1
        #n = pista.find(',',n,n1)
        pista4 = pista[n+1:n1]
        #frase1 = pista[0:25]# Estas cerca un poco abajo
        #frase2 = pista[27:53]# Estás cerca un poco arriba
        #frase3 = pista[56:71]# estás muy abajo
        #frase4 = pista[73:91]# estás muy arriba

        print("Bienvenido al juego Escoge un número entre")
        valor = str(x)
        ciclo = True
        fallos = 0
        while ciclo:
            print(pregunta[0]['question'],"\n")
            respuesta = input("ingrese el numero que considere correcto: ")
            if respuesta == valor:
                print("Respuesta correcta")
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":    
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            nombre[cuarto+'_'+lado] = "1"
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            ciclo = False
                            break
            else:
                print("Respuesta incorrecta")
                if fallos == 3:
                    with open('status.json') as file:
                        data = json.load(file)
                        for nom in data[usuario]:
                            vida2 = nom['vida']
                            float(vida2)
                            vida3  = vida2 - 0.25
                            nom["vida"] = vida3
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            if nom["vida"] <= 0:
                                ciclo = False
                            else:
                                fallos = 0
                                break
                fallos +=1
                print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
                seleccion = input(":")
                if seleccion == "*":
                    n = int(valor) - int(respuesta)
                    if n > 0:
                        if n > 2:
                            print(pista3)
                        else:
                            print(pista1)
                    else:
                        if n < -2:
                            print(pista4)
                        else:
                            print(pista2)
                else:
                    print("valor incorrecto")
                    pass
    
    def Palabra_mezclada(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        
        x = random.randint(0,2)
        pregunta = preguntas[x]
        print("Bienvenido al juego Palabra mezclada")
        palabras = pregunta['words']
        valor = []
        guardar = True
        x = 0
        while guardar:
            valor1 = []
            for palabra in palabras[x]:
                valor1.append(palabra)
                random.shuffle(valor1)
            x+=1
            valor.append(valor1)
            if x == len(palabras):
                guardar = False
                break
        ciclo = True
        validar = [1,1,1,1,1]
        while ciclo:
            print(pregunta['question'],"\n")
            print("Categoria:",pregunta['category'])
            y = 0
            for z in range(len(palabras)):  
                desorden =valor[y]
                if validar[y] == 1:
                    print(f"{y})",*desorden)
                y+=1
            respuesta = input("ingrese la palabra ordenada que considere correcta: ")
            incorrecto = True
            n = 0
            for validacion in palabras:
                if respuesta == validacion:
                    if validar[n]==0:
                        print("Ya usted escribio esta respuesta")
                    else:
                        print("Respuesta correcta")
                        validar[n] = 0
                        if 1 in validar:
                            pass
                        else:
                            print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                            if premio != "":    
                                with open('status.json') as file:
                                    data = json.load(file)
                                    for nombre in data[usuario]:
                                        nombre["inventario"].append(premio)
                                        nombre[cuarto+'_'+lado] = "1"
                                        with open('status.json', 'w') as file:
                                            json.dump(data, file, indent=4)
                                        ciclo = False
                                        break

                    incorrecto = False
                n+=1   
                    
            if incorrecto:
                print("Respuesta incorrecta")
                with open('status.json') as file:
                    data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 0.25
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            ciclo = False
                        else:
                            break
    def Criptograma(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        
        x = random.randint(0,2)
        pregunta = preguntas[x]
        print("\nBienvenido al Criptograma\n")
        encriptado = pregunta['question']
        encriptado = encriptado.lower()


        clave = pregunta['desplazamiento']
        resultado = ""
        for letra in encriptado:
            numero = ord(letra)
            #if numero == 130:
            #    numero = 101
            #elif numero == 225:
            #    print(letra, ord(letra))
            #    numero = 160
            #elif numero == 161:
            #    numero = 105
            #elif numero == 162:
            #    numero = 111
            #elif numero == 163:
            #    numero = 117  
            
            numero += clave     
            if numero > 122 and numero != 225+clave and numero != 233+clave and numero != 237+clave and numero != 243+clave and numero != 250+clave:
                numero -=26
 
            elif numero < 97 and numero != 32+clave:
                numero += 26

            resultado += chr(numero)
        abecedario = []
        enigma = []
        separacion = []
        for n in range(97,123):
            n1 = n+ clave
            if n1 > 122:
                n1 -=26
            elif n1 < 97:
                n1 +=26
            abecedario.append(chr(n))
            enigma.append(chr(n1))
            separacion.append("|")
 
        abecedario.append("á")
        n1 = ord("á")+clave
        enigma.append(chr(n1))
        separacion.append("|")
        abecedario.append("é")
        n1 = ord("é")+clave
        enigma.append(chr(n1))
        separacion.append("|")
        abecedario.append("í")
        n1 = ord("í")+clave
        enigma.append(chr(n1))
        separacion.append("|")
        abecedario.append("ó")
        n1 = ord("ó")+clave
        enigma.append(chr(n1))
        separacion.append("|")
        abecedario.append("ú")
        n1 = ord("ú")+clave
        enigma.append(chr(n1))
        separacion.append("|")
        abecedario.append("Espacio")
        n1 = ord(" ")+clave
        enigma.append(chr(n1))
        separacion.append("|")
        #n = 1
        #for z in range(1,300):
        #    if z != 155 and z !=156  and z !=  157 and z!= 158 and z !=159:
        #        print(n,")",chr(z))
        #    n+=1
        ciclo = True
        while ciclo:
            print(*abecedario)
            print(*separacion)
            print(*enigma)
    
            print("\nDesencripta el la siguiente oracion: ", resultado)
            respuesta = input("Ingrese la oracion desencriptada: ")
    
            if respuesta == encriptado:
                print("respuesta correcta")
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":    
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            nombre[cuarto+'_'+lado] = "1"
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            ciclo = False
                            break
            else: 
                print("\nRespuesta incorrecta")
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
                            ciclo = False
                        else:
                            break

        
    
    def sopa_letras(rooms,preguntas,lado,usuario):
        class Cursor:
            def __init__(self, fila, columna):
                self.fila = fila
                self.columna = columna
                self.avanX = [-1, 0, 1][random.randint(0,2)]
                self.avanY = [-1, 0, 1][random.randint(0,2)]
                if self.avanX == 0 and self.avanY == 0:
                    self.avanX = 1
        
            def es_valido(self, dimension):
                return 0 <= self.fila < dimension and 0 <= self.columna < dimension
        
        class Matrix:
            def __init__(self, dimension):
                valores = [' '] * dimension * dimension
                self.dimension = dimension
                self.matriz = np.array(valores).reshape((dimension, dimension))
                self.libres = dimension * dimension
                self.palabras = []
        
            def __getitem__(self, cursor):
                if cursor.es_valido(self.dimension):
                    return self.matriz[cursor.fila][cursor.columna]
                else:
                    return ' '
        
            def __setitem__(self, cursor, value):
                if cursor.es_valido(self.dimension):
                    if self.matriz[cursor.fila][cursor.columna] == ' ':
                        self.libres -= 1
                    self.matriz[cursor.fila][cursor.columna] = value
        
            def __str__(self):
                regla = f"   {('0 1 2 3 4 5 6 7 8 91011121314 ' * int (self.dimension / 10 + 1))[:self.dimension * 2]}\n"
                linea = regla
                for i in range(self.dimension):
                    linea += f"{i:2d} {' '.join(self.matriz[i].tolist())}\n"
                return linea + regla

        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        x = random.randint(0,2)
        pregunta = preguntas[x]
        
        m1 = x+1
        with open('status.json') as file:
            data = json.load(file)
            for nombre in data[usuario]:
                pista_contador = nombre["sopa_letras_pista"+str(m1)]
                k = int(pista_contador)+1
                if k >= 4:
                    k = 1
                pista_contador_G = nombre['pista']
                break

        pista = pregunta['clue_'+str(k)]
        if pista_contador_G == 0:
            pista = ""
        
        print("\nBienvenido a la Sopa de Letras\n")
        palabra1 = pregunta['answer_1']
        palabra2 = pregunta['answer_2']
        palabra3 = pregunta['answer_3']
        palabra1=palabra1.lower()
        palabra2=palabra2.lower() 
        palabra3=palabra3.lower() 

        matriz = Matrix(15)
        posicion1 = [1,3,4]
        posicion2 = [2,5,1]
        
        palabras = [palabra1, palabra2, palabra3]
        posicion3 = [len(palabras[0]),len(palabras[1]),len(palabras[2])]
        posicion4 = [0,0,0]
        t=0
        for palabra in palabras:
            largo = len(palabra)
            n = 0
            x= posicion1[t]
            y=posicion2[t]
            t+=1
            while n < largo:
                cursor = Cursor(x,y)
                matriz[cursor] = palabra[n]
                n+=1
                x+=1
                y+=1
        n =97
        for x in range(0,15):
            for y in range(0,15):
                cursor = Cursor(x,y)
                campo = matriz[cursor]
                if campo == " ":
                    matriz[cursor] = chr(n)
                    n+=1
                    if n > 122:
                        n -= 26
        ciclo = True
        while ciclo:
            print(matriz)
            respuesta = ""
           
            print("\nPara pedir una pista ingrese el caracter: * (asterisco)")
            ciclo1 = True
            ciclo2 = True
            while ciclo1:
                x1 = input("colocar el numero de fila inicial de la palabra: ")
                if x1 != "*":
                    if x1.isnumeric():
                        x1 = int(x1)
                        if x1 >= 0 and x1 <=14:
                            ciclo1 = False
                    if ciclo1:
                        print("respuesta incorrecta") 
                else:
                    ciclo2 = False
                    ciclo1 =False
            if ciclo2:
                ciclo1 = True
                while ciclo1:
                    y1 = input("colocar el numero de columna inicial de la palabra: ")
                    if y1.isnumeric():
                        y1 = int(y1)
                        if y1 >= 0 and y1 <=14:
                            ciclo1 = False
                    if ciclo1:
                        print("respuesta incorrecta") 
    
                ciclo1 = True
                while ciclo1:
                    x2 = input("colocar el numero de fila final de la palabra: ")
                    if x2.isnumeric():
                        x2 = int(x2)
                        if x2 >= 0 and x2 <=14:
                            ciclo1 = False
                    if ciclo1:
                        print("respuesta incorrecta") 
    
                
                        
                ciclo1 = True
                while ciclo1:
                    y2 = input("colocar el numero de columna final de la palabra: ")
                    if y2.isnumeric():
                        y2 = int(y2)
                        if y2 >= 0 and y2 <=14:
                            ciclo1 = False
                    if ciclo1:
                        print("respuesta incorrecta") 
                entro = False
                for n in range(0,3):
                    v1 = int(posicion1[n])
                    v2 = int(posicion2[n])
                    
                    if v1 == x1 and v2 == y1:
                        
                        largo = posicion3[n]
                        
                        a1 = x1 + largo-1
                        a2 = y1 + largo-1
                        if a1 == x2 and a2 == y2:
                            if posicion4[n] == 1:
                                print("Ya usted selecciono esta palabra")
                            else:
                                
                                posicion4[n] = 1
                            entro = True
                            break
                if entro:
                    print("Respuesta correcta")
                


            gano = False
            if posicion4[0]==1 and posicion4[1] ==1 and posicion4[2] == 1:
                gano = True

            
            
            

            if x1 == "*":
                entrar = True
                if pista_contador_G != 0:
                    if nombre["sopa_letras_pista"+str(m1)] == "3":
                        print("llegaste al limite de pistas")
                        entrar = False
                        pass
                if entrar:
                    print("\n",pista)
                    grabar = False
                    if k <= 3:
                        nombre["sopa_letras_pista"+str(m1)] = str(k)
                        k += 1
                        grabar = True
                        if k <=3:
                            pista = pregunta['clue_'+str(k)]
                        if pista_contador_G >0:
                            pista_contador_G -=1
                            nombre['pista'] = pista_contador_G
                            grabar = True
                    
                
                    if grabar:
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)


                if pista_contador_G == 0:
                    pista = "Ya usted no tienes mas posibilidad de pista"
                
            elif gano:   
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            vida2 = nombre['vida']
                            float(vida2)
                            vida3  = vida2 + 1
                            nombre["vida"] = vida3
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                                ciclo = False
            elif not entro:      
                with open('status.json') as file:
                    data = json.load(file)
                    for nom in data[usuario]:
                        vida2 = nom['vida']
                        float(vida2)
                        vida3  = vida2 - 0.5
                        nom["vida"] = vida3
                        with open('status.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        if nom["vida"] <= 0:
                            ciclo = False
                        break
                print("respuesta incorrecta\n Perdiste media vida, te queda",nom['vida'])
    
    def Pipes(rooms,preguntas,lado,usuario):
        cuarto = rooms.nombre 
        objeto = rooms.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                break
        print("\nBienvenido al juego PIPES\n")
        print("(TIENES SOLO 1 MINUTO PARA TERMINAR PIPES)")
        tiempo = 2
        salida = temporizador.tiempo.cronometro(tiempo)
        



        CuadroL = ["╗","╝","╚","╔"]
        CuadroH = ["║","═"]
        
        matrizP=[
        ["█"," "," "," "," "," "," "," "," "," "],
        [CuadroL[0],CuadroH[0],CuadroH[1],CuadroH[0],CuadroH[0],CuadroL[0],CuadroH[0]," "," "," "],
        [" "," ",CuadroH[0]," ",CuadroH[1],CuadroH[1]," ",CuadroL[0]," "," "],
        [" "," ",CuadroL[1]," " ,CuadroL[3],CuadroH[0]," "," ",CuadroL[0],CuadroH[1]],
        [" ",CuadroL[1],CuadroL[2],CuadroH[1],CuadroH[1],CuadroL[3]," ",CuadroL[1]," "," "],
        [CuadroL[0],CuadroH[1],CuadroH[0]," "," ",CuadroH[0],CuadroL[0],CuadroL[3],CuadroL[0],CuadroH[0],"■■"],
        [" "," ",CuadroL[1],CuadroH[1],CuadroH[1],CuadroH[1],CuadroL[3],CuadroL[3],CuadroL[2],CuadroL[3]],
        ]
        matrizR=[
        ["█"," "," "," "," "," "," "," "," "," "],
        [CuadroL[2],CuadroH[1],CuadroH[1],CuadroH[1],CuadroH[1],CuadroL[0],CuadroH[0]," "," "," "],
        [" "," ",CuadroH[0]," ",CuadroH[1],CuadroH[0]," ",CuadroL[0]," "," "],
        [" "," ",CuadroL[1]," " ,CuadroL[3],CuadroH[0]," "," ",CuadroL[0],CuadroH[1]],
        [" ",CuadroL[1],CuadroL[3],CuadroH[1],CuadroH[1],CuadroL[1]," ",CuadroL[1]," "," "],
        [CuadroL[0],CuadroH[1],CuadroH[0]," "," ",CuadroH[0],CuadroL[3],CuadroL[0],CuadroL[3],CuadroH[1],"■■"],
        [" "," ",CuadroL[2],CuadroH[1],CuadroH[1],CuadroH[1],CuadroL[1],CuadroL[2],CuadroL[1],CuadroL[3]],
        ]
        matrizR1=[
        ["█"," "," "," "," "," "," "," "," "," "],
        [1,1,1,1,1,1,CuadroH[0]," "," "," "],
        [" "," ",CuadroH[0]," ",CuadroH[1],1," ",CuadroL[0]," "," "],
        [" "," ",CuadroL[1]," " ,CuadroL[3],1," "," ",CuadroL[0],CuadroH[1]],
        [" ",CuadroL[1],1,1,1,1," ",CuadroL[1]," "," "],
        [CuadroL[0],CuadroH[1],1," "," ",CuadroH[0],1,1,1,1,"■■"],
        [" "," ",1,1,1,1,1,1,1,CuadroL[3]],
        ]
        ciclo =True
        while ciclo:
            perdiste = temporizador.tiempo.hora_actual()
            if perdiste >= salida:
                print("Perdiste se te acabo el tiempo!!")
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
                            ciclo = False
                time.sleep(3)
                ciclo = False
                break
            count =0
            print("te queda de tiempo: ",salida - perdiste)
            print("   0 1 2 3 4 5 6 7 8 9 ")
            for mati in matrizP: 
                print(f"{count})",*mati)
                count += 1
            x = input("\nIngrese la posicion de la fila que desea seleccionar: ")
            y = input("\nIngrese la posicion de la columna que desea seleccionar: ")
            if x.isnumeric() and y.isnumeric():
                x = int(x)
                y = int(y)
                if 0 <= x <= 6 and 0 <= y <= 9:
                    if matrizP[x][y] in CuadroL:
                        print("0 1 2 3")
                        print(*CuadroL)
                        change = input("Ingrese la nueva direccion que desea ultilizar: ")
                        if change.isnumeric():
                            change = int(change)
                            if  0 <= change <=3:
                                matrizP[x][y] = CuadroL[change]
                            else:
                                print("valor incorrecto")
            
                    elif matrizP[x][y] in CuadroH:
                        print("0 1 ")
                        print(*CuadroH)
                        change = input("Ingrese la nueva direccion que desea ultilizar: ")
                        if change.isnumeric():
                            change = int(change)
                            if  0 <= change <=1:
                                matrizP[x][y] = CuadroH[change]
                            else:
                                print("valor incorrecto")
                else:
                    print("valores incorrecots")
            else:
                print("no son numericos")

            entro = True
            for f in range(0,7):
                for c in range(0,10):
                    if matrizR1[f][c] == 1:
                        if matrizR[f][c]!=matrizP[f][c]:
                            entro = False
                            
                            
            if entro:
                print("respuesta correcta")
                print("Felicidades Ganaste!!(en el inventario veras las recompensas)")
                if premio != "":    
                    with open('status.json') as file:
                        data = json.load(file)
                        for nombre in data[usuario]:
                            nombre["inventario"].append(premio)
                            nombre[cuarto+'_'+lado] = "1"
                            with open('status.json', 'w') as file:
                                json.dump(data, file, indent=4)
                ciclo = False
                
            
    
    
            
    
    
    
    
        


