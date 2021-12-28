# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:41:53 2021

@author: Matheus L. Carrijo

Exercício 24
Indexação de arrays 1-D

Considerando os arrays abaixo:

import numpy as np
array1 = np.array([10, 20, 30, 40])
array2 = np.array([100, 30, 5, 1, 40, 100, 20, 130, 155,170])
   

Obtenha:

a) o primeiro, o terceiro e o último elemento de cada array;

b) inverta o array;

c) pegue o número 20 em ambos os arrays e armazene a soma em uma variável.
"""

import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([100, 30, 5, 1, 40, 100, 20, 130, 155,170])

# item a: 

primeiro_elem_1, terceiro_elem_1, ultimo_elem_1 = array1[0], array1[2], \
                                                  array1[-1]
                                                  
primeiro_elem_2, terceiro_elem_2, ultimo_elem_2 = array2[0], array2[2], \
                                                  array2[-1]  
                                                
# item b:
    
array1_reversed = array1[::-1]

# item c:
    
soma = array1[1] + array2[-4]
