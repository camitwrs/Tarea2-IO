# SRFLP con Algoritmo Genetico.
# Integrantes: Camila Torres, Jan Houter.

import statistics
from prettytable import PrettyTable
from src.SRFLP import SRFLP
from src.AlgoritmoGenetico import AlgoritmoGenetico

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
  solver = AlgoritmoGenetico(instancia=problem, seleccion_padres="elitista", tipo_cruzamiento="ordenado", tipo_mutacion="swap", estrategia="mulambda", seleccion_poblacion="elitista", tam_poblacion=50, tam_descendencia=100, prob_mutacion=0.3)
  
  valores_optimos = []
  for i in range(1,10+1): 
    print(f"===> EJECUCION: {i}")
    solver.ejecucion(max_iteraciones=30)
    valores_optimos.append(solver.obtener_optimo())
    print("---------------------------")
  
  # Crear tabla 
  tabla = PrettyTable(["Ejecución", "f(x)"])
  for i, valor in enumerate(valores_optimos, 1):
    tabla.add_row([i, valor])
  print(tabla)
  
  media = statistics.mean(valores_optimos)
  desviacion_estandar = statistics.stdev(valores_optimos)
  
  print(f'Media: {media}')
  print(f'Desviacion Estandar: {desviacion_estandar}')
  
    
elif(opcion == '2'):
  
  problem = SRFLP(nombre_archivo="QAP_sko100_04_n.txt")
  solver = AlgoritmoGenetico(instancia=problem, seleccion_padres="elitista", tipo_cruzamiento="ordenado", tipo_mutacion="swap", estrategia="mulambda", seleccion_poblacion="elitista", tam_poblacion=50, tam_descendencia=100, prob_mutacion=0.3)
  
  valores_optimos = []
  for i in range(1,10+1): 
    print(f"===> EJECUCION: {i}")
    solver.ejecucion(max_iteraciones=30)
    valores_optimos.append(solver.obtener_optimo())
    print("---------------------------")
  
  # Crear tabla 
  tabla = PrettyTable(["Ejecución", "f(x)"])
  for i, valor in enumerate(valores_optimos, 1):
    tabla.add_row([i, valor])
  print(tabla)
  
  media = statistics.mean(valores_optimos)
  desviacion_estandar = statistics.stdev(valores_optimos)
  
  print(f'Media: {media}')
  print(f'Desviacion Estandar: {desviacion_estandar}')
  
else:
  print('No hay más opciones de instancias por ahora.')




