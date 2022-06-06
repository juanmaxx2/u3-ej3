from manejadorContrato import ManejadorContrato
from manejadorJugador import ManejadorJugador
from manejadorEquipo import ManejadorEquipo
class Menu:
    __opcion=None

    def __init__(self):
        self.__opcion=None
    
    def Iniciar(self):
        unManejadorC=ManejadorContrato()
        unManejadorJ=ManejadorJugador()
        unManejadorE=ManejadorEquipo()
        unManejadorE.Iniciar()
        while self.__opcion!='6':
            print('\n1.Para Crear un jugador')
            print('2.Para crear un Contrato')
            print('3.Buscar jugador por contrato')
            print('4.Buscar jugadores que se les vence el contrato dentro de 6 meses')
            print('5.Para obtener el importe de todos los contratos de un equipo')
            print('6.Salir')
            self.__opcion=input('Ingrese la opcion a realizar:')

            if self.__opcion=='1':
                unManejadorJ.Iniciar()

            elif self.__opcion=='2':
                jugador=input('\nIngrese el DNI del jugador a realizar el contrato:')
                i=unManejadorJ.BuscarJugador(jugador)
                if i==-1:
                    print('No existe el jugador')
                else:
                    equipo=input('Ingrese el nombre del equipo para el jugador:')    
                    j=unManejadorE.BuscarEquipo(equipo)
                    if j==-1:
                        print('No se encontro el equipo')
                    else:
                        unManejadorC.Iniciar(unManejadorJ.getLista()[i],unManejadorE.getLista()[j])

            elif self.__opcion=='3':
                dni=input('\nIngrese el DNI del jugador:')
                unManejadorC.BuscarporDNI(dni)

            elif self.__opcion=='4':
                equipo=input('Ingrese el indice de un equipo')
                unManejadorC.VencimientodeContrato(equipo)
                
            elif self.__opcion=='5':
                equipo=input('Ingrese el nombre')
                unManejadorC.BuscarContratos(equipo)