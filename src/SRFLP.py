import os
import random

# SRFLP: Problema de ubicación de instalaciones con restricciones de tamaño.
class SRFLP():
  
  # Constructor de la clase. Toma como argumento el nombre de un archivo, que contiene los datos del problema.
  def __init__(self, nombre_archivo):
    # Nombre del archivo de instancia
    self.nombre = nombre_archivo
    # Numero de instalaciones (inicialmente -1 antes de leer)
    self.n = -1
    # Lista de tamaños de las instalaciones
    self.tam_instal = []
    # Matriz de pesos entre las instalaciones i,j. 
    self.peso_instal = []
    
    if not os.path.isfile(nombre_archivo):
            print(f"No se puede leer el archivo {nombre_archivo}")
            exit(1)

    self.leer_srflp(nombre_archivo)
  
  # Lee un archivo que contiene información sobre las instalaciones: el número de instalaciones, los tamaños de las instalaciones y
  # los pesos entre las instalaciones, y almacena esta información en la instancia de la clase.
  def leer_srflp(self, nombre_archivo):
    i = -1
    
    if(nombre_archivo == None):
      print("Instancia no especificada, abortando...")
      exit(1)
      
    print(f"\nLeyendo archivo {nombre_archivo} ... ")
    
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        lineas = file.readlines()
        
        for linea in lineas:
          linea = linea.strip()
          if linea == "EOF":
            break
          if linea.startswith("#"):
            continue
          
          if self.n < 0:
            # Primera lineaa número de instalaciones
            self.n = int(linea)
          elif i == -1:
            # Segunda lineaa tamaño de instalaciones
            valores_linea = linea.split(",")
            for k in range(self.n):
              self.tam_instal.append(int(valores_linea[k].strip()))
            i = 0
          else:
            valores_linea = linea.split(",")
            self.peso_instal.append([])  # Añade una nueva lista vacía en self.peso_instal[i]
            for k in range(self.n):
              self.peso_instal[i].append(int(valores_linea[k].strip()))
            i += 1
  
  
  # Imprime el número de instalaciones, los tamaños de las instalaciones y los pesos entre las instalaciones de una instancia
  def imprimir_instancia(self):
    print(f"Numero de instalaciones: {self.n}")
    
    print("Tamaños: ", end="")
    # Imprime la lista de tamaños de las instalaciones
    for k in range(self.n):
        print(f"{self.tam_instal[k]} ", end="")
        
    print("\nPesos: ")
    # Imprime la matriz de pesos
    for i in range(self.n):
        for k in range(self.n):
            print(f"{self.peso_instal[i][k]} ", end="")
        print() 
  
  # Devuelve el tamaño de instalaciones del problema
  def obtener_tam_problema(self):
    return self.n
  
  # Devuelve el peso correspondiente de peso_instal.
  # Verifica si los índices i y j están dentro del rango válido, y si no, imprime un mensaje de error y termina el programa.
  def obtener_peso(self, i, j):
    if i >= self.n or i < 0 or j >= self.n or j < 0:
        print(f"Error no existe el puesto {i} o {j} fuera de rango")
        exit(1)
    return self.peso_instal[i][j]
  
  # Devuelve el tamaño correspondiente de tam_instal.
  # Verifica si el índice i está dentro del rango válido, y si no, imprime un mensaje de error y termina el programa. 
  def obtener_tam_instal(self, i):
    if i >= self.n or i < 0:
        print(f"Error no existe el puesto {i} fuera de rango")
        exit(1)
    return self.tam_instal[i]
  
  # Crea una solucion random desde la instancia, no entrega soluciones duplicadas
  def crear_solucion_inicial(self):
    instalaciones = list(range(self.n))
    solucion = []

    for i in range((self.n)):
        nodo = random.randrange(len(instalaciones))
        solucion.append(instalaciones.pop(nodo))
    return solucion    

  # FUNCION OBJETIVO
  # Calcula y devuelve el esfuerzo requerido de una solución (array) proporcionado.
  # Indice de array comienza desde el 0
  def obtener_esfuerzo(self, sol):
    distancia_total = 0.0
    esfuerzo_total = 0.0
    tam_sol = len(sol)
    for i in range(tam_sol - 1):
        p1 = sol[i] 
        distancia_media = 0.0
        for j in range(i + 1, tam_sol):
            p2 = sol[j]
            distancia_total = self.tam_instal[p1] / 2 + distancia_media + self.tam_instal[p2] / 2
            distancia_media += self.tam_instal[p2]
            esfuerzo_total += distancia_total * self.obtener_peso(i, j)
    return esfuerzo_total
  


  
            


    

    