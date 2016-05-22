# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:45:17 2016

@author: Lidiane
"""

import string
import collections

def carregarLista(arquivo):
    conteudo = open(arquivo)
    dados = conteudo.read()
    lista = string.split(dados)
    inteiros = []
    for elemento in lista:
        inteiros.append(int(elemento))
    return inteiros

def universo_amostral(lista):
    return len(lista)

def frequencia_abs(lista):
    frequencias = {}
    for xi in lista:
        if xi not in frequencias:
            frequencias[xi] = 1
        else:
            frequencias[xi] += 1

    return frequencias

def frequencia_rel(lista):
    frequencias = frequencia_abs(lista)
    for xi, fi in frequencias.iteritems():
        frequencias[xi] = float(fi) / universo_amostral(lista) * 100
    return frequencias

def frequencia_acumulada(lista):
    frequencias = frequencia_abs(lista)
    frequencias = collections.OrderedDict(sorted(frequencias.items()))
    aux = 0
    for xi, fi in frequencias.iteritems():
        frequencias[xi] = fi + aux
        aux += fi
    return frequencias

def frequencia_acumulada_rel(lista):
    frequencias = frequencia_acumulada(lista)
    for xi, fac in frequencias.iteritems():
        frequencias[xi] = float(fac) / universo_amostral(lista) * 100
    return frequencias

arquivo = 'pesos.txt'

lista = carregarLista(arquivo)
print lista
print "Universo Amostral:", universo_amostral(lista)
print "Fi de 70:", frequencia_abs(lista)[70]
print "Fr de 85:", frequencia_rel(lista)[85]
print "Fac de 98:", frequencia_acumulada(lista)[98]
print "Frac de 98:", frequencia_acumulada_rel(lista)[98]