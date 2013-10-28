Pasteles-Ricos
==============
El problema de calcular la cantidad máxima de pasteles ricos distintos se resuelve realizando una búsqueda de grafo por amplitud.
La búsqueda se realiza expandiendo nodos, los cuales contienen un estado que en este caso representa la posicion de los ingredientes en el molde.

Planteando diferentes escenarios en los cuales se elijen 9 de los 10 ingredientes nos encontramos con lo siguiente:

Situación 1 (representacion del molde):
dulce		| dulce		| dulce
frutas		| frutas	| frutas
confites	| confites	| confites

Situación 2:
masita		| dulce		| dulce
frutas		| frutas	| frutas
confites	| confites	| confites

Situación 3:
dulce		| dulce		| dulce
masita		| frutas	| frutas
confites	| confites	| confites

Situación 4:
dulce		| dulce		| dulce
frutas		| frutas	| frutas
masita		| confites	| confites

Estas situaciones son estados iniciales que sirven de entrada al algoritmo de búsqueda para encontrar todas las combinaciones que son válidas (pasteles ricos)

Si se ejecuta el archivo waragon.py veremos como salida:

Situacion 1. Pasteles ricos: 336
Situacion 2. Pasteles ricos: 3594
Situacion 3. Pasteles ricos: 3594
Situacion 4. Pasteles ricos: 3594

Total de pasteles ricos: 11118


Lo que nos indica que el numero buscado para nuestra solucion es 11118 pasteles ricos.
