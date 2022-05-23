class Contrato:
    __FechaI=None
    __FechaF=None
    __Pago=None
    __Equipo=None
    __Jugador=None
    
    def __init__(self,FechaI,FechaF,Pago):
        self.__FechaI=FechaI
        self.__FechaF=FechaF
        self.__Pago=Pago