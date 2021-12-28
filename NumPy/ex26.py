# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:54:03 2021

@author: Matheus L. Carrijo

Exercício 26
Indexação de arrays 3-D


Acesse os números 5, 9, 3 e 21 do array abaixo.


import numpy as np
ar = np.array([
    [[1, 1, 5, 1],
     [1, 1, 1, 9]],
    [[1, 3, 1, 1],
     [1, 1, 21, 1]]
              ])
"""

import numpy as np

ar = np.array([
    [[1, 1, 5, 1],
     [1, 1, 1, 9]],
    [[1, 3, 1, 1],
     [1, 1, 21, 1]]
              ])

numero5 = ar[0, 0, 2]
numero9 = ar[0, 1, 3]
numero3 = ar[1, 0, 1]
numero21 = ar[1, 1, 2]

