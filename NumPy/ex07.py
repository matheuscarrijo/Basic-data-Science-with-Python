# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 04:04:45 2021

@author: Matheus L. Carrijo

Exercício 7
Utilize a função np.full(shape, fill_value, dtype) para criar os arrays a 
seguir. Esta função permite criar um array com um shape e dtype definidos pelo 
usuário, preenchido com um determinado valor.

a)


array([5., 5., 5., 5., 5., 5., 5., 5., 5., 5.])


b)


array([[-5., -5., -5., -5.],
       [-5., -5., -5., -5.],
       [-5., -5., -5., -5.],
       [-5., -5., -5., -5.]])


c)


array([[3, 3, 3],
       [3, 3, 3],
       [3, 3, 3]])
d)


array([[50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
       [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]])


Dica: outra possibilidade seria obter os arrays com uma operação diferente, a 
partir da multiplicação de uma matriz preenchida com número 1 por um 
determinado valor.

"""

import numpy as np

# item a:
    
arraya = np.full(10, 5, dtype = float)

# item b:
    
arrayb = np.full((4, 4), -5, dtype = float)

# item c:
    
arrayc = np.full((3,3), 3)

# item d:

arrayd = np.full((10, 10), 50)
