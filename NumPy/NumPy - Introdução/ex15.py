# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:14:47 2021

@author: Matheus L. Carrijo

Exercício 15
A partir da matriz definida abaixo obtenha: 
    a) soma total dos elementos; 
    b) soma das linhas ; 
    c) soma das colunas.

import numpy as np
matriz = np.array(np.random.randint(1, 100, 15)).reshape(5, 3)

"""

import numpy as np

matriz = np.array(np.random.randint(1, 100, 15)).reshape(5, 3)

# item a:

soma = np.sum(matriz)
    
# item b:
    
soma_linhas = np.sum(matriz, axis = 1)

# item c:
    
soma_colunas = np.sum(matriz, axis = 0)
    