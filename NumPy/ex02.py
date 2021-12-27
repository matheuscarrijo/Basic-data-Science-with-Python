# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo

Exercício 2
Com base no exercício anterior crie uma função que receba um array e mostre na 
tela seus atributos. Verifique se o argumento inserido é de fato um objeto 
numpy. Use também a função built-in type() para verificar a classe do objeto.

Retorno esperado:

inspecionar_array(np.array([1,2,3]))
 
Shape : (3,)
Size:  3
Ndim:  1
Nbytes:  24
Dtype:  int64
Type:  <class 'numpy.ndarray'>
array([1, 2, 3, 4])


inspecionar_array([1,2,3])
 
'O objeto inserido não é um array NumPy.'

"""

import numpy as np 

def inspecionar_array(array):
    
    if type(array) == type(np.array([])):
        
        print(f"Shape: {array.shape}")
        print(f"Size: {array.size}")
        print(f"Ndim: {array.ndim}")
        print(f"Nbytes: {array.nbytes}")
        print(f"Dtype: {array.dtype}")
        print(f"Type: {type(array)}")
        
        return array
        
    else:
        
        return "O objeto inserido não é um array NumPy"

