from src.SRFLP import SRFLP
import random

# Referencias: Pseudocodigo Aula - Leslie Perez

class AlgoritmoGenetico():
  # Variables de constructor (no se utilizan todas)
  def __init__(self, instancia, seleccion_padres, tipo_cruzamiento, tipo_mutacion, estrategia, seleccion_poblacion, tam_poblacion, tam_descendencia, prob_mutacion):
    self.instancia = instancia
    self.seleccion_padres = seleccion_padres
    self.tipo_cruzamiento = tipo_cruzamiento
    self.tipo_mutacion = tipo_mutacion
    self.estrategia = estrategia
    seleccion_poblacion = seleccion_poblacion
    self.tam_poblacion = tam_poblacion
    self.tam_descendencia = tam_descendencia
    self.prob_mutacion = prob_mutacion
    self.mejores_soluciones = []
    print("Iniciando Algoritmo Genetico...")

  # Genera una población inicial de soluciones para el algoritmo genético, solo utiliza el tamaño de la poblacion para ello.
  def generar_poblacion_inicial(self):
    pob = []
    for i in range(self.tam_poblacion):
      pob.append(self.instancia.crear_solucion_inicial()) 
    return pob
  
  # Tipo: ELITISTA (minimizacion)
  # Selecciona los mejores individuos de una población, ordenándolos de menor a mayor según su esfuerzo (asumiendo que un menor esfuerzo es mejor), y devuelve la cantidad especificada de los mejores individuos
  def seleccionar_mejores(self, pob, cantidad):
    pob_mayor_a_menor = sorted(pob, key=lambda individuo: self.instancia.obtener_esfuerzo(individuo))
    mejores_individuos = pob_mayor_a_menor[:cantidad]
    
    return mejores_individuos
  
  # Tipo: SWAP
  # Realiza una mutación de intercambio en dos individuos h1 y h2. Si un número aleatorio es menor que la probabilidad de mutación, intercambia dos genes aleatorios en el individuo. Devuelve los individuos mutados.
  def mutacion(self, h1, h2):
    mutados = []
    
    rand1 = random.random()   
    if rand1 < self.prob_mutacion:
      gen1, gen2 = random.sample(range(len(h1)), 2)
      h1[gen1], h1[gen2] = h1[gen2], h1[gen1]
      
    rand2 = random.random()
    if rand2 < self.prob_mutacion:
      gen1, gen2 = random.sample(range(len(h2)), 2)
      h2[gen1], h2[gen2] = h2[gen2], h2[gen1]
    
    mutados.append(h1)
    mutados.append(h2)
    
    return mutados
  
  # Realiza un cruce ordenado entre dos padres p1 y p2. Mantiene una subsecuencia de cada padre en los hijos y llena los espacios restantes con genes del otro padre en el orden en que aparecen. Devuelve los hijos cruzados.
  def cruzamiento_ordenado(self, p1, p2):
    hijos_cruzados = []
    
    corte1, corte2 = sorted(random.sample(range(self.instancia.obtener_tam_problema()), 2))
    
    h1 = [None]*len(p1)
    h1[corte1:corte2] = p1[corte1:corte2]
    
    for ind, item in enumerate(p2):
          if item not in h1:
            for i in range(self.instancia.obtener_tam_problema()):
              if h1[i] is None:
                h1[i] = item
                break
              
    # Mantiene los elementos entre start y end del segundo padre
    h2 = [None]*len(p2)
    h2[corte1:corte2] = p2[corte1:corte2]
    # Llena los espacios restantes con los genes del primer padre en el orden en que aparecen
    for ind, item in enumerate(p1):
      if item not in h2:
        for i in range(self.instancia.obtener_tam_problema()):
          if h2[i] is None:
              h2[i] = item
              break
    
    hijos_cruzados.append(h1)
    hijos_cruzados.append(h2)
    
    return hijos_cruzados
  
  # Devuelve el esfuerzo asociado con la última solución en la lista de las mejores soluciones. El esfuerzo se calcula utilizando la instancia actual del problema.
  def obtener_optimo(self):
    tam = len(self.mejores_soluciones)
    ultima_solucion = self.mejores_soluciones[tam-1]
    esfuerzo = self.instancia.obtener_esfuerzo(ultima_solucion)
    return esfuerzo

  # Implementacion del algoritmo genetico.   
  # Genera una población inicial y luego entra en un bucle donde selecciona padres, realiza el cruce y la mutación, y selecciona la próxima generación. 
  # Este proceso se repite por un número máximo de iteraciones. La función mantiene un registro de las mejores soluciones encontradas en cada generación y al final imprime el esfuerzo asociado con la última mejor solución.
  def ejecucion(self, max_iteraciones) -> None:
    print("Generando la poblacion inicial ...")
    # Creando la poblacion inicial
    poblacion = self.generar_poblacion_inicial()
    mejor_sol = self.seleccionar_mejores(poblacion, 1)
    self.mejores_soluciones.append(mejor_sol)
      
    # Bucle generaciones/iteraciones
    print('Comenzando la busqueda...')
    iteracion = 1
    while(iteracion <= max_iteraciones):
      print(f'GENERACION {iteracion} DE {max_iteraciones}')
      descendencia = []
      #descendencia.clear()
      
      # Bucle descendencia (Conmentarios analogos al Pseudocodigo)
      while(len(descendencia) < self.tam_poblacion):
        # seleccionar individuos(G,2)
        lista_padres = self.seleccionar_mejores(poblacion, 2)
        padre1 = lista_padres[0]
        padre2 = lista_padres[1]
        
        # cruzar individuos(p1, p2)
        lista_hijos = self.cruzamiento_ordenado(padre1, padre2)
        hijo1 = lista_hijos[0]
        hijo2 = lista_hijos[1]
        
        # mutar(h1, h2)
        lista_mutados = self.mutacion(hijo1, hijo2)
        mutado1 = lista_mutados[0]
        mutado2 = lista_mutados[1]
        
        # G∗ + S
        descendencia.append(mutado1)
        descendencia.append(mutado2)
      
      # MU,LAMBDA
      poblacion = self.seleccionar_mejores(descendencia, self.tam_poblacion)
      # Como va a estar ordenado, el de la izquierda (index 0) siempre será el mejor
      mejor_sol = poblacion[0]
      print(f"Mejor solución: {self.instancia.obtener_esfuerzo(mejor_sol)}")
      self.mejores_soluciones.append(mejor_sol)

      iteracion += 1
    
    print(f"Distribucion: ")
    print(self.mejores_soluciones[len(self.mejores_soluciones)-1])
    
   
      
    
    
      
      
    
    
      
      