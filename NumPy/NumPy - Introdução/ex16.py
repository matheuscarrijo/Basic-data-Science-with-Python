# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:14:47 2021

@author: Matheus L. Carrijo

Exercício 16
Obtenha o valor máximo e o valor mínimo de cada array abaixo. Implemente uma 
solução com loop for.

import numpy as np
array1 = np.array([-1, 10, 3, 4, 7, 27])
array2 = np.random.randint(-100,300,30)
array3 = np.random.randn(10)
array4 = np.array(range(50,10,-2))


Dica: para obter o valor máximo e mínimo de um array podemos usar array.max() 
e array.min() ( ou ainda max(array) e min(array)).
"""

import numpy as np

array1 = np.array([-1, 10, 3, 4, 7, 27])
array2 = np.random.randint(-100,300,30)
array3 = np.random.randn(10)
array4 = np.array(range(50,10,-2))

lista = [array1, array2, array3, array4]

for i in range(len(lista)):
    
    print(f"Valor maximo para o array {i+1}: {max(lista[i])}")
    print(f"Valor minimo para o array {i+1}: {min(lista[i])}")

    

