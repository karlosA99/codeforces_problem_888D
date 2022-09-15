import itertools
import math
from random import randint

def Count_AIP_BF(n, k):
    perm = list(itertools.permutations(range(1,n+1),n)) #generamos todas las permutaciones de tamaño n
    ans = 0 # aqui llevamos la cuenta de cuantas permutaciones han cumplido la propiedad
    for p in perm:  #recorremos dichas permutaciones
        count = k  #inicializamos count = k, ya que la permutación admite k elementos "mal ubicados"
        ans += 1   #asumimos que p cumple la propiedad, en caso de no cumplirla se resta 1 luego
        for i in range(n): #recorremos los elementos de p hasta que count < 0, si count < 0 significa que no cumple la propiedad
            if (p[i] != i+1): 
                count-=1
            if (count < 0):
                ans-=1
                break
    return ans

def Count_AIP_C(n, k):
    count = 0
    #en el pdf esta la explicación y demostración bien profunda de este algoritmo
    for m in range(k+1):
        count += math.comb(n, m) * d(m)
    
    return count

def d(m):  # aqui se asignan los valores que ya conocemos que retornará d en cada caso, pudimos hacerlo de esta manera ya que solo
    if (m==0):                          #hay 5 valores posibles para m, cada caso quedo explicado en el pdf
        return 1
    if (m==1):  
        return 0
    if (m==2):
        return 1
    if (m==3):
        return 2
    if (m==4):
        return 9
    
def F(m): #Solamente se utilizó para saber el resultado de d(4). Pero es posible utilizarla para cualquiera sea m 
    count = 0
    perm = list(itertools.permutations(range(1,m+1),m)) #aqui creamos las permutaciones de los índices de los elementos
    for p in perm:    #recorremos dichas permutaciones en busca  de encontrar las que tiene todos sus elem "mal ubicados"
        count+=1  #primeramente asumimos que p tiene todos los elementos "mal ubicados"
        for i in range(m):
            if (p[i] == i+1):  #al recorrer la permutación si nos percatamos de que hay un elemento "bien ubicado", restamos 1
                count-=1                            # al count y pasamos a la siguiente permutación
                break
    return count

def Tester(test_number,ran_n):
    corrects = 0   #esta es la cantidad de casos correctos
    incorrects = []   #en esta lista se guardan las tuplas <n,k> que hallan resultado incorrecta para su análisis
    
    for i in range(test_number):  #ejecutamos el ciclo test_number veces
        n = randint(4, ran_n)    #creamos valores random de n y k, en este caso n acotado por ran_n, ya que para valores elevados de
        k = randint(1, 4)                                           #n da error en memoria producto del algoritmo por fuerza bruta
        if (Count_AIP_C(n,k) == Count_AIP_BF(n,k)):   #comprobamos si ambos algoritmos dan iguales resultados
            corrects += 1      #en caso positivo aumentamos los tests correctos
        else:
            incorrects.append((n,k))    #en caso negativo guardamos la tupla que resulto en un error en la lista incorrects
    print(str(corrects) + " " + "Casos Correctos")    #finalmente imprimimos los resultados obtenidos
    print("Los casos incorrectos son" + " " + str(incorrects))
    






