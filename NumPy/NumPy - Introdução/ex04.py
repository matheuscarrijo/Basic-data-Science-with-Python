# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 03:37:55 2021

@author: Matheus L. Carrijo

Exercício 4
A função np.ones() permite criar um array preenchido com o número 1 em todas as
suas entradas. Podemos especificar como argumentos o shape e o tipo de dado 
dtype do array. Use esta função para criar os arrays a seguir:

a)

array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])


b)

array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
       

c)

array([[1, 1],
       [1, 1],
       [1, 1]])
"""

import numpy as np 

# Ítem a:
    
arraya = np.ones(shape = 10, dtype = float)

# Ítem b:
    
arrayb = np.ones(shape = (4, 4), dtype = float)
    
# Ítem c:
    
arrayc = np.ones(shape = (3, 2), dtype = int)