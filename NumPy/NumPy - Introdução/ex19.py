# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:37:29 2021

@author: Matheus L. Carrijo

Exercício 19
Com base nos arrays definidos a seguir obtenha a matriz de covariância e a 
matriz de correlação.

import numpy as np
x = np.random.rand(100)
y = np.random.uniform(size=100)

Dica: use np.corrcoef() e np.cov().
"""

import numpy as np

x = np.random.rand(100)
y = np.random.uniform(size=100)

matriz_cov = np.cov(x, y)
matriz_corr = np.corrcoef(x, y)