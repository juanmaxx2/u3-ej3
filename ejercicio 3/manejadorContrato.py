from contrato import Contrato
import numpy as np
import csv
class ManejadorContrato:
    __Cantidad=0
    __Dimension=0
    __Incremento=5

    def __init__(self,dimension=5):
        self.__Contrato=np.empty(dimension,dtype=Contrato)
        self.__Cantidad=0
        self.__Dimension=dimension

    def AgregarContrato(self,unContrato):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__Contrato.rezise(self.__Dimension)
        self.__Contrato[self.__cantidad]=unContrato
        self.__cantidad+=1
    
    def Iniciar(self):
        archivo=open('contratos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unContrato=Contrato(fila[0],fila[1],fila[2])
                self.AgregarContrato(unContrato)
        archivo.close()