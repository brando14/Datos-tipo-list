#1. Question 1
# Escriba una función de nombre promedio_std(). La función debe recibir una lista de números llamada lista,
# y debe retornar retornar el promedio de ellos, junto con su desviación estándar.
# Hint 1: La desviación estándar corresponde a la raíz de la suma de los cuadrados
#  de las diferencias de cada elemento respecto al promedio, divididos por la cantidad de elementos.
# Hint 2: Recuerda que puedes retonar dos valores x e y

from math import sqrt,pow

def Promedio_std(lista):
    total = 0
    for i in lista:
        total += i
        x = total / len(lista)
    total = 0
    for i in lista:
        total += (i - x) ** 2
        y = sqrt(total / len(lista)) ** 0.5
    return (x,y)

lista = [3, 5, 10, 12]
media, desviacion_tipica = Promedio_std(lista)
print(f"Media: {media}")
print(f"Desviación estandar: {desviacion_tipica}")



#Suponga que tiene una lista de colores repetidos y desordenados, estos pueden ser: azul, rojo, verde y amarillo.
# Desea saber cual de esos colores es el que más se repite. Escriba una función color_frecuente que reciba como argumento
#  a una lista de strings llamada lista y retorne el string más repetido y el número de ocurrencias del mismo.
# Por ejemplo para la lista
# ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul',
# 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
# Debe retornar: "verde", 8
# En caso de que haya varios colores con el máximo número,
# se retornará con la siguiente prioridad: azul, rojo, verde, amarillo.
# Es decir, por ejemplo si la lista es l = ['rojo', 'rojo', 'azul', azul'], la función debe retornar "azul", 2


def obtener_color_frecuente(colores, lista_prioridad):
    contador = {}
    for color in colores:
        if color in contador:
            contador[color] += 1 # incrementamos si existe el color
        else:
            contador[color] = 1 # creamos un nuevo item con el key del color y el valor inicial de 1
    m = max(contador.values()) # obtenemos el max de repeticiones
    color_seleccionado = [key for key, value in contador.items() if value == m] # seleccionamos los colores que cumplen con el maximo
    if len(color_seleccionado) > 1: # verificamos si existe mas de un maximo
        color_seleccionado = min(color_seleccionado, key= lambda x: lista_prioridad.index(x)) # obtenemos el elemento segun la prioridad
    else:
         color_seleccionado = color_seleccionado[0]
    return color_seleccionado, m

prioridad = ["azul","rojo","verde","amarillo"]
colores = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul',
        'azul', 'verde', 'verde', 'verde', 'amarillo']
print(obtener_color_frecuente(colores, prioridad))




