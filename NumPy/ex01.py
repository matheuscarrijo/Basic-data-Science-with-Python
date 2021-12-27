# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo

Exercício:
    
Inspecionando um Array NumPy

Um objeto numpy possui atributos e métodos, herdados da classe (numpy.ndarray). 
Crie um array  e inspecione os seguintes atributos:

shape: uma tupla que contém o número de elementos (tamanho) em cada dimensão do 
array;

size: número total de elementos do array;

ndim: número de dimensões (eixos);

nbytes: número de bytes utilizado no armazenamento dos dados;

dtype: data type dos elementos do array.

"""

import numpy as np 

matriz = np.array([[1, 2, 3],
                  [4, 5, 6]]) # criando uma matriz

shape = matriz.shape # ou: shape = np.shape(matriz)
size = matriz.size # ou: np.size(matriz)
dimensao = matriz.ndim # ou: np.ndim(matriz)
numero_bytes = matriz.nbytes # NÃO funciona np.nbytes(matriz)
tipo = matriz.dtype # NÃO funciona np.dtype(matriz)


