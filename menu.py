# coding: utf-8
# Projeto desenvolvido como projeto final da disciplina de Lp1 na UFCG - Campus Campina Grande
# Abel Antunes
# 117210287
# abel.neto

import pygame, sys
from pygame import *

# Valores constantes.
altura = 800
largura = 1200

cor_preta = (0,0,0)
cor_branca = (255,255,255)
cor_azul = (108,194,236)
cor_cinza = (105,105,105)
cor_vermelha = (227,57,9)
cor_vermelho_claro = (249, 82, 82)
cor_azul_claro = (185, 193, 251)
cor_azul_escuro = (55, 55, 135)
cor_amarela = (248, 251, 8)

pygame.init()
tela = pygame.display.set_mode((largura,altura))
pygame.display.	set_caption('DAMAS')

class jogo():

	def __init__(self):
		self.status = 'jogando'
		self.turno = 1
		self.jogadores = ('x', 'o')
		self.pecas_azuis = 12
		self.pecas_vermelhas = 12
		self.peca_selecionada = None
		self.turno = 'azul'
		self.destino = None
		self.comidas = []
		self.comer = False
		self.x_ret = 0
		self.y_ret = 0
		self.vencedor = None 
		self.jogador1 = 'o'
		self.jogador2 = 'x'
		self.ret_pos = None
		self.lista_pos = []
		self.lista_pos_indice = []
		self.dama = 'da'
		self.dama2 = 'dv'
		self.diagonais_peca = []
		self.matriz_pecas = []
		self.tem_pra_comer_list = []
		self.quem_comeu = None
		self.matriz_jogadores = [['-','x','-','x','-','x','-','x'],
							 ['x','-','x','-','x','-','x','-'],
							 ['-','x','-','x','-','x','-','x'],
							 ['-','-','-','-','-','-','-','-'],
							 ['-','-','-','-','-','-','-','-'],
							 ['o','-','o','-','o','-','o','-'],
							 ['-','o','-','o','-','o','-','o'],
							 ['o','-','o','-','o','-','o','-']]
	
	lista_ret = []

	peca_selecionada = None
	destino = None
		
	# Desenhando pecas e tabuleiro.
	def desenha_jogo(self):
		
		pygame.font.init()					# Configurando fonte
		font = pygame.font.get_default_font()
		font_placar = pygame.font.SysFont(font, 100)
		
		mensagem_placar = 'Placar:'
		
		texto_placar = font_placar.render(mensagem_placar, 1, cor_branca)		#aparece na tela um texto
		
		tela.blit(texto_placar, (830,30))
		
		lista_pos = self.lista_pos
		
		# Muda a cor da possibilidade de jogada.
		if self.turno == 'azul':
			cor_pos = cor_azul_claro
		else:
			cor_pos = cor_vermelho_claro
			
		matriz = self.matriz_jogadores
		matriz_pecas = self.matriz_pecas 
		y = 0
		indice = -1
		ret_pos = self.ret_pos
		
		for l in range(len(matriz)):
			indice += 1
			lista = []
			matriz_pecas.append(lista)
			x = 0
			if l % 2 == 1:
				cor1 = cor_preta
				cor2 = cor_branca
			else:
				cor2 = cor_preta
				cor1 = cor_branca
		
			for c in range(len(matriz[l])):
				ret = pygame.Rect(x, y, 100, 100)
				matriz_pecas[indice].append(ret)
				
				
				if c % 2 == 0:
					pygame.draw.rect(tela, cor1, ret)
				
				else:
					pygame.draw.rect(tela, cor2, ret)	
		
				if self.ret_pos != None:
					for pos in lista_pos:
						ret = (pos[0], pos[1], 100, 100)
						pygame.draw.rect(tela, cor_pos, ret)
				
				if matriz[l][c] == 'o':
					pecao = (x + 50 , y + 50)
					pygame.draw.circle(tela,cor_azul,pecao, 40)
					
					
				elif matriz[l][c] == 'x':
					pecax = (x + 50 , y + 50)
					pygame.draw.circle(tela,cor_vermelha,pecax, 40)
					
				# Desenha as damas. 	
				elif matriz[l][c] == 'da':
					pecax = (x + 50 , y + 50)
					pygame.draw.circle(tela,cor_azul,pecax, 40)
					pygame.draw.circle(tela,cor_amarela,pecax, 10)
					
				elif matriz[l][c] == 'dv':
					pecax = (x + 50 , y + 50)
					pygame.draw.circle(tela,cor_vermelha,pecax, 40)
					pygame.draw.circle(tela,cor_amarela,pecax, 10)
						
				x += 100
					
			y += 100

	# Olhando onde foi clicado.	
	def analisa_click(self, (x, y)):		
		matriz_jogadores = self.matriz_jogadores
		matriz_pecas = self.matriz_pecas
		colidiu = 'nao'
		indice =  0
		indice2 = -1
				
		def diagonais_peca(self):
			peca_selecionada = self.peca_selecionada
			linha = peca_selecionada[0]
			coluna = peca_selecionada[1]
			self.diagonais_peca = []
			lista_diagonais = self.diagonais_peca
			
			var = 1
			while linha + var <= 7 and coluna + var <= 7:
				lista_diagonais.append((linha + var, coluna + var))
				var += 1
			
			var = 1
			while linha + var <= 7 and coluna - var >= 0:
				lista_diagonais.append((linha + var, coluna - var))
				var += 1
			
			var = 1
			while linha - var >= 0 and coluna + var <= 7:
				lista_diagonais.append((linha - var, coluna + var))
				var += 1
			
			var = 1
			while linha - var >= 0 and coluna - var >= 0:
				lista_diagonais.append((linha - var, coluna - var))
				var += 1
		
		def possibilidades(self):
		
			if self.peca_selecionada != None:	
				pec_s_l = self.peca_selecionada[0]
				pec_s_c = self.peca_selecionada[1]
				matriz = self.matriz_jogadores
				x = self.x_ret
				y = self.y_ret
				lista = self.lista_pos
				lista2 = self.lista_pos_indice
				x_pos = None
				comidas = self.comidas
				jogador1 = self.jogador1
				jogador2 = self.jogador2
				dama2 = self.dama2
				
				# Se for uma peça, olha se existe uma da outra equipe em posição que dê para comer.
				# Olhar a questão dos indices.
				
				if pec_s_l - 2 >= 0 and pec_s_c - 2 >= 0 and matriz[pec_s_l - 1][pec_s_c - 1] in (jogador2, dama2) and matriz[pec_s_l - 2][pec_s_c - 2] == '-' :
						x_pos = (x - 200)
						y_pos = (y - 200)
						lista.append((x_pos, y_pos))
						lista2.append ((pec_s_l - 2, pec_s_c - 2))
						self.comer = True
						self.muda_turno = 'nao'
						
				if pec_s_c + 2 <= 7 and pec_s_l - 2 >= 0 and matriz[pec_s_l - 1][pec_s_c + 1] in (jogador2, dama2) and matriz[pec_s_l - 2][pec_s_c + 2] == '-' and pec_s_l - 2 >= 0:
						x_pos = (x + 200)
						y_pos = (y - 200)
						lista.append((x_pos, y_pos))
						lista2.append ((pec_s_l - 2, pec_s_c + 2))
						self.comer = True
						self.muda_turno = 'nao'
						
				if pec_s_l + 2 <= 7 and pec_s_c + 2 <= 7 and matriz[pec_s_l + 1][pec_s_c + 1] in (jogador2, dama2) and matriz[pec_s_l + 2][pec_s_c + 2] == '-' :
						x_pos = (x + 200)
						y_pos = (y + 200)
						lista.append((x_pos, y_pos))
						lista2.append ((pec_s_l + 2, pec_s_c + 2))
						self.comer = True
						self.muda_turno = 'nao'
						
				if pec_s_l + 2 <= 7 and pec_s_c - 2 >= 0 and matriz[pec_s_l + 1][pec_s_c - 1] in (jogador2, dama2) and matriz[pec_s_l + 2][pec_s_c - 2] == '-' :
						x_pos = (x - 200)
						y_pos = (y + 200)
						lista.append((x_pos, y_pos))
						lista2.append ((pec_s_l + 2, pec_s_c - 2))
						self.comer = True
						self.muda_turno = 'nao'
				
				if 	matriz[pec_s_l][pec_s_c] == 'o':
						
					if self.comer != True:
						self.muda_turno = 'sim'
						if pec_s_l > 0 and pec_s_c > 0 and matriz[pec_s_l - 1][pec_s_c - 1] == '-':
							x_pos = (x - 100)
							y_pos = (y - 100)
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l - 1, pec_s_c - 1))		
									
						if pec_s_l > 0 and pec_s_c < 7 and matriz[pec_s_l - 1][pec_s_c + 1] == '-':
							x_pos = (x + 100)
							y_pos = (y - 100)
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l - 1, pec_s_c + 1))
						
						if x_pos != None:				
							self.ret_pos = (x_pos, y_pos, 100, 100)
					
				elif  pec_s_l >= 0 and pec_s_l <= 7 and pec_s_c >= 0 and pec_s_c <= 7 and matriz[pec_s_l][pec_s_c] == 'x':
					
					if self.comer != True:		
						if pec_s_l < 7 and pec_s_c > 0 and matriz[pec_s_l + 1][pec_s_c - 1] == '-':
							x_pos = (x - 100)
							y_pos = (y + 100)
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l + 1, pec_s_c - 1))
									
						if pec_s_l < 7 and pec_s_c < 7 and matriz[pec_s_l + 1][pec_s_c + 1] == '-':
							x_pos = (x + 100)
							y_pos = (y + 100)
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l + 1, pec_s_c + 1))
						
								
							self.ret_pos = (x_pos, y_pos, 100, 100)
	
									# Para poder clicar fora do tabuleiro.
				
				
		def possibilidades_dama(self):
		
			if self.peca_selecionada != None:	
				pec_s_l = self.peca_selecionada[0]
				pec_s_c = self.peca_selecionada[1]
				matriz = self.matriz_jogadores
				x = self.x_ret
				y = self.y_ret				
				dama = self.dama
				dama2 = self.dama2
				lista = self.lista_pos
				lista2 = self.lista_pos_indice
				x_pos = None
				comidas = self.comidas
				ja_limpou = False
				jogador1 = dama
				jogador2 = self.jogador2
				
				if 	matriz[pec_s_l][pec_s_c] in ('da', 'dv'):
						
					if pec_s_l > 0 and pec_s_c > 0:
							
						livres = 1
						while pec_s_l - livres >= 0 and pec_s_c - livres >= 0 and matriz[pec_s_l - livres][pec_s_c - livres] == '-':
							x_pos = (x - (100 * livres))
							y_pos = (y - (100 * livres))
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l - livres, pec_s_c - livres))		
							livres += 1
							
						# Olhar se tem para comer com a dama.
						if pec_s_l - livres >= 0 and pec_s_c - livres >= 0 and matriz[pec_s_l - livres][pec_s_c - livres] in (jogador2, dama2):
							if pec_s_l - (livres + 1) >= 0 and pec_s_c - (livres + 1) >= 0 and matriz[pec_s_l - (livres + 1)][pec_s_c - (livres + 1)] == '-':
								indice = pec_s_l - (livres + 1)
								indice2 = pec_s_c - (livres + 1)
								x_pos = (x - (100 * (livres + 1)))
								y_pos = (y - (100 * (livres + 1)))
									
								if ja_limpou == False:
									self.lista_pos = []
									self.lista_pos_indice = []
									ja_limpou = True
										
								self.lista_pos.append((x_pos, y_pos))
								self.lista_pos_indice.append((indice, indice2))	
								self.tem_pra_comer_list.append((indice, indice2))
									
								quant = 1
								livres = livres + 1
								while indice - quant >= 0 and indice2 - quant >= 0 and matriz[indice-quant][indice2-quant] == '-':
									x_pos = (x - (100 * (livres + quant)))
									y_pos = (y - (100 * (livres + quant)))
									self.lista_pos.append((x_pos, y_pos))
									self.lista_pos_indice.append((indice - quant, indice2 - quant))	
									self.tem_pra_comer_list.append((indice - quant, indice2 - quant))
									quant += 1
									
									
					if pec_s_l > 0 and pec_s_c < 7:
							
						livres = 1
						while pec_s_l - livres >= 0 and pec_s_c + livres <= 7 and matriz[pec_s_l - livres][pec_s_c + livres] == '-':
							x_pos = (x + (100 * livres))
							y_pos = (y - (100 * livres))
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l - livres, pec_s_c + livres))	
							livres += 1
								
							
						# Olhar se tem para comer com a dama.
						if pec_s_l - livres >= 0 and pec_s_c + livres <= 7 and matriz[pec_s_l - livres][pec_s_c + livres] in (jogador2, dama2):
							if pec_s_l - (livres + 1) >= 0 and pec_s_c + (livres + 1) <= 7 and matriz[pec_s_l - (livres + 1)][pec_s_c + (livres + 1)] == '-':
								indice = pec_s_l - (livres + 1)
								indice2 = pec_s_c + (livres + 1)
								x_pos = (x + (100 * (livres + 1)))
								y_pos = (y - (100 * (livres + 1)))
									
								if ja_limpou == False:
									self.lista_pos = []
									self.lista_pos_indice = []
									ja_limpou = True
								
								self.lista_pos.append((x_pos, y_pos))
								self.lista_pos_indice.append((indice, indice2))	
								self.tem_pra_comer_list.append((indice, indice2))
									
								quant = 1
								livres = livres + 1
								while indice - quant >= 0 and indice2 + quant <= 7 and matriz[indice-quant][indice2+quant] == '-':
									x_pos = (x + (100 * (livres + quant)))
									y_pos = (y - (100 * (livres + quant)))
									self.lista_pos.append((x_pos, y_pos))
									self.lista_pos_indice.append((indice - quant, indice2 + quant))	
									self.tem_pra_comer_list.append((indice - quant, indice2 + quant))
									quant += 1
									
							
					if pec_s_l < 7 and pec_s_c > 0:
							
						livres = 1
						while pec_s_l + livres <= 7 and pec_s_c - livres >= 0 and matriz[pec_s_l + livres][pec_s_c - livres] == '-':
							x_pos = (x - (100 * livres))
							y_pos = (y + (100 * livres))
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l + livres, pec_s_c - livres))		
							livres += 1
							
						# Olhar se tem para comer com a dama.
						if pec_s_l + livres <= 7 and pec_s_c - livres >= 0 and matriz[pec_s_l + livres][pec_s_c - livres] in (jogador2, dama2):
							if pec_s_l + (livres + 1) <= 7 and pec_s_c - (livres + 1) >= 0 and matriz[pec_s_l + (livres + 1)][pec_s_c - (livres + 1)] == '-':
								indice = pec_s_l + (livres + 1)
								indice2 = pec_s_c - (livres + 1)
								x_pos = (x - (100 * (livres + 1)))
								y_pos = (y + (100 * (livres + 1)))									
									
								if ja_limpou == False:
									self.lista_pos = []
									self.lista_pos_indice = []
									ja_limpou = True
									
								self.lista_pos.append((x_pos, y_pos))
								self.lista_pos_indice.append((indice, indice2))	
								self.tem_pra_comer_list.append((indice, indice2))
								
								quant = 1
								livres = livres + 1
								while indice + quant <= 7 and indice2 - quant >= 0 and matriz[indice+quant][indice2-quant] == '-':
									x_pos = (x - (100 * (livres + quant)))
									y_pos = (y + (100 * (livres + quant)))
									self.lista_pos.append((x_pos, y_pos))
									self.lista_pos_indice.append((indice + quant, indice2 - quant))	
									self.tem_pra_comer_list.append((indice + quant, indice2 - quant))
									quant += 1
						
							
					if pec_s_l < 7 and pec_s_c < 7:
						livres = 1
						while pec_s_l + livres <= 7 and pec_s_c + livres <= 7 and matriz[pec_s_l + livres][pec_s_c + livres] == '-':
							x_pos = (x + (100 * livres))
							y_pos = (y + (100 * livres))
							lista.append((x_pos, y_pos))
							lista2.append((pec_s_l + livres, pec_s_c + livres))	
							livres += 1		
						
						# Olhar se tem para comer com a dama.
						if pec_s_l + livres <= 7 and pec_s_c + livres <= 7 and matriz[pec_s_l + livres][pec_s_c + livres] in (jogador2, dama2):
							if pec_s_l + (livres + 1) <= 7 and pec_s_c + (livres + 1) <= 7 and matriz[pec_s_l + (livres + 1)][pec_s_c + (livres + 1)] == '-':
								indice = pec_s_l + (livres + 1)
								indice2 = pec_s_c + (livres + 1)
								x_pos = (x + (100 * (livres + 1)))
								y_pos = (y + (100 * (livres + 1)))
								
								if ja_limpou == False:
									self.lista_pos = []
									self.lista_pos_indice = []
									ja_limpou = True
									
								self.lista_pos.append((x_pos, y_pos))
								self.lista_pos_indice.append((indice, indice2))	
								self.tem_pra_comer_list.append((indice, indice2))
									
								quant = 1
								livres = livres + 1
								while indice + quant <= 7 and indice2 + quant <= 7 and matriz[indice+quant][indice2+quant] == '-':
									x_pos = (x + (100 * (livres + quant)))
									y_pos = (y + (100 * (livres + quant)))
									self.lista_pos.append((x_pos, y_pos))
									self.lista_pos_indice.append((indice + quant, indice2 + quant))	
									self.tem_pra_comer_list.append((indice + quant, indice2 + quant))
									quant += 1		
						
					if x_pos != None:				
						self.ret_pos = (x_pos, y_pos, 100, 100)
									
		while colidiu != 'sim' and indice <=7:
			indice2 += 1
			if matriz_pecas[indice][indice2].collidepoint(x, y):
				ret = matriz_pecas[indice][indice2]
				colidiu = 'sim'
	
			else:
				colidiu = 'nao'
				
			# Pelo indice da matriz de pecas acessa a matriz de jogadores.
			if indice2 > 7:
				indice += 1
				indice2 = -1
		
		# Pega os indices para trabalhar com eles no movimento.		
		if self.tem_pra_comer_list == []:
			if colidiu == 'sim' and ((matriz_jogadores[indice][indice2] in ('dv', 'x') and self.turno == 'vermelho') or (matriz_jogadores[indice][indice2] in ('da', 'o') and self.turno == 'azul')) and (self.destino == None):
				self.peca_selecionada = (indice, indice2) 
				diagonais_peca(self)
				
				# Pego o x e o y do retangulo selecionado.
				self.x_ret = ret[0]
				self.y_ret = ret[1]
			
		elif (indice, indice2) in self.tem_pra_comer_list:
			if colidiu == 'sim' and ((matriz_jogadores[indice][indice2] in ('dv', 'x') and self.turno == 'vermelho') or (matriz_jogadores[indice][indice2] in ('o', 'da') and self.turno == 'azul')) and (self.destino == None):
				self.peca_selecionada = (indice, indice2) 
				diagonais_peca(self)
				
				# Pego o x e o y do retangulo selecionado.
				self.x_ret = ret[0]
				self.y_ret = ret[1]	
		
		# Consertando erro de comer a peça mesmo depois de trocar a peça selecionada.
		else:
			self.peca_selecionada = None
			self.lista_pos = []
			self.lista_pos_indice = []
			self.destino = None
				
			# Troca a peça selecionada.
		if indice <= 7 and self.peca_selecionada != None and matriz_jogadores[indice][indice2] in (self.jogador1, self.dama) and (self.tem_pra_comer_list == [] or (indice, indice2) in self.tem_pra_comer_list):
			self.peca_selecionada = (indice, indice2)
			self.x_ret = ret[0]
			self.y_ret = ret[1]
			self.lista_pos = []
			self.lista_pos_indice = []
			self.destino = None
				
		# Chama as possibilidades das damas
		self.lista_pos = []
		
		if indice <= 7 and indice2 <= 7 and matriz_jogadores[indice][indice2]  in ('da', 'dv') and (self.tem_pra_comer_list == [] or (indice, indice2) in self.tem_pra_comer_list):
			possibilidades_dama(self)
		
		elif self.tem_pra_comer_list == [] or (indice, indice2) in self.tem_pra_comer_list:
			possibilidades(self)
		
		if self.peca_selecionada != None :
			self.destino = (indice, indice2)
	
	def movimento(self):
		
		# Função que olha se é obrigado comer uma peça.
		def tem_pra_comer(self):
			matriz_jogadores = self.matriz_jogadores
			jogador1 = self.jogador1
			jogador2 = self.jogador2
			dama = self.dama
			dama2 = self.dama2
			lista = self.tem_pra_comer_list
			
			
			for l in range(len(matriz_jogadores)):
				for c in range(len(matriz_jogadores[0])):
					if matriz_jogadores[l][c] == jogador1 and (l+1 <= 7 and c+1 <=7 and matriz_jogadores[l+1][c+1] in (jogador2, dama2)) and (l+2 <=7 and c+2 <= 7 and matriz_jogadores[l+2][c+2] == '-'):
						lista.append((l, c))
						
					if matriz_jogadores[l][c] == jogador1 and (l+1 <= 7 and c-1 >=0 and matriz_jogadores[l+1][c-1] in (jogador2, dama2)) and (l+2 <=7 and c-2 >= 0 and matriz_jogadores[l+2][c-2] == '-'):
						lista.append((l, c))
						
					if matriz_jogadores[l][c] == jogador1 and (l-1 >= 0 and c+1 <=7 and matriz_jogadores[l-1][c+1] in (jogador2, dama2)) and (l-2 >= 0 and c+2 <= 7 and matriz_jogadores[l-2][c+2] == '-'):
						lista.append((l, c))
						
					if matriz_jogadores[l][c] == jogador1 and (l-1 >= 0 and c-1 >=0 and matriz_jogadores[l-1][c-1] in (jogador2, dama2)) and (l-2 >=0 and c-2 >= 0 and matriz_jogadores[l-2][c-2] == '-'):
						lista.append((l, c))
					
					if matriz_jogadores[l][c] == dama:
						pec_s_l = l
						pec_s_c = c
						
						if pec_s_l > 0 and pec_s_c > 0:
							livres = 1
							while pec_s_l - livres >= 0 and pec_s_c - livres >= 0 and matriz[pec_s_l - livres][pec_s_c - livres] == '-':		
								livres += 1
							
							# Olhar se tem para comer com a dama.
							if pec_s_l - livres >= 0 and pec_s_c - livres >= 0 and matriz[pec_s_l - livres][pec_s_c - livres] in (jogador2, dama2):
								if pec_s_l - (livres + 1) >= 0 and pec_s_c - (livres + 1) >= 0 and matriz[pec_s_l - (livres + 1)][pec_s_c - (livres + 1)] == '-':
									lista.append((l, c))	
									
						if pec_s_l > 0 and pec_s_c < 7:
							livres = 1
							while pec_s_l - livres >= 0 and pec_s_c + livres <= 7 and matriz[pec_s_l - livres][pec_s_c + livres] == '-':
								livres += 1
								
							# Olhar se tem para comer com a dama.
							if pec_s_l - livres >= 0 and pec_s_c + livres <= 7 and matriz[pec_s_l - livres][pec_s_c + livres] in (jogador2, dama2):
								if pec_s_l - (livres + 1) >= 0 and pec_s_c + (livres + 1) <= 7 and matriz[pec_s_l - (livres + 1)][pec_s_c + (livres + 1)] == '-':
									lista.append((l, c))
										
						if pec_s_l < 7 and pec_s_c > 0:
							
							livres = 1
							while pec_s_l + livres <= 7 and pec_s_c - livres >= 0 and matriz[pec_s_l + livres][pec_s_c - livres] == '-':	
								livres += 1
							
							# Olhar se tem para comer com a dama.
							if pec_s_l + livres <= 7 and pec_s_c - livres >= 0 and matriz[pec_s_l + livres][pec_s_c - livres] in (jogador2, dama2):
								if pec_s_l + (livres + 1) <= 7 and pec_s_c - (livres + 1) >= 0 and matriz[pec_s_l + (livres + 1)][pec_s_c - (livres + 1)] == '-':
									lista.append((l, c))	
							
						if pec_s_l < 7 and pec_s_c < 7:
							livres = 1
							while pec_s_l + livres <= 7 and pec_s_c + livres <= 7 and matriz[pec_s_l + livres][pec_s_c + livres] == '-':
								livres += 1		
							
							# Olhar se tem para comer com a dama.
							if pec_s_l + livres <= 7 and pec_s_c + livres <= 7 and matriz[pec_s_l + livres][pec_s_c + livres] in (jogador2, dama2):
								if pec_s_l + (livres + 1) <= 7 and pec_s_c + (livres + 1) <= 7 and matriz[pec_s_l + (livres + 1)][pec_s_c + (livres + 1)] == '-':
									lista.append((l, c))	
							
		def pode_trocar_turno(self):
			
			self.tem_pra_comer_list = []
			tem_pra_comer(self)
			if self.tem_pra_comer_list == []:
				return True
			
			elif self.quem_comeu not in self.tem_pra_comer_list:
				return True
				 
			else:
				return False
				
					
		def troca_turno(self):
			pode_ser_dama_l = self.destino[0]
			pode_ser_dama_c = self.destino[1]
			matriz = self.matriz_jogadores
			
			if pode_trocar_turno(self) == True:
					
				if matriz[pode_ser_dama_l][pode_ser_dama_c] == 'o' and pode_ser_dama_l == 0:
					matriz[pode_ser_dama_l][pode_ser_dama_c] = 'da'
					
				elif matriz[pode_ser_dama_l][pode_ser_dama_c] == 'x' and pode_ser_dama_l == 7:
					matriz[pode_ser_dama_l][pode_ser_dama_c] = 'dv'
						
				# Come as peças possíveis antes de trocar de turno.	
				# Troca os turnos entre os jogadores após uma jogada.	
				if self.turno == 'azul':
					self.turno = 'vermelho'
					self.comer = False	
					self.lista_pos_indice = []
					self.comidas = []
					self.jogador1 = 'x'
					self.jogador2 = 'o'
					self.dama = 'dv'
					self.dama2 = 'da'
					self.tem_pra_comer_list = []
					tem_pra_comer(self)
					self.quem_comeu = None
							
				else:
					self.turno = 'azul'
					self.comer = False
					self.lista_pos_indice = []
					self.comidas = []
					self.dama = 'da'
					self.dama2 = 'dv'
					self.jogador1 = 'o'
					self.jogador2 = 'x'
					self.tem_pra_comer_list = []
					tem_pra_comer(self)
					self.quem_comeu = None
					
							
			else:
					
				self.lista_pos_indice = []
				self.comer = False
				self.comidas = []
				self.tem_pra_comer_list = []
				tem_pra_comer(self)
					
		
		
		# Olha se um movimento é válido antes de executa-lo
		def movimento_valido(self):
			# Começa aqui mov_valido.
			pec_s_l = self.peca_selecionada[0]
			pec_s_c = self.peca_selecionada[1]
			des_l = self.destino[0]
			des_c = self.destino[1]
			matriz = self.matriz_jogadores
		
			if matriz[pec_s_l][pec_s_c] == 'o':
				if self.destino in self.lista_pos_indice:	# Olha a validez pelos indices da matriz.
					return True
			
			elif matriz[pec_s_l][pec_s_c] == 'x':
				if self.destino in self.lista_pos_indice:	# Olha a validez pelos indices da matriz.
					return True
			
			
			elif matriz[pec_s_l][pec_s_c] in ('da', 'dv'):
				if self.destino in self.lista_pos_indice:	# Olha a validez pelos indices da matriz.
					return True		
		
		if self.peca_selecionada != None and self.destino != None:
			matriz = self.matriz_jogadores
			pec_s_l = self.peca_selecionada[0]
			pec_s_c = self.peca_selecionada[1]
			des_l = self.destino[0]
			des_c = self.destino[1]
			destino = self.destino
			dama2 = self.dama2
			jogador2 = self.jogador2
			
			# Trocando a peca de lugar usando os indices.
			if movimento_valido(self):
				des_l_temp = des_l
				des_c_temp = des_c
				
				matriz[pec_s_l][pec_s_c], matriz[des_l][des_c] =  matriz[des_l][des_c], matriz[pec_s_l][pec_s_c]
				
				# Comendo apenas as peças saltadas, inclusive com damas.
				comidas = self.comidas
				for l in range(len(matriz)):
					for c in range(len(matriz[0])):
						if matriz[l][c] in (jogador2, dama2) and pec_s_l < l < des_l and pec_s_c < c < des_c and (l, c) in self.diagonais_peca:
							comidas.append((l, c)) 
							self.quem_comeu = (des_l, des_c)
							
						elif matriz[l][c] in (jogador2, dama2) and pec_s_l > l > des_l and pec_s_c > c > des_c and (l, c) in self.diagonais_peca:
							comidas.append((l, c))
							self.quem_comeu = (des_l, des_c)
							
						elif matriz[l][c] in (jogador2, dama2) and pec_s_l > l > des_l and pec_s_c < c < des_c and (l, c) in self.diagonais_peca:
							comidas.append((l, c))
							self.quem_comeu = (des_l, des_c)
							
						elif matriz[l][c] in (jogador2, dama2) and pec_s_l < l < des_l and pec_s_c > c > des_c and (l, c) in self.diagonais_peca:
							comidas.append((l, c))
							self.quem_comeu = (des_l, des_c)
				
				if self.comidas == []:			
					troca_turno(self)
					
					
				else:
					for c in comidas:
						linha = c[0]
						coluna = c[1]
						if matriz[linha][coluna] in ('o', 'da'):
							self.pecas_azuis -= 1
						
						else:
							self.pecas_vermelhas -= 1
						
						matriz[linha][coluna] = '-'
					
					self.comidas = []
					troca_turno(self)
				
				if self.pecas_azuis == 0:
					self.vencedor = 'VERMELHO'
				
				elif self.pecas_vermelhas == 0:
					self.vencedor = 'AZUL'	
				
				self.lista_pos = []	
				self.peca_selecionada = None
				self.destino = None
		
	def menu(self):
		
		relogio = pygame.time.Clock()  # fps
		tela.fill(cor_preta)
		
		pygame.font.init()					# Configurando fonte
		font = pygame.font.get_default_font()
		font_titulo = pygame.font.SysFont(font, 130)
		font_iniciar = pygame.font.SysFont(font, 50)
		font_reiniciar = pygame.font.SysFont(font, 40)
		font_sair = pygame.font.SysFont(font, 40)
				
		
		mensagem = 'JOGO DE DAMAS'
		mensagem_iniciar = 'Iniciar partida'
		mensagem_reiniciar = 'Jogar Novamente'
		mensagem_sair = 'Sair do jogo'
		
		texto = font_titulo.render(mensagem, 1, cor_branca)		#aparece na tela um texto
		texto_sair = font_sair.render(mensagem_sair, 1, cor_branca)
		
		sair = font_sair.render(mensagem_sair, 1, cor_branca)
		iniciar = font_iniciar.render(mensagem_iniciar, 1, cor_branca)
		reiniciar = font_reiniciar.render(mensagem_reiniciar, 1, cor_branca)
		
		tela.blit(texto, (210,10))
		
		
		ret_iniciar = pygame.Rect(50, 300, 300, 100)
		ret_sair = pygame.Rect(850, 300, 300, 100)
		pygame.draw.rect(tela, cor_cinza, ret_iniciar)
		pygame.draw.rect(tela, cor_cinza, ret_sair)
		
		tela.blit(iniciar, (85, 330))
		tela.blit(sair, (920,330))
		
		def ganhou(self):
				
			tela.fill(cor_preta)
				
			ganhador = self.vencedor
				
			mensagem = 'VENCEDOR: '
			mensagem += ganhador
			texto = font_titulo.render(mensagem, 1, cor_branca)		#aparece na tela um texto
				
			tela.blit(texto, (50,20))
				
			ret_reiniciar = pygame.Rect(50, 300, 300, 100)
				
			pygame.draw.rect(tela, cor_cinza, ret_reiniciar)
			pygame.draw.rect(tela, cor_cinza, ret_sair)
			tela.blit(reiniciar, (75, 330))
			tela.blit(sair, (920,330))
		
		def olha_clique_menu(ret_iniciar, (x, y)):
			if ret_iniciar.collidepoint(x, y):
						damas()
			elif ret_sair.collidepoint(x, y):
				sys.exit()
		
		while True:
			relogio.tick(100) # Taxa de FPS.
			
			if self.vencedor != None:
				ganhou(self)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				
				if event.type == MOUSEBUTTONDOWN:
					(x, y) = pygame.mouse.get_pos()
					olha_clique_menu(ret_iniciar, (x, y))
						
			pygame.display.update()	

			
				
# loop do jogo.	
def damas():

	jogo2 = jogo()
	
	relogio = pygame.time.Clock()  # fps
	while True:
		
		if jogo2.vencedor != None:
			jogo2.menu()
			
		relogio.tick(100) # Taxa de FPS.
		tela.fill(cor_azul_escuro)
		jogo2.desenha_jogo()
		jogo2.movimento()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == MOUSEBUTTONDOWN:
				jogo2.analisa_click(pygame.mouse.get_pos())
		pygame.display.update()
	
jogo().menu()


