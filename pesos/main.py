# -*- coding: utf-8 -*-
"""
Created on Mon May 23 01:02:17 2016

@author: Lidiane
"""

from frequencias import *
from medidas_posicao import *

arquivo = 'pesos.txt'

lista = carregarLista(arquivo)
print "fi de 85:", frequencia_abs(lista)[85]
print "fac de 75:", frequencia_acumulada(lista)[75]
print "fr de 65:", frequencia_rel(lista)[65]
print "frac de 96:", frequencia_acumulada_rel(lista)[96]

# lista.append(76)
print "Media:", media(lista)
print "Mediana:", (mediana(lista))
print "Moda:", (moda(lista))
