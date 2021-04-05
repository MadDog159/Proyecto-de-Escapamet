import datetime

class tiempo():

    def cronometro(tiempos):
        hoy = datetime.datetime.now()

        hora_entrada = datetime.datetime(hoy.year, hoy.month, hoy.day, hoy.hour, hoy.minute, hoy.second)

        valor = hora_entrada.minute + tiempos
        valor1 = hora_entrada.hour
        valor2 = hora_entrada.day
        valor3 = hora_entrada.month
        if valor >= 60:
            valor -= 60
            valor1 = hora_entrada.hour+1
        if valor1 >23:
            valor1 = 0
            valor2 = hora_entrada.day+1
        if valor2 > 31:
            valor2 = 1
            valor3 = hora_entrada.month+1
        
        hora_salida = datetime.datetime(hoy.year, month= valor3, day= valor2, hour=valor1, minute=valor, second=hora_entrada.second)
        #hora_salida = datetime.datetime(hoy.year, hoy.month, hoy.day, hour=valor1, minute=valor, second=hora_entrada.second)
        return hora_salida
    def tiempo_partida_guardada(tiempos, segundos):
        hoy = datetime.datetime.now()

        hora_entrada = datetime.datetime(hoy.year, hoy.month, hoy.day, hoy.hour, hoy.minute, hoy.second)

        val = hora_entrada.second + segundos
        valor = hora_entrada.minute + tiempos
        valor1 = hora_entrada.hour
        valor2 = hora_entrada.day
        valor3 = hora_entrada.month
        
        if val >= 60:
            val -= 60
            valor += 1
        if valor >= 60:
            valor -= 60
            valor1 = hora_entrada.hour+1
        if valor1 >23:
            valor1 = 0
            valor2 = hora_entrada.day+1
        if valor2 > 31:
            valor2 = 1
            valor3 = hora_entrada.month+1
        
        hora_salida = datetime.datetime(hoy.year, month= valor3, day= valor2, hour=valor1, minute=valor, second=val)
        #hora_salida = datetime.datetime(hoy.year, hoy.month, hoy.day, hour=valor1, minute=valor, second=hora_entrada.second)
        return hora_salida
    
    def hora_actual():
        hora  = datetime.datetime.now()
        hora_actual = datetime.datetime(hora.year, hora.month, hora.day, hora.hour, hora.minute, hora.second)
        return hora_actual

 


