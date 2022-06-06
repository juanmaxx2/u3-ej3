class Equipo:
    __Id=None
    __Nombre=None
    __Ciudad=None
    __Contrato=None

    def __init__(self,Id,Nombre,Ciudad):
        self.__Id=Id
        self.__Nombre=Nombre
        self.__Ciudad=Ciudad
        self.__Contrato=[]

    def AgregarContrato(self,jugador):
        self.__Contrato.append(jugador)
    def getID(self):
        return self.__Id
    def getNombre(self):
        return self.__Nombre
    def getCiudad(self):
        return self.__Ciudad