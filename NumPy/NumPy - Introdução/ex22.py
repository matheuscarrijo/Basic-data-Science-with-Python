# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:55:42 2021

@author: Matheus L. Carrijo

Exercício 22
Escreva uma função que receba um array NumPy e mostre na tela um conjunto de 
estatísticas descritivas deste objeto.


Resultado esperado:

Input:

array = np.array([-57, 101, 270, 130, 144])
info_array(array)


Output:

Valor máximo: 270
Valor mínimo: -57
Média: 117.6
Mediana: 130.0
Variância: 10967.439999999999
Desvio padrão: 104.72554607162475
"""

import numpy as np

def info_array(array):
    
    print(f"Valor máximo: {np.max(array)}")
    print(f"Valor mínimo: {np.min(array)}")
    print(f"Média: {np.mean(array)}")
    print(f"Variância: {np.var(array)}")
    print(f"Desvio padrão: {np.std(array)}")
    
    pass

array = np.array([-57, 101, 270, 130, 144])
info_array(array)