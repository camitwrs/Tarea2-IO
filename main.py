# SRFLP con Algoritmo Genetico.

from src.SRFLP import SRFLP
from src.AlgoritmoGenetico import AlgoritmoGenetico
from prettytable import PrettyTable

def mostrar_menu_instancia():
    print("\n-----------------------------")
    print("     Elija la instancia:")
    print("-----------------------------")
    print("     1) QAP_sko56_04_n.txt")
    print("     2) QAP_sko100_04_n.txt")
    print("-----------------------------\n")

    opcion = input('Instancia elegida: ')
    return opcion


# ------------------------------------ MAIN --------------------------------------------

# Leer e interpretar el problema leido desde la instancia definida
opcion = mostrar_menu_instancia()
if(opcion == '1'):
  problem = SRFLP(nombre_archivo="QAP_sko56_04_n.txt")
elif(opcion == '2'):
  problem = SRFLP(nombre_archivo="QAP_sko100_04_n.txt")
else:
  print('No hay más opciones de instancias por ahora.')

# Verificar si leyó bien la instancia
problem.imprimir_instancia()

