from contrato import Contrato
import numpy as np
import datetime
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
    
    def Iniciar(self,jugador,equipo):
        print('Ingrese la informacion del contrato:')
        print('para el inicio del contratro:')
        diaI=input('Dia de inicio:')
        mesI=input('Mes de inicio:')
        anioI=input('Anio de inicio:')
        print('Para el Final del contrato:')
        diaF=input('Dia de finalizacion:')
        mesF=input('Mes de finalizacion:')
        anioF=input('Anio de finalizacion:')
        FechaI=datetime.date(int(anioI),int(mesI),int(diaI))
        FechaF=datetime.date(int(anioF),int(mesF),int(diaF))
        pago=input('Ingrese el pago mensual:')
        unContrato=Contrato(FechaI,FechaF,pago,equipo,jugador)
        self.AgregarContrato(unContrato)
        jugador.AgregarContrato(unContrato)
        equipo.AgregarEquipo(unContrato)
    
    def BuscarporDNI(self,dni):
        i=0
        while dni!=self.__Contrato[i].getJugador().getDNI() and i<len(self.__Contrato):
            i+=1
        if dni==self.__Contrato[i].getJugador().getDNI():
            print('El nombre del equipo es:{}'.format(self.__Contrato[i].getEquipo().getNombre()))
        else:print('No existe ese jugador')
    
    def VencimientodeContrato(self,Equipo):
        for i in range(len(self.__Contrato)):
            if Equipo==self.__Contrato[i].getEquipo().getID():
                fecha=datetime.date.today()
                fecha.month+=6
                if fecha>=self.__Contrato[i].getFechaF():
                    print(self.__Contrato[i].getJugador().getNombre())
    
    def BuscarContratos(self,Equipo):
        c=0
        for i in range(len(self.__Contratos)):
            if Equipo==self.__Contratos[i].getEquipo().getNombre():
                c+=self.__Contratos[i].getPago()
        print ('EL importe total de los contratos es:{}'.format(c))