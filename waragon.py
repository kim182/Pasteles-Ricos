from search import Problem, breadth_first_graph_search
import copy

# Tablero (Molde)
#   a1  a2  a3
#   b1  b2  b3
#   c1  c2  c3

#   (0,0)   (0,1)   (0,2)
#   (1,0)   (1,1)   (1,2)
#   (2,0)   (2,1)   (2,2)

class ProblemaDelMolde(Problem):
    ''' Clase problema (formalizacion de nuestro problema) siguiendo la
        estructura que aima espera que tengan los problemas.'''
    def __init__(self, initial, goal=None):
        '''Inicializacion de nuestro problema.'''
        Problem.__init__(self, initial, goal)

        # Las acciones son movimientos de determinadas piezas:
        #
        # Movimientos horizontales
        # a1xa2
        # a2xa3
        # b1xb2
        # b2xb3
        # c1xc2
        # c2xc3
        #
        # Movimientos verticales
        # a1xb1
        # b1xc1
        # a2xb2
        # b2xc2
        # a3xb3
        # b3xc3

        self._actions = [
                            ('a1xa2', (0,0), (0,1)), ('a2xa3', (0,1), (0,2)), ('b1xb2', (1,0), (1,1)), ('b2xb3', (1,1), (1,2)), ('c1xc2', (2,0), (2,1)), ('c2xc3', (2,1),(2,2)),
                            ('a1xb1', (0,0), (1,0)), ('b1xc1', (1,0), (2,0)), ('a2xb2', (0,1), (1,1)), ('b2xc2', (1,1), (2,1)), ('a3xb3', (0,2), (1,2)), ('b3xc3', (1,2),(2,2))
                        ]
        self.validStates = []
        self.cantidadPastelesRicos = 0

    def actions(self, s):
        '''Devuelve las acciones validas para un estado.'''
        # las acciones validas para un estado son aquellas que al aplicarse
        # nos dejan en otro estado valido
        return [a for a in self._actions]

    def result(self, s, a):
        '''Devuelve el estado resultante de aplicar una accion a un estado
           determinado.'''
        # Debemos conmutar las coordenadas presentes en la acciones (a[1] x a[2])
        x,y = a[1]
        x1,y1 = a[2]
        h = copy.deepcopy(s) # realizar una copia
        h = list(list(x) for x in h)
        h[x][y], h[x1][y1] = h[x1][y1], h[x][y]
        h = (tuple(tuple(x) for x in h))
        return h

    def goal_test(self, state):
        # Verificar si el pastel es rico

        if (self.es_rico(state)):
            if state not in self.validStates:
                self.cantidadPastelesRicos += 1
                self.validStates.append(state)

        return state == self.goal

    def es_rico(self, s):
        # El pastel es rico cuando tres mismos ingredientes estan alineados
        # vertical u horizontalmente. La masita es especial
        if (

            # horizontal
                ((s[0][0] == s[0][1] or (s[0][0] == 'm' or s[0][1] == 'm'))
                and (s [0][1] == s [0][2] or (s[0][1] == 'm' or s[0][2] == 'm')))
            or

            # horizontal
                ((s[1][0] == s[1][1] or (s[1][0] == 'm' or s[1][1] == 'm'))
                and (s [1][1] == s [1][2] or (s[1][1] == 'm' or s[1][2] == 'm')))

            or
            # horizontal
                ((s[2][0] == s[2][1] or (s[2][0] == 'm' or s[2][1] == 'm'))
                and (s [2][1] == s [2][2] or (s[2][1] == 'm' or s[2][2] == 'm')))

            or
            # vertical
                ((s[0][0] == s[1][0] or (s[0][0] == 'm' or s[1][1] == 'm'))
                and (s [1][0] == s [2][0] or (s[1][0] == 'm' or s[2][0] == 'm')))

            or
            # vertical
                ((s[0][1] == s[1][1] or (s[0][1] == 'm' or s[1][1] == 'm'))
                and (s [1][1] == s [2][1] or (s[1][1] == 'm' or s[2][1] == 'm')))

            or
            # vertical
                ((s[0][2] == s[1][2] or (s[0][2] == 'm' or s[1][2] == 'm'))
                and (s [1][2] == s [2][2] or (s[1][2] == 'm' or s[2][2] == 'm')))
            ):
            return True
        return False


dulce='d'
frutas='f'
confites='c'
masita='m'
estado_inicial = (
                    (dulce,dulce,dulce),
                    (frutas,frutas,frutas),
                    (confites,confites,confites))

estado_objetivo = (('x','x','x'),
                    ('x','x','x'),
                    ('x','x','x')) # Objetivo irreal, para explorar todo el grafo de posibilidades

p1 = ProblemaDelMolde(estado_inicial, estado_objetivo)

#Busqueda en amplitud
r = breadth_first_graph_search(p1)

print "Situacion 1. Pasteles ricos: " + str(p1.cantidadPastelesRicos)

estado_inicial = (
                    (masita,dulce,dulce),
                    (frutas,frutas,frutas),
                    (confites,confites,confites))

estado_objetivo = (('x','x','x'),
                    ('x','x','x'),
                    ('x','x','x')) # Objetivo irreal, para explorar todo el grafo de posibilidades

p2 = ProblemaDelMolde(estado_inicial, estado_objetivo)

#Busqueda en amplitud
r = breadth_first_graph_search(p2)

print "Situacion 2. Pasteles ricos: " + str(p2.cantidadPastelesRicos)

estado_inicial = (
                    (dulce,dulce,dulce),
                    (masita,frutas,frutas),
                    (confites,confites,confites))

estado_objetivo = (('x','x','x'),
                    ('x','x','x'),
                    ('x','x','x')) # Objetivo irreal, para explorar todo el grafo de posibilidades

p3 = ProblemaDelMolde(estado_inicial, estado_objetivo)

#Busqueda en amplitud
r = breadth_first_graph_search(p3)

print "Situacion 3. Pasteles ricos: " + str(p3.cantidadPastelesRicos)

estado_inicial = (
                    (dulce,dulce,dulce),
                    (frutas,frutas,frutas),
                    (masita,confites,confites))

estado_objetivo = (('x','x','x'),
                    ('x','x','x'),
                    ('x','x','x')) # Objetivo irreal, para explorar todo el grafo de posibilidades

p4 = ProblemaDelMolde(estado_inicial, estado_objetivo)

#Busqueda en amplitud
r = breadth_first_graph_search(p4)

print "Situacion 4. Pasteles ricos: " + str(p4.cantidadPastelesRicos)

print "---------------------------------------------"
print "Total de pasteles ricos: " + str(p1.cantidadPastelesRicos + p2.cantidadPastelesRicos + p3.cantidadPastelesRicos + p4.cantidadPastelesRicos)