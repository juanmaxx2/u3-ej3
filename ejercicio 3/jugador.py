class Jugador:
    __Nombre=None
    __DNI=None
    __Ciudad=None
    __Pais=None
    __FechaNacimiento=None

    def __init__(self,Nombre,DNI,Ciudad,FechaNacimiento,Pais):
        self.__Nombre=Nombre
        self.__DNI=DNI
        self.__Ciudad=Ciudad
        self.__Pais=Pais
        self.__FechaNacimiento=FechaNacimiento
    
    def getNombre(self):
        return self.__Nombre
    def getDNI(self):
        return self.__DNI