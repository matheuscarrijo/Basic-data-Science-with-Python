# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 16:12:38 2021

@author: Matheus L. Carrijo

Exercício 25
Indexação de arrays 2-D


Acesse os números 9 e 90 do array abaixo.


import numpy as np
ar = np.array([[-1, 33, 44, 9, 1],[11, 1, 0, 90, 44]])

"""

import numpy as np

ar = np.array([[-1, 33, 44, 9, 1],[11, 1, 0, 90, 44]])

numero9 = ar[0, 3]
numero90 = ar[1, 3]