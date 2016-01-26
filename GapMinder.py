# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 04:28:50 2016

@author: rafael
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv
#classe inscial
class Inicio(object):

    #classe inicial
    def __init__(self):# esse parenteses e o construtor
        __lista1 = []
        __lista2 = []
        #transforma cada linha em uma string e salva tudo em uma lista_1 e Lista_2
        with open ( 'indicator hiv estimated prevalence% 15-49.csv' , 'rb' ) as csvfile :
            spamreader = csv . reader ( csvfile , delimiter = ' ' , quotechar = '|' )
            for row in spamreader :
                __lista1.append(', ' . join ( row ))
        with open ( 'cell phone total.csv' , 'rb' ) as csvfile_2 :
            spamreader_1 = csv . reader ( csvfile_2 , delimiter = ' ' , quotechar = '|' )
            for I in spamreader_1 :
                __lista2.append(', ' . join ( I ))
        Tratamento(__lista1,__lista2)


#tratamento dos dados
class Tratamento(object):
	def __init__(self,a,b):
		"""

		:rtype: object
		"""
		Anos_0 = []
		Anos_1 = []
		Pais_ST_0 = []
		Pais_ST_1 = []
		#fatia a primeira camada Titulo e Anos
		for i in range(len(a)):
			Tratamento_1 = []
			if i == 0 :
				Anos_0.append(a[i].split(','))
			if i != 0 :
				Tratamento_1.append(a[i])
				for i in range(len(Tratamento_1)):
					Pais_ST_0.append(Tratamento_1[i].split(','))

		for i in range(len(b)):
			Tratamento = []
			if i == 0 :
				Anos_1.append(b[i].split(','))
			if i != 0 :
				Tratamento.append(b[i])
				for i in range(len(Tratamento)):
					Pais_ST_1.append(Tratamento[i].split(','))


		Cort = Corte()
		titulo,anos = Cort.titulo(Anos_0)
		titulo1,anos1 = Cort.titulo(Anos_1)
		paises,St = Cort.Pais(Pais_ST_0)
		paises1,St1 = Cort.Pais(Pais_ST_1)

		Garfico1 = Plotar(titulo,anos,paises,St)
		Garfico2 = Plotar(titulo1,anos1,paises1,St1)

#corte das listas
class Corte():
    def titulo(self,a):
		x = a
		Titulos = x[0].pop(0)
		return Titulos,x
    def Pais(self,b):
        Paises = []
        z = b
        for I in range(len(z)):
            Paises.append(z[I].pop(0))
        return Paises,z


class Plotar():
    def __init__(self,T,A,P,S):
		def _update_plot(i, fig, scat):
			scat.set_offsets(([300, i],[250, i],[2100, i]))
			print('Frames: %d' %i)

			return scat,

		fig =  plt.figure()
		x = [1,2,3,4]
		y = [0,0,0,0]
		b = A[0][0]
		bc = A[0][len(A[0])-1]
		print bc
		b = int(b)
		bc = int(bc)
		ax = fig.add_subplot(111)
		ax.grid(True, linestyle = '-', color = '0.75')
		ax.set_xlim([0 , 1000])
		ax.set_ylim([b , bc])

		#instancia do grafico Dispersão
		scat = plt.scatter(x, y, c = x)
		
		plt.title(T)
		plt.ylabel("Anos")
		#seta alpha
		scat.set_alpha(0.8)
		plt.grid(False)
		#instancia da função animação recebe uma instancia de figura,uma instancia do grafico,
		anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat),frames = 100, interval = 100)
		#Mostra o Grafico
		plt.show()

Inicio()
