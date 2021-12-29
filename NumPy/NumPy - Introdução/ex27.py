# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:57:49 2021

@author: Matheus L. Carrijo

Exercício 27
Slicing 1-D

Com base no array abaixo obtenha o slice do índice 2 até o índice 6.


import numpy as np
ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


Dica: Em Python, slicing significa que podemos selecionar elementos entre 
índices especificados. Sintaxe: [start:end:pass].

Se não especificarmos o start o valor default será 0. Se não definirmos o step,
será considerado o valor 1.
"""

import numpy as np

ar = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

slice = ar[2:7]

