#2. Question 2.Sea la variable lista_espera que contiene la lista de espera de un restaurante.
#¿Cuál, de las siguientes alternativas, permite almacenar en la variable siguiente_cliente el nombre
#del siguiente cliente a ser atendido?. El siguiente cliente es el primero en la lista de espera, de izquierda a derecha.

lista_espera = ["Mar", "Jorge", "Cristian", "Valeria"]
siguiente_cliente = lista_espera[0]                     
print(siguiente_cliente)

# tercera pregunta del cuestionario: ¿Cómo queda la lista lista_compras después de ejecutar este código?
# Doña Rosa ya no sabe qué comprar y qué no comprar
lista_compras = ["pan", "huevo", "queso", "arroz", "jamon"]
lista_compras.append("maní")
lista_compras.remove("arroz")
lista_compras.insert(2,"leche")
print(lista_compras)

#¿Cuál es el valor de la variable trozo después de ejecutar el siguiente código? (pregunta 4 y 5)

datos = [2, "Julio", 2017, "Final", 14.5, "Chile", 0, "Alemania", 1]
trozo = datos[2:6]
print(trozo)

datos2 = ["semillas", 500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza", 95.4]
trozo2 = datos2[1:9:2]
print(trozo2)

# pregunta 6  para que la salida sea [49, 2, 55, 300] se debe aplicar el siguiente codigo.
unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = unidades[2:4] + unidades[6:8]
print(muestra)

#la lista votos, que contiene listas con los resultados de una votación:

def ganador(votos):
  mayor = votos[0]            # este lafuncion indicada que retorna correctamente el string asociado al valor más grande
  for cand in votos:
    if cand[1] > mayor[1]:
      mayor = cand
  return mayor

resultados = [ ["Alfredo",20], ["Marcela",40], ["Ignacio",30], ["Loreto",10] ]  # estos son los resultados que se consideraron
mayoria = ganador(resultados)
print(ganador(resultados))


# ¿Cuál es el valor de la variable splitted luego de ejecutar el siguiente código?
contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
print(splitted)
# el resultado es ['Marcelo, Alvaro', ' Elena, Karen', ' Jaime', ' Carmen']


# obtener la cantidad de veces que un elemento elem se encuentra dentro de la lista conjunto.

def cuantas(elem, conjunto):
  contador = 0
  for e in conjunto:
    if e == elem:
      contador += 1
  return contador

lista = [1, 1, 2, 3, 4, 4]
n = cuantas(4, lista)
print(n)


#Considera un tablero de 3x3 posiciones, donde cada una de ella está numerada desde el número 1 al 9.
#  El tablero está definido de la siguiente manera: tablero = [ [1,2,3], [4,5,6], [7,8,9] ]
#De los siguientes códigos, marque aquellos que permiten recorrer el tablero por orden de columnas.
#  Esto significa que la salida debe escribir los valores: 1 4 7 2 5 8 3 6 9

# respuesta:

tablero = [ [1,2,3], [4,5,6], [7,8,9] ]
for i in range(9):
  print(tablero[i%3][i//3],end=" ")