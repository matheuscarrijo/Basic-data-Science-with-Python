# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo

Exercício 3:
    
Use a função np.array() para criar os arrays unidimensionais listados abaixo:

a) Use uma lista como argumento e obtenha:

array([-1,  4,  7,  9])


b) Use a função range() e obtenha:
    
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])


c)Use uma tupla como argumento e obtenha:

array([10, 11, 12, 13, 14])


d) Use a função range() e obtenha:
    
array([1990, 1995, 2000, 2005, 2010, 2015, 2020])


e) Use a função range() e obtenha:


array([2020, 2010, 2000, 1990, 1980, 1970, 1960, 1950, 1940, 1930, 1920,
       1910, 1900])


f) Obtenha:

array(100)

"""

import numpy as np

#Solução:
    
# Letra a

array_a = np.array([1,2])

# Letra b

array_b = np.arange(1, 11)

# Letra c

array_c = np.array((10, 11, 12, 13, 14))

# Letra d

array_d = np.arange(1990, 2025, 5)

# Letra e

array_e = np.arange(2020, 1895, -10)

# Letra f

array_f = np.array(100)
