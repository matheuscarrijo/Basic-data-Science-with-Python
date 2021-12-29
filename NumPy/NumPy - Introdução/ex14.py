# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:14:47 2021

@author: Matheus L. Carrijo

Exercício 14
Obtenha a soma dos elementos de cada array a seguir. Use a função np.sum(). 
Implemente uma solução com loop for, para tanto armazene os vetores em uma 
lista.


import numpy as np
array1 = np.arange(1,11)
array2 = np.linspace(1,50,10)
array3 = np.array(range(51))
array4 = np.logspace(1,10,5)
array5 = np.diag(range(5,31,5))


Retorno esperado:


Soma dos elementos do array 1:  55
Soma dos elementos do array 2:  255.0
Soma dos elementos do array 3:  1275
Soma dos elementos do array 4:  10056552148.564463
Soma dos elementos do array 5:  105

"""

import numpy as np

# solucao 1:
    
array1 = np.arange(1,11)
sum_array1 = np.sum(array1)

array2 = np.linspace(1,50,10)
sum_array2 = np.sum(array2)

array3 = np.array(range(51))
sum_array3 = np.sum(array3)

array4 = np.logspace(1,10,5)
sum_array4 = np.sum(array4)

array5 = np.diag(range(5,31,5))
sum_array5 = np.sum(array5)

lista = [sum_array1, sum_array2, sum_array3, sum_array4, sum_array5]

for i,j in enumerate(lista):
    
    print(f"Soma dos elementos do array {i+1}: {j}")