import pygame
from pygame.locals import *
from random import randint
from random import choice
from time import sleep
from sys import exit

def TicTacToe():
	#Funções
	def ganhou(j):
		if posicao[0] == posicao[1] == posicao[2] == j: return True
		elif posicao[3] == posicao[4] == posicao[5] == j: return True
		elif posicao[6] == posicao[7] == posicao[8] == j: return True
		elif posicao[0] == posicao[3] == posicao[6] == j: return True
		elif posicao[1] == posicao[4] == posicao[7] == j: return True
		elif posicao[2] == posicao[5] == posicao[8] == j: return True
		elif posicao[0] == posicao[4] == posicao[8] == j: return True
		elif posicao[2] == posicao[4] == posicao[6] == j: return True
		else: return False
	#Variáveis
	jogador = 'O'
	proximo = 'X'
	memoria = list()
	posicao = ['']*9
	#Inicialização
	pygame.display.set_caption('Tic-Tac-Toe')
	tela = pygame.display.set_mode((330,330))
	#Loop
	while True:
		tela.fill(PRETO)
		#Tabuleiro
		pygame.draw.line(tela, BRANCO, (111,10), (111,319), 3)
		pygame.draw.line(tela, BRANCO, (215,10), (215,319), 3)
		pygame.draw.line(tela, BRANCO, (10,111), (319,111), 3)
		pygame.draw.line(tela, BRANCO, (10,215), (319,215), 3)
		#Colisores
		colisor1 = pygame.draw.rect(tela, PRETO, (10,10,100,100))
		colisor2 = pygame.draw.rect(tela, PRETO, (113,10,101,100))
		colisor3 = pygame.draw.rect(tela, PRETO, (217,10,102,100))
		colisor4 = pygame.draw.rect(tela, PRETO, (10,113,100,101))
		colisor5 = pygame.draw.rect(tela, PRETO, (113,113,101,101))
		colisor6 = pygame.draw.rect(tela, PRETO, (217,113,102,101))
		colisor7 = pygame.draw.rect(tela, PRETO, (10,217,100,102))
		colisor8 = pygame.draw.rect(tela, PRETO, (113,217,101,102))
		colisor9 = pygame.draw.rect(tela, PRETO, (217,217,102,102))
		#TratadorDeEventos
		for evento in pygame.event.get():
			if evento.type == QUIT: pygame.quit(); exit()
			if evento.type == MOUSEBUTTONUP:
				ponto = pygame.mouse.get_pos()
				pygame.mixer.music.load('sounds/click.mp3')
				pygame.mixer.music.play()
				if colisor1.collidepoint(ponto) and posicao[0]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,60,60])
					posicao[0] = jogador
				elif colisor2.collidepoint(ponto) and posicao[1]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,165,60])
					posicao[1] = jogador
				elif colisor3.collidepoint(ponto) and posicao[2]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,269,60])
					posicao[2] = jogador
				elif colisor4.collidepoint(ponto) and posicao[3]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,60,165])
					posicao[3] = jogador
				elif colisor5.collidepoint(ponto) and posicao[4]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,165,165])
					posicao[4] = jogador
				elif colisor6.collidepoint(ponto) and posicao[5]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,269,165])
					posicao[5] = jogador
				elif colisor7.collidepoint(ponto) and posicao[6]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,60,269])
					posicao[6] = jogador
				elif colisor8.collidepoint(ponto) and posicao[7]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,165,269])
					posicao[7] = jogador
				elif colisor9.collidepoint(ponto) and posicao[8]=='':
					jogador, proximo = proximo, jogador
					memoria.append([jogador,269,269])
					posicao[8] = jogador
		#Desenhos
		for desenho, x, y in memoria:
			if desenho == 'X':
				pygame.draw.line(tela, BRANCO, (x-40,y-40), (x+40,y+40), 3)
				pygame.draw.line(tela, BRANCO, (x+40,y-40), (x-40,y+40), 3)
			elif desenho == 'O':
				pygame.draw.circle(tela, BRANCO, (x,y), 40)
				pygame.draw.circle(tela, PRETO, (x,y), 37)
		#Finalização
		pygame.display.update()
		if ganhou('X'): mensagem = 'X Ganhou!'; break
		elif ganhou('O'): mensagem = 'O Ganhou!'; break
		elif len(memoria)==9: mensagem = 'Empate!'; break
	sleep(2); tela.fill(PRETO)
	x,y = pygame.font.Font.size(FONTE2, mensagem)
	texto = FONTE2.render(mensagem, True, (255,255,255))
	tela.blit(texto, (164-x//2,165-y//2))
	pygame.display.update()
	pygame.mixer.music.load('sounds/win.mp3')
	pygame.mixer.music.play(); sleep(3)
	tela = pygame.display.set_mode((400,400))


def PingPong():
	#Variáveis
	posJ1 = posJ2 = 160
	pontosJ1 = pontosJ2 = 0
	tempo,cont,mult,vel = 3,0,1,0.5
	vely = choice([-vel,vel])
	velx = choice([-vel,vel])
	posy = randint(50,350)
	posx = 400
	#Inicialização
	pygame.display.set_caption('Ping-Pong')
	tela = pygame.display.set_mode((800,400))
	#Loop
	while True:
		tela.fill(PRETO)
		#TratadorDeEventos
		for evento in pygame.event.get():
			if evento.type == QUIT: pygame.quit(); exit()
		#MovimentoDoJogador1
		if posJ1 > 1 and pygame.key.get_pressed()[K_w]: posJ1 -= 1
		if posJ1 < 320 and pygame.key.get_pressed()[K_s]: posJ1 += 1
		#MovimentoDoJogador2
		if posJ2 > 1 and pygame.key.get_pressed()[K_UP]: posJ2 -= 1
		if posJ2 < 320 and pygame.key.get_pressed()[K_DOWN]: posJ2 += 1
		#MovimentoDaBola
		if posx >= 785:
			vel = 0.5
			pontosJ1 += 1
			posx = 160
			posy = randint(75,325)
			vely = choice([-vel,vel])
			velx = vel
			tempo = 3
			sleep(2)
		if posx <= 0:
			vel = 0.5
			pontosJ2 += 1
			posx = 640
			posy = randint(50,350)
			vely = choice([-vel,vel])
			velx = -vel
			tempo = 3
			sleep(2)
		if posy >= 385 or posy <= 0: vely = -vely
		posx += velx; posy += vely
		#Desenhos
		bola = pygame.draw.circle(tela, BRANCO, (posx,posy), 15)
		jogador1 = pygame.draw.rect(tela, VERMELHO, (0,posJ1,20,80))
		jogador2 = pygame.draw.rect(tela, VERDE, (780,posJ2,20,80))
		pygame.draw.line(tela, AMARELO, (0,398), (800,398), 3)
		pygame.draw.line(tela, AMARELO, (0,1), (800,1), 3)
		#Colisões
		if jogador1.colliderect(bola):
			pygame.mixer.music.load('sounds/ball.mp3')
			pygame.mixer.music.play()
			velx = vel; cont += 1
		if jogador2.colliderect(bola):
			pygame.mixer.music.load('sounds/ball.mp3')
			pygame.mixer.music.play()
			velx = -vel; cont += 1
		if cont == 8*mult: vel += 0.5; mult += 1
		#Textos
		x,_ = pygame.font.Font.size(FONTE2, str(pontosJ1))
		texto1 = FONTE2.render(str(pontosJ1), True, BRANCO)
		texto2 = FONTE2.render(str(pontosJ2), True, BRANCO)
		tela.blit(texto1, (385-x,15))
		tela.blit(texto2, (415,15))
		#Finalização
		pygame.display.update()
		if pontosJ1 == 3: mensagem = 'Jogador1 Ganhou!'; break
		elif pontosJ2 == 3: mensagem = 'Jogador2 Ganhou!'; break
		while tempo != 0: sleep(1); tempo -= 1
	x,y = pygame.font.Font.size(FONTE2, mensagem)
	texto = FONTE2.render(mensagem, True, BRANCO)
	tela.blit(texto, (400-x//2,200-y//2))
	pygame.display.update()
	pygame.mixer.music.load('sounds/win.mp3')
	pygame.mixer.music.play(); sleep(3)
	tela = pygame.display.set_mode((400,400))


def Creditos():
	voltar = False
	pygame.mixer.music.load('sounds/win.mp3')
	pygame.mixer.music.play()
	while True:
		tela.fill(PRETO)
		#Textos
		titulo = FONTE1.render('Two Players!!', True, BRANCO)
		texto1 = FONTE3.render('Universidade Federal do Maranhão', True, BRANCO)
		texto2 = FONTE3.render('CCET - DEINF - Algoritmo I', True, BRANCO)
		texto3 = FONTE3.render('Version 1.2.2 de 2021.2', True, BRANCO)
		texto4 = FONTE3.render('Developed by Rick-Eick', True, BRANCO)
		texto5 = FONTE3.render('Powered by Pygame', True, BRANCO)
		texto6 = FONTE3.render('∘ Voltar ∘', True, BRANCO)
		x0,y0 = pygame.font.Font.size(FONTE1, 'Two Players!!')
		x1,y1 = pygame.font.Font.size(FONTE3, 'Universidade Federal do Maranhão')
		x2,y2 = pygame.font.Font.size(FONTE3, 'CCET - DEINF - Algoritmo I')
		x3,y3 = pygame.font.Font.size(FONTE3, 'Version 1.2.2 of 2021.2')
		x4,y4 = pygame.font.Font.size(FONTE3, 'Developed by Rick-Eick')
		x5,y5 = pygame.font.Font.size(FONTE3, 'Powered by Pygame')
		x6,y6 = pygame.font.Font.size(FONTE3, '∘ Voltar ∘')
		colisor = pygame.draw.rect(tela, PRETO, (200-x6//2,70+y0+y1*5,x6,y6))
		tela.blit(titulo, (200-x0//2,10))
		tela.blit(texto1, (200-x1//2,20+y0))
		tela.blit(texto2, (200-x2//2,30+y0+y1*1))
		tela.blit(texto3, (200-x3//2,40+y0+y1*2))
		tela.blit(texto4, (200-x4//2,50+y0+y1*3))
		tela.blit(texto5, (200-x5//2,60+y0+y1*4))
		tela.blit(texto6, (200-x6//2,70+y0+y1*5))
		#TratadorDeEventos
		for evento in pygame.event.get():
			if evento.type == QUIT: pygame.quit(); exit()
			if evento.type == MOUSEBUTTONUP:
				ponto = pygame.mouse.get_pos()
				if colisor.collidepoint(ponto): voltar = True
		#Finalização
		pygame.display.update()
		if voltar: break


#Inicialização
pygame.init()
pygame.display.set_caption('Two Players')
tela = pygame.display.set_mode((400,400))
#Fontes
FONTE1 = pygame.font.SysFont('Arial', 50, True, False)
FONTE2 = pygame.font.SysFont('Arial', 30, True, False)
FONTE3 = pygame.font.SysFont('Arial', 20, True, False)
#Cores
PRETO = (0,0,0)
VERDE = (0,255,0)
VERMELHO = (255,0,0)
AMARELO = (255,255,0)
BRANCO = (255,255,255)
#LoopPrincipal
while True:
	tela.fill(PRETO)
	#Textos
	titulo = FONTE1.render('Two Players!!', True, BRANCO)
	opcao1 = FONTE2.render('∘ Tic-Tac-Toe ∘', True, BRANCO)
	opcao2 = FONTE2.render('∘ Ping-Pong ∘', True, BRANCO)
	opcao3 = FONTE2.render('∘ Créditos ∘', True, BRANCO)
	x0,y0 = pygame.font.Font.size(FONTE1, 'Two Players!!')
	x1,y1 = pygame.font.Font.size(FONTE2, '∘ Tic-Tac-Toe ∘')
	x2,y2 = pygame.font.Font.size(FONTE2, '∘ Ping-Pong ∘')
	x3,y3 = pygame.font.Font.size(FONTE2, '∘ Créditos ∘')
	#Colisores
	tictactoe = pygame.draw.rect(tela, PRETO, (200-x1//2,40+y0,x1,y1))
	pingpong = pygame.draw.rect(tela, PRETO, (200-x2//2,70+y0+y1,x2,y2))
	creditos = pygame.draw.rect(tela, PRETO, (200-x3//2,100+y0+y1+y2,x3,y3))
	#Blits
	tela.blit(titulo, (200-x0//2,10))
	tela.blit(opcao1, (200-x1//2,40+y0))
	tela.blit(opcao2, (200-x2//2,70+y0+y1))
	tela.blit(opcao3, (200-x3//2,100+y0+y1+y2))
	#TratadorDeEventos
	for evento in pygame.event.get():
		if evento.type == QUIT: pygame.quit(); exit()
		if evento.type == MOUSEBUTTONUP:
			ponto = pygame.mouse.get_pos()
			if tictactoe.collidepoint(ponto): TicTacToe()
			elif pingpong.collidepoint(ponto): PingPong()
			elif creditos.collidepoint(ponto): Creditos()
	#Finalização
	pygame.display.update()
