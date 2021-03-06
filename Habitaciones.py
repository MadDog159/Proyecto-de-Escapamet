import json
import random




Puerta_Laboratorio_C = '''
  ---------------------PASILLO LABORATORIO-----------------------
  |     |                                                 |    |
  |     |          ____________________                   |    |
  |     |         |                    |                  |    |
  |     |         |   P.laboratorios   |                  |    |
  |     |         |                    |                  |    |
  |     |         |                    |                  |    |
  |     |         | O                  |                  |    |
  |     | 3 = C   |                    |                  |    |
  |_____|___      |                    |                  |    |
  |        /|_____|____________________|__________________|    |
  |_ _ _ _/ |                                             \    |
  |       |=@                                              \   |
  |       |/|                                               \  |
  |       |=@                                                \ |
  |/______|_/_________________________________________________\|

  Esas frente a la puerta
  '''
Puerta_Laboratorio_A = '''
  --------------------PASILLO LABORATORIO------------------------
  |     |                                                 |    |
  |     |         ____________________   __      5 = A    |    |
  |     |        || |___________|_____|||\  \             |    |
  |     |        ||/                  | | \  \            |    |
  |     |        |/                   | |  \  \           |    |
  |     |        |                    |||   \ _\          |    |
  |     |        |                    | |    |  |         |    |
  |     |        |                    | |    |  |         |    |
  |_____|___     |                    | |    |  |         |    |
  |        /|____|____________________|||    |  |=@_______|    |
  |_ _ _ _/ |                            \   |  |         \    |
  |       |=@                             \  |  |          \   |
  |       |/|                              \ |  |           \  |
  |       |=@                               \|__|            \ |
  |/______|_/_________________________________________________\|

  La puerta esta abierta
  '''



Biblioteca = '''
  -------------------------------------BIBLIOTECA--------------------------------------
  |      |                                                                    |       |
  |      |                   _//|_//|__ //|____                    2 = B      ||\     |
  |      |                  / ||/ ||/  ||/    /|          ____________        || \    |
  |      |                 /_________________/||        /____________/|       ||  |   |
  |      |/\                |||___________|||_||        |  o  |  o  | |       ||  |   |
  |      / /|               |||___________|||/||        |_____|_____| |       ||* |   |
  |     / / |____           |||___________|||_||        |  o  |  o  | |       ||  |   |
  |    /\/  /   /|__________|||___________|||/_|________|_____|_____| |_______||  |   |
  |   |  | /   / /          |_|           |_|           |___________|/         \  |   |
  |   |  |/___/ /                                           P.laboratios-->     \ |   |
  |   |       |/                                                                 \|   |
  |   |______/                              Saman                                 \   |
  |  /                                      ||                                     \  |
  | /                                       \/                                      \ |
  |/_____________________________/___________|__________\____________________________\|

Estas en el medio de la Biblioteca
'''
Plaza_Rectorado = """
  -------------------------------------PLAZA RECTORADO-------------------------------------
  |    - |      | -            _____  ____  ____                                          |
  |     - \____/ -            /     \/    \/    \                                         |
  |      / | | | \            \_____/\____/\____/                                         |
  |                                     __________________                                |                  
  |_______                             /                  \                               |   
  |______ \                           |                    |                              |    
  |___   \ \                           \                  /                               |    
  | /|__  | |                           \_____      _____/                                |            
  |/ / /|_|/            ____                  |    |                _____                 |        
  | / / /              /   /| ________________|    |______________ |\    \                |                  
  |/ / /<-biblioteca  /   /   /  1 = P        |    |              \  \    \               |      
  | / /              /___/   /                |    |               \  \____\              |           
  |/ /               |___|  /           _________  __________       \  |___|              |         
  | /                      /___________/________/|/_________/|_______\                    |                                             
  |/                                   ||     ||  ||      ||                              |    
  |                                                                                       |    
  |                                                                                       |    
  |_______________________________________________________________________________________|  
  
  Estas en el medio de la plaza                                                                        
"""
Laboratorios_SL001 = """

  -------------------------------------laboratorios_SL001------------------------------
  |       |                          ____\ __|__ /____                        |       |
  |       |                         |    -|_____|-    |                       |       |
  |   /|  |                         |    /       \    |                       |       |
  |  / |  |      _______            | 4 = L           |       _______         |  |\   |
  | /  |  |    _|| pc1 ||____       |_________________|     _|| pc2 ||____    |  | \  |
  | |  |  |   |\||_____||--< \      /_________________/    |\||_____||--< \   |  |  \ |
  | |  |  |   ||\_____________\                            ||\_____________\  |  |  | |
  | | *|  |___||_||_______||_||____________________________||_||_______||_||__|  |* | |
  | |  | /       ||          ||                               ||          ||   \ |  | |
  | |  |/        ||          ||                               ||          ||    \|  | |
  | |  /                                                                         \  | |
  | | / <--P.laboratorios                                                         \ | |
  | |/                                                                             \| |
  | /                                                                               \ |
  |/_________________________________________________________________________________\|

Estas en el medio de la habitacion
"""

Cuarto_de_Servidores = """
  ---------------------------------CUARTO DE SERVIDORES--------------------------------
  |       |          _______________                                           |      |
  |       |         / ::::::       /|      ____________                        |      |
  |   /|  |        / ::::::  6 = S/ |     |            |     ________________  |      |
  |  / |  |       /______________/ <|     |            |    |\  :::::::::::  \ |      |
  | /  |  |      |        ____   | <|     |o           |    | \  :::::::::::  \|      |
  | |  |  |      |       | >< |  | <|     |            |    |  \ ______________\      |
  | |  |  |      |       |____|  |/ |     |            |    | |\|         ><>< |  |\  |
  | | *|  |______| ___         : |/ /_____|____________|____<==||         ><>< |====| |
  | |  | /       | ---.        : |//                        | \|| -------|\<>< |====| |
  | |  |/        |_______________|/                         \-.:| --_____| \-O |====| |
  | |  /                                                     \ :| -|\   |\ |   | \ \| |
  | | / <--P.laboratorios                                     \ | -| \__|_\|   |  \   |
  | |/                                                         \|__| |    |____|   \  |
  | /                                                               \|____|         \ |
  |/_________________________________________________________________________________\|

Estas en el medio de la habitacion
"""

