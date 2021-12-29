# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 04:28:10 2021

@author: Matheus L. Carrijo

Exercício 11
Use a função np.diag() para construir o array a seguir:


array([[ 5,  0,  0,  0,  0,  0],
       [ 0, 10,  0,  0,  0,  0],
       [ 0,  0, 15,  0,  0,  0],
       [ 0,  0,  0, 20,  0,  0],
       [ 0,  0,  0,  0, 25,  0],
       [ 0,  0,  0,  0,  0, 30]])

"""

import numpy as np

arraya = np.diag(np.arange(5, 35, 5))
