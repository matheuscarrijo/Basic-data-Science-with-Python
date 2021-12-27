# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 04:28:10 2021

@author: Matheus L. Carrijo

Exercício 12
Use a função np.eye() (ou ainda np.identity()) para obter o array seguir.


array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])


Dica: essa matriz é definida como matriz identidade, neste caso de ordem 10, e 
assume grande relevância em diversos cálculos computacionais, como veremos mais
adiante.



"""

import numpy as np

arraya = np.eye(10)
