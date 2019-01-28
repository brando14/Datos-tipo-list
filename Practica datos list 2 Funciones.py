lista1= ['a','b','c','d']
print('hay',len(lista1),'elementos') # indica cuantos elemenros hay en una lista

print('a' in lista1)  # el metodo in permite saber si un factor esta en la lista si esta dara como resultado la expresion.
                      # booleana tru si no esta arrojara la expresion false.

print(lista1.index('b'))   # la funcion index permite,saber la posicion en que se encuentra el elemento en la lista de acuerdo a su indice

#Como convertir un elemento de Stra una lista
texto = input("Ingrese una lista: ")
no_olvidar = []
inicio = 0
for i in range(0,len(texto)):
    if texto[i] == ",":
        no_olvidar.append(texto[inicio:i])
        inicio = i+1
no_olvidar.append(texto[inicio:])         # Split es un método de tipo string, no es un método de las listas, pero es muy útil porque nos permite separar un string cada vez que ocurre un texto
                                          # que le llamamos separador, y obtener como resultado una lista con todos los elementos separados de acuerdo a este separador.
                                        #De esta manera como ejemplo, el mismo código largo que vimos en la slide anterior podemos reescribirlo de manera mucho más concisa usando solamente una línea.
                                        # aqui la indicamos que lacoma sera el separador.
print('lista:', no_olvidar)

# o
texto2= input("Ingrese una lista: ")
lista2= texto2.split(',')
print('lista:', lista2)

lista3= ['43','60','23','18','1']
lista3.sort()                         # el metodo sort permite ordenar de menor a mayor losfacotres contenidos de las listas.
print(lista3)