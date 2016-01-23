# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 04:28:50 2016

@author: rafael
"""
import numpy as np
import matplotlib.pyplot as plt

class GrapMinder(object):

    #classe inicial
    def __init__():# esse parenteses e o construtor
        #abrir arquivos
        #Comando open com 'r' de reader
        dataset_1 = open('indicator hiv estimated prevalence% 15-49.csv','r')
        dataset_2 = open('cell phone total.csv','r')
        #instancia da classe plotar, objeto pl
        pl = plotar()

        #fechar os arquivos ;)
        dataset_1.close()
        dataset_2.close()


"""
Essa classe vai ser os tratamento dos dados
ela deve retornar eles tratados para a classe inicial
e la se plota o grafico bonitinho
"""
class Tratamento(object):
    pass


#nessa classe onde vai ser plotado o grafico
class Plotar(object):
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()