import json


class cuartos:

    def __init__(self,nombre,objeto):
        self.nombre = nombre
        self.objeto = objeto


    def cuarto_objetos(self):
        linea1 = ""
        linea2 = ""
        linea3 = ""
        cuarto = self.nombre
        print(cuarto)
        objeto = self.objeto
        for lugar in objeto:
            if lugar['position']== "left":
                linea1 ="(1)",lugar['position'],":",lugar['name'] 
            elif lugar['position']== "center":
                linea2 ="(2)",lugar['position'],":",lugar['name'] 
            elif lugar['position']== "right":
                linea3 ="(3)",lugar['position'],":",lugar['name'] 
        print(*linea1)
        print(*linea2)
        print(*linea3)
    
        if cuarto == 'Biblioteca':
            print("(4) Plaza Rectorado\n(5) Puerta Laboratorios\n(p) Inventario")

        elif cuarto == 'Laboratorio SL001':
            print("(4) Biblioteca\n(5) Cuarto de Servidores\n(p) Inventario")

        elif cuarto == 'Plaza Rectorado':
            print("(4) Biblioteca\n(p) Inventario")

        elif cuarto == 'Pasillo Laboratorios ':
            print("(4) Biblioteca\n(p) Inventario")
        
        elif cuarto == 'Cuarto de Servidores ':
            print("(4) Laboratorio SL001\n(p) Inventario")
    
    def cuarto_regla(self,lado):
        objeto = self.objeto
        for lugar in objeto:
            if lugar['position']== lado:
                juegos = lugar['game']
                premio = juegos['award']
                regla = juegos["rules"]
                actividad = juegos['name']
                print("Si completas este nivel te ganas: ",premio)
                print("Regla del juego: ",regla)
                print("El Juego es: ", actividad)
                break
    
            

                
              
