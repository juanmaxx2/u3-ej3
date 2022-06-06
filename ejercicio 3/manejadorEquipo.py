from equipo import Equipo
import numpy as np
import csv
class ManejadorEquipo:
    __Cantidad=0
    __Dimension=0
    __Incremento=5

    def __init__(self,dimension=5):
        self.__Equipo=np.empty(dimension,dtype=Equipo)
        self.__Cantidad=0
        self.__Dimension=dimension

    def AgregarEquipo(self,unEquipo):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__Equipo.rezise(self.__Dimension)
        self.__Equipo[self.__Cantidad]=unEquipo
        self.__Cantidad+=1

    def Iniciar(self):
        archivo=open('equipos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unEquipo=Equipo(fila[0],fila[1],fila[3])
                self.AgregarEquipo(unEquipo)
        archivo.close()

    def BuscarEquipo(self,unEquipo):
        i=0
        ret=None
        while unEquipo!=self.__Equipo[i].getNombre():
            i+=1
        if unEquipo==self.__Equipo[i].getNombre():
            ret=i
        else: ret=-1
        return ret
    
    def getLista(self):
        return self.__Equipo