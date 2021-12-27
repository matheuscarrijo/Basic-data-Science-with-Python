# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 04:28:10 2021

@author: Matheus L. Carrijo

Exercício 10
A função np.logspace() retorna números com espaçamento uniforme em uma escala logarítmica. Crie um array com números
dentro do intervalo [1, 51] em 10 partes com a função np.logspace().

Retorno esperado:

array([[1.00000000e+01],
       [3.59381366e+06],
       [1.29154967e+12],
       [4.64158883e+17],
       [1.66810054e+23],
       [5.99484250e+28],
       [2.15443469e+34],
       [7.74263683e+39],
       [2.78255940e+45],
       [1.00000000e+51]])

"""

import numpy as np

arraya = np.logspace(1, 51, 10)
