# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:09:41 2021

@author: Matheus L. Carrijo

Exercício 23
Use a função np.unique() para obter um array com os elementos únicos do array 
abaixo. Para tanto, armazene o novo array em uma variável.

A = np.array([
    [1, 3, 3, 4, 5],
    [4, 7, 11, 3, 5],
    [1, 11, 4, 4, 11]])
"""

import numpy as np

A = np.array([
    [1, 3, 3, 4, 5],
    [4, 7, 11, 3, 5],
    [1, 11, 4, 4, 11]])

novo_array = np.unique(A)
print(novo_array)

