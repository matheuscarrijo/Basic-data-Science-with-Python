# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:49:24 2021

@author: Matheus L. Carrijo

Exercício 20
Obtenha o índice do valor mínimo do array A.


B = np.array([
    [73, 22, 20, 62,  3],
    [68, 84, 27, 59, 93],
    [48, 52,  4, 55, 50],
    [42, 23, 63, 67,  4],
    [44, 30, 41, 31, 29]])


Dica: use np.argmin() ou array.argmin().
"""

import numpy as np

B = np.array([
    [73, 22, 20, 62,  3],
    [68, 84, 27, 59, 93],
    [48, 52,  4, 55, 50],
    [42, 23, 63, 67,  4],
    [44, 30, 41, 31, 29]])

indice_valor_min = np.argmin(B)
