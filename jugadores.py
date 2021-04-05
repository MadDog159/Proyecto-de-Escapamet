import json
from time import tzname
class Jugador():

    def __init__(self,usuario,password,edad):
        self.usuario = usuario
        self.password = password
        self.edad = edad

    def buscar_usuario(self):
        salir = False
        if self.usuario !="":
            with open('data.json') as file:
                data = json.load(file)
                if len(data)>0:
                    for usuarios in data['usuarios']:
                        if usuarios['nombre'] == self.usuario:
                            salir = True
                            break
        return salir

    def validar_contrasena(self, password):
        salir = False
        with open('data.json') as file:
            data = json.load(file)
            for usuarios in data['usuarios']:
                if usuarios['nombre'] == self.usuario:
                    if usuarios['password']== password:
                        salir = True
                        with open('data.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        break
        return salir
    

class puntuaciones(Jugador):

    def __init__(self, dificultad, personaje, tiempo, usuario, password, edad):
        super().__init__(usuario, password, edad)
        self.dificultad = dificultad
        self.personaje = personaje
        self.tiempo = tiempo
        
    def Base_datos_records(self):
    
        with open('status.json') as file:
            data = json.load(file)
        for nombre in data[self.usuario]:
            s = nombre
        with open('records.json') as file:
            data = json.load(file)
            data1 ={}
            with open('records.json', 'w') as file:
                json.dump(data1, file, indent=4)
            usu = self.usuario    
            if usu in data:
                pass
            else:
                data2 ={usu:[]}
                #data={usu:[]}
                data.update(data2)
            data[usu].append([
                {
                'personaje': self.personaje,
                'tiempo': self.tiempo,
                'dificultad': self.dificultad,
                'Biblioteca':nombre['contador_Biblioteca'] ,
                "Laboratorio SL001": nombre['contador_Laboratorio SL001'],
                "Plaza Rectorado": nombre['contador_Plaza Rectorado'],
                "Pasillo Laboratorios ": nombre['contador_Pasillo Laboratorios '],
                "Cuarto de Servidores ": nombre['contador_Cuarto de Servidores ']
                }
                ])
            with open('records.json', 'w') as file:
                json.dump(data, file, indent=4)
    


    