from jugador import Jugador
import datetime
class ManejadorJugador:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    
    def AgregarJugador(self,unJugador):
        self.__lista.append(unJugador)

    def Iniciar(self):
        nombre=input('Ingrese el nombre del jugador:')
        dni=input('Ingrese el dni del jugador:')
        ciudad=input('Ingrese la ciudad del jugador:')
        pais=input('Ingrese el pais del jugador:')
        print('Para la fecha de nacimiento ingrse:')
        dia=input('Dia:')
        mes=input('Mes:')
        anio=input('Anio:')
        fechadenacimiento=datetime.date(int(anio),int(mes),int(dia))
        unJugador=Jugador(nombre,dni,ciudad,pais,fechadenacimiento)
        self.AgregarJugador(unJugador)
    
    def BuscarJugador(self,jugador):
        i=0
        ret=None
        while self.__lista[i].getDNI()!=jugador:
            i+=1
        if self.__lista[i].getDNI()==jugador:
            ret=i
        else: ret=-1
        return ret
    
    def getLista(self):
        return self.__lista
    