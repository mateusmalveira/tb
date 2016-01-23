# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 04:28:50 2016

@author: rafael
"""
import numpy as np
import matplotlib.pyplot as plt

class GrapMinder(object):


    def __init__():
        dataset_1 = open('indicator hiv estimated prevalence% 15-49.csv','r')
        dataset_2 = open('cell phone total.csv','r')
        pl = plotar()






class Tratamento(object):
    pass

class Plotar(object):
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()