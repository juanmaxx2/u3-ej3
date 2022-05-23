from jugador import Jugador
import csv
class ManejadorJugador:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    
    def Iniciar(self):
        archivo=open('jugadores.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unJugador=Jugador(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(unJugador)
        archivo.close()
