# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 04:13:49 2021

@author: Matheus L. Carrijo

Exercício 8
Defina o array K e verifique se há dados ausentes (missing data). Use a função 
np.isnan().


array([[ nan,   1.,  10.,   0.],
       [ nan,  nan,  nan,  nan],
       [100.,  50.,  nan, -25.],
       [ 30.,  nan,  nan, 130.]])

"""

import numpy as np 

K = np.array([np.nan,      1,     10,      0,
              np.nan, np.nan, np.nan, np.nan,
              100,        50, np.nan,    -25,
              30,     np.nan, np.nan,    130], dtype = float)

missings = np.isnan(K)

if True in missings:
    
    print("Existe dado ausente (missing data) no array K")
    
else:
    
    print("Não existe dado ausente (missing data) no array K")
