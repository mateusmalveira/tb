# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 04:28:50 2016

@author: rafael
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
class GrapMinder(object):

    #classe inicial
    def __init__():# esse parenteses e o construtor
 		lista1 = []
 		lista2 = []
 		#transforma cada linha em uma string e salva tudo em uma lista_1 e Lista_2
		with open ( 'indicator hiv estimated prevalence% 15-49.csv' , 'rb' ) as csvfile :
			spamreader = csv . reader ( csvfile , delimiter = ' ' , quotechar = '|' )
			for row in spamreader :
				 lista1.append(', ' . join ( row ))    
        
		with open ( 'cell phone total.csv' , 'rb' ) as csvfile_2 :
			spamreader_1 = csv . reader ( csvfile_2 , delimiter = ' ' , quotechar = '|' )
			for I in spamreader_1 :
				 lista2.append(', ' . join ( I ))
		plotar().show()


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
    #plt.show()
