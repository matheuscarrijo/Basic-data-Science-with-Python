# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:49:24 2021

@author: Matheus L. Carrijo

Exercício 20
Obtenha o índice do valor máximo do array A.


A = np.array([[11, 15, 33, 105],
              [1, 140, 45, 90],
              [67, 230, 78, 99]])


Dica: use np.argmax() ou array.argmax().
"""

import numpy as np

A = np.array([[11, 15, 33, 105],
              [1, 140, 45, 90],
              [67, 230, 78, 99]])

indice_valor_max = np.argmax(A)
