class Contrato:
    __FechaI=None
    __FechaF=None
    __Pago=None
    __Equipo=None
    __Jugador=None
    
    def __init__(self,FechaI,FechaF,Pago,Equipo,Jugador):
        self.__FechaI=FechaI
        self.__FechaF=FechaF
        self.__Pago=Pago
        self.__Equipo=Equipo
        self.__Jugador=Jugador
    
    def getFechaI(self):
        return self.__FechaI
    def getFechaF(self):
        return self.__FechaF
    def getPago(self):
        return self.__Pago
    def getEquipo(self):
        return self.__Equipo
    def getJugador(self):
        return self.__Jugador