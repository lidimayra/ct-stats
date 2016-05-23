# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:43:24 2016

@author: Lidiane
"""

from math import floor, ceil
from frequencias import carregarLista, frequencia_abs, universo_amostral, frequencia_acumulada

def media(lista):
    xifi = frequencia_abs(lista)    
    somatoria_xifi = 0
    for xi, fi in xifi.items():
        somatoria_xifi += xi*fi
    return float(somatoria_xifi) / universo_amostral(lista)

def mediana(lista):
    x1 = 0; x2 = 0
    fac = frequencia_acumulada(lista)
    em = (universo_amostral(lista) + 1) / 2.0        

    for xi, freq in fac.items():
        if (freq <= em):
            posicao_1 = floor(em)
            posicao_2 = ceil(em)

    for chave, valor in fac.items():
        if x1 == 0 and valor >= posicao_1:
            x1 = chave
        if x2 == 0 and valor >= posicao_2:
            x2 = chave
    
    res = (x1 + x2) / 2.0
    return res

def moda(lista):
    xifi = frequencia_abs(lista)
    return max(xifi, key=xifi.get)

arquivo = 'pesos.txt'

lista = carregarLista(arquivo)
# lista.append(76)
print media(lista)
print(mediana(lista))
print(moda(lista))
