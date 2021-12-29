# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 03:55:16 2021

@author: Matheus L. Carrijo

Exercício 6
Crie os arrays a seguir:


a)


array([[10],
       [15],
       [20],
       [25],
       [30],
       [35],
       [40],
       [45]])


b)


array([-50, -45, -40, -35, -30, -25, -20, -15, -10,  -5])


c)


array([[ 50,  52,  54,  56,  58,  60,  62,  64,  66,  68],
       [ 70,  72,  74,  76,  78,  80,  82,  84,  86,  88],
       [ 90,  92,  94,  96,  98, 100, 102, 104, 106, 108],
       [110, 112, 114, 116, 118, 120, 122, 124, 126, 128],
       [130, 132, 134, 136, 138, 140, 142, 144, 146, 148]])
       

Dica: use np.arange() ou np.array(range()).

"""

import numpy as np 

# item a:
    
arraya = np.arange(start = 10, stop = 50, step = 5).reshape((8,1))

# item b:
    
arrayb = np.arange(-50, 0, 5)
    
# item c:
    
arrayc = np.arange(50, 150, 2).reshape((5, 10))

