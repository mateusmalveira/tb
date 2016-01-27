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
		#instancia de pyplot.figure
		fig =  plt.figure()
		#esqueci pra que serve so sei que era importante
		x = [2009, 2010, 2011]
		y = [0,0,0]
		
		#pega o primero ano
		b = A[0][0]
		#pega o ultimo ano
		bc = A[0][len(A[0])-1]
		
		#converte pra inteiro 
		b = int(b)
		bc = int(bc)
		
		#define o tamanho do grafico na verdade adiciona um sube grafico ao grafico e da o tamanho do mesmo
		ax = fig.add_subplot(111)
		ax.grid(True, linestyle = '-', color = '0.75') #seta a grade
		ax.set_xlim([b , bc ])# limites em x
		ax.set_ylim([0 , 100 ])# limites e y
		#define função _update_plot responsavel por adicionar as bolas e printar os frames retorna uma instancia do grafico de disperção
		def _update_plot(i, fig, scat):
			scat.set_offsets(([1980, i],[1985, i],[1990, i],[1995, i],[2000, i],[2005 ,i],[2010, i]))# seta a linha em x que a bola vai trilhar e cria as bolas
			print('Frames: %d' %i)
			return scat,

		#instancia do grafico Dispersão
		scat = plt.scatter(x, y, s = 2000 , c = x)
		#seta titulo e nome do x 
		plt.title(T)
		plt.xlabel("Anos")
		
		scat.set_alpha(0.8) #seta alpha
		
		#instancia da função animação recebe uma instancia de figura,uma instancia do grafico, aumentando o numero de frames, é mostrado mais grafico
		#só que devese diminuir mt o intervalo ou o grafico ica muito lento 
		anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat),frames = 60000, )
		#Mostra o Grafico
		plt.show()

Inicio()
