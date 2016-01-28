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
        with open ( 'indicator hiv estimated prevalence% 15-49-america.csv' , 'rb' ) as csvfile :
            spamreader = csv . reader ( csvfile , delimiter = ' ' , quotechar = '|' )
            for row in spamreader :
                __lista1.append(', ' . join ( row ))
        with open ( 'cell phone total-America.csv' , 'rb' ) as csvfile_2 :
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
		selec = 0 
		
		while True :
			for I in range(len(paises)):
				print(I ,' -> ',paises[I])
			print "Escolha um país a ser plotado :"
			raw_input(selec)
			if selec >= 0 | selec <= (len(paises) - 1): break
		
		
		
		Garfico1 = Plotar(titulo,anos,paises,St,selec)
		Garfico2 = Plotar(titulo1,anos1,paises1,St1,selec)

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
    def __init__(self,T,A,P,S,selec):
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
		x1 = int(b)
		x2 = int(bc)
		 
		
		#define o tamanho do grafico na verdade adiciona um sube grafico ao grafico e da o tamanho do mesmo
		ax = fig.add_subplot(111)
		
		ax.grid(True, linestyle = '-', color = '0.75') #seta a grade
		
		ax.set_xlim([x1 , x2 ])# limites em x
		ax.set_ylim([0 , 1000 ])# limites e y
		
		#define função _update_plot responsavel por adicionar as bolas e printar os frames retorna uma instancia do grafico de disperção
		def _update_plot(i, fig, scat):
			s = [[1979, i ],[1980, i ],[1981, i ],[1982, i ],[1983, i ],[1984, i ],[1985, i ],[1986, i ],[1987, i ],[1988, i ],[1989, i ],[1990, i ],[1991, i ],[1992, i ],[1993, i ],[1994, i ],[1995, i ],[1996, i ],[1997, i ],[1998, i ],[1999, i ],[2000, i ],[2001, i ],[2002, i ],[2003, i ],[2004, i ],[2005, i ],[2006, i ],[2007, i ],[2008, i ],[2009, i ],[2010, i ],[2011, i ]]
			scat.set_offsets(s)# seta a linha em x que a bola vai trilhar e cria as bolas
			return scat,
		
		estatisricas = [] 	
		for I in range(len(A[0])):
			estatisricas.append(float(S[selec][I])) # recebe a linha de estatisticas do país selecionado 
			
		#instancia do grafico Dispersão
		scat = plt.scatter(x, y, s = estatisricas , c = x)
		
		#seta titulo e nome do x 
		plt.title(T)
		plt.xlabel("Anos")
		
		scat.set_alpha(0.8) #seta alpha
		
		#instancia da função animação recebe uma instancia de figura,uma instancia do grafico, aumentando o numero de frames, é mostrado mais grafico
		#só que devese diminuir mt o intervalo ou o grafico ica muito lento 
		anim = animation.FuncAnimation(fig, _update_plot, fargs = (fig, scat),frames = 10000, )
		#Mostra o Grafico
		plt.show()

Inicio()

