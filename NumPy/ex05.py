# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 03:49:34 2021

@author: Matheus L. Carrijo

Exercício 5
A função np.ones() permite criar um array preenchido com o número 0 em todas
as suas entradas. Podemos especificar como argumentos o shape e o tipo de dado 
dtype do array (default é o float). Use esta função para criar os arrays a 
seguir:

a)

array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])


b)

array([[0., 0.],
       [0., 0.]])  
       

c)

array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.]])

"""

import numpy as np 

# Ítem a:
    
arraya = np.ones(10)

# Ítem b:
    
arrayb = np.ones((2, 2))

# Ítem c:
    
arrayc = np.ones((4, 6))