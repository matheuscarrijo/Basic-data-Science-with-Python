# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 14:14:47 2021

@author: Matheus L. Carrijo

Exercício 17
Crie uma função que receba uma matriz como entrada e calcule:

    a) Valor máximo da matriz;

    b) Valor máximo por coluna;

    c) Valor máximo por linha;

    d) Valor mínimo da matriz;

    e) Valor mínimo por coluna;

    f) Valor mínimo por linha.


Exemplo de retorno para a matriz definida abaixo:

   
Input:

matriz = np.random.randint(-1000,1000,50).reshape(10,5)
info_matriz(matriz)


Output:

Valor máximo da matriz:  987
Valor máximo por coluna:  [959 987 597 748 719]
Valor máximo por linha:  [ 987  312  982  204  719  689  101  793 -460  959]
Valor mínimo da matriz:  -969
Valor mínimo por coluna:  [-878 -966 -969 -884 -881]
Valor mínimo por linha:  [  30 -878 -335 -863  -40 -289 -660 -239 -969 -966]
"""

import numpy as np

def info_matriz(matriz):
    
    valor_max = np.max(matriz)
    valor_max_por_linha = np.max(matriz, axis = 1)
    valor_max_por_coluna = np.max(matriz, axis = 0)
    valor_min = np.min(matriz)
    valor_min_por_linha = np.min(matriz, axis = 1)
    valor_min_por_coluna = np.min(matriz, axis = 0)
    
    print(f"Valor máximo da matriz: {valor_max}")
    print(f"Valor máximo por coluna: {valor_max_por_coluna}")
    print(f"Valor máximo por linha: {valor_max_por_linha}")
    print(f"Valor mínimo da matriz: {valor_min}")
    print(f"Valor mínimo por coluna: {valor_min_por_coluna}")
    print(f"Valor mínimo por linha: {valor_min_por_linha}")
    
    pass

matriz = np.random.randint(-1000,1000,50).reshape(10,5)
info_matriz(matriz)
