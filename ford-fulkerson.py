# Esta clase representa un Grafo dirigido usando una Matriz de adyecencia
class Grafo:

    def __init__(self, grafo):
        self.grafo = grafo  # grafo residual
        self.fila = len(grafo)

    '''Regresa true si hay un camino desde salida hasta llegada en el grafo 
    residual. Ademas llena padre[] para almacenar el camino'''

    def encontrar_camino(self, salida, llegada, padre):

        # Marca todos los vertices como no visitados
        visitado = [False] * self.fila

        # Crea una cola para encontrar_camino
        cola = []

        # Marca el nodo de salida como visitado y lo saca de la cola
        cola.append(salida)
        visitado[salida] = True

        # Inicia la cola
        while cola:

            # Saca el primer vertice de la cola y lo guarda en una variable 'u'
            u = cola.pop(0)

            # Obtiene todos los vectores adyecentes del vertice 'u'
            # Si un vertice adyecente no ha sido visitado, lo marca
            # visitado y lo saca de la cola
            # La funcion enumerate devuelve un objeto enumrado
            # 'indice' indicara el indice y 'valor' el valor de la arista
            for indice, valor in enumerate(self.grafo[u]):
                if visitado[indice] == False and valor > 0:
                    cola.append(indice)
                    visitado[indice] = True
                    padre[indice] = u

        # Si se llega al vertice de llegada desde el de salida
        # devuelve true, si no devuelve false
        return True if visitado[llegada] else False

    # Retorna el flujo maximo desde salida hasta llegada en el grafo recibido
    def ford_fulkerson(self, source, sink):

        # Este vector es llenado por encontrar_camino para almacenar el camino
        padre = [-1] * self.fila

        max_flujo = 0  # Pone el flujo maximo en 0 por defecto

        # Aumenta el flujo mientras haya un camino desde salida hasta llegada
        while self.encontrar_camino(source, sink, padre):

            # Establece la variable como infinito para ser comparada

            camino_flujo = float("Inf")
            s = sink
            while s != source:
                # La funcion 'min' devuelve el valor minimo entre los argumentos
                camino_flujo = min(camino_flujo, self.grafo[padre[s]][s])
                s = padre[s]

            # Añade el flujo obtenido al flujo total
            max_flujo += camino_flujo

            # Actualiza la capacidad residual de las aristas y las aristas inversas
            v = sink
            while v != source:
                u = padre[v]
                self.grafo[u][v] -= camino_flujo
                self.grafo[v][u] += camino_flujo
                v = padre[v]

        return max_flujo


if __name__ == '__main__':
    grafo = [[0, 8, 0, 0, 3, 0],
             [0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 7, 2],
             [0, 0, 0, 0, 0, 5],
             [0, 0, 7, 4, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    g = Grafo(grafo)

    source = 0
    sink = 5

    print("Max Flow: %d " % g.ford_fulkerson(source, sink))
