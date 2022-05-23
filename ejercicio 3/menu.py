from manejadorContrato import ManejadorContrato
from manejadorJugador import ManejadorJugador
from manejadorEquipo import ManejadorEquipo
class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=None
    
    def Iniciar(self):
        unManejadorC=ManejadorContrato()
        unManejadorC.Iniciar()
        unManejadorJ=ManejadorJugador()
        unManejadorJ.Iniciar()
        unManejadorE=ManejadorEquipo()
        unManejadorE.Iniciar()
        while self.__opcion!='4':
            print()
            print()
            print()
            print('4')
            self.__opcion=input('Ingrese la opcion a realizar:')

            if self.__opcion=='1':

            elif self.__opcion=='2':

            elif self.__opcion=='3':