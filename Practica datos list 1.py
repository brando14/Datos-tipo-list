lista1= ['a','b','c','d']
print(lista1)

lista2= ['f','g','h']
lista3= lista1+lista2     # se puede usar las mismas propiedades de los string como la cocatenacion y la repeticion
print(lista3)             # la primera concatenacion consiste en unir dos listas y crear una nueva que incluya los datos de ambas

print(lista1*3)           # la repeticion consiste en repetir en una secuencia los datos incluidos en la lista.

for elem in lista1:        # el for-in permite hacer una colocar los elementos de una lista en fila.
    print('letra:', elem)

lista1.append('f')  # el metodo append permite agregar un elemento al extremo
print(lista1)       # de una lista


lista4= ['1','2','3']
                         # el metodo extend permite agregar 2 o mas elementos para modificar una lista
lista4.extend(['4','5'])   # a diferencia de la cocatenecion esta modifica la lista original y no crea una nueva
print(lista4)



lista4.insert(4,'5')  # el metodo insert permite insertar un nuevo elemento a lal ista en cualquier posicion que se indeque
print(lista4)         # esto depende del numero de indice en donde se quiera colocar el elemento, en este caso siguiendo las
                      #las propiedades de los string aplicables a las listas se indico que se insertara en elindici 4 el factor 5
                      # los indices se encuentran ordenados derecha a izquierda empezando desde 0.

lista5 = ['10','20','30','40']  # el metodo pop permite remover el ultimo factor de una lista y lo entrega como resultado.
print(lista5.pop())             # una observacion en el curso se indica que elimina el primer factor pero no es asi.
                                # verifique con alejandro.

lista6= ['10','20','30','40'] # permite remover un elemento de la lista indicando cual es, otra observacion
lista6.remove('20')           # en el  curso se dice que se remueve por el numero de indice pero no es asi hay que indicar que
print(lista6)                 # parametro se va a eliminar.


