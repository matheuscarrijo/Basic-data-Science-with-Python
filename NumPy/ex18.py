# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:30:48 2021

@author: Matheus L. Carrijo

Exercício 18
Com base no array definido abaixo obtenha sua média, mediana, variância e 
desvio padrão.


import numpy as np
arr = np.random.normal(40,0.5,size = (300))


Dica:

Média: np.mean();

Mediana: np.median();

Desvio padrão: np.std();

Variância: np.var().
"""

import numpy as np

arr = np.random.normal(40,0.5,size = (300))

media = np.mean(arr)
mediana = np.median(arr)
dp = np.std(arr)
var = np.var(arr)