#Importações
import pygame
from pygame.locals import *
from time import sleep
from sys import exit
#Funções
def ganhou(char):
	if posicao[0] == posicao[1] == posicao[2] == char: return True
	elif posicao[3] == posicao[4] == posicao[5] == char: return True
	elif posicao[6] == posicao[7] == posicao[8] == char: return True
	elif posicao[0] == posicao[3] == posicao[6] == char: return True
	elif posicao[1] == posicao[4] == posicao[7] == char: return True
	elif posicao[2] == posicao[5] == posicao[8] == char: return True
	elif posicao[0] == posicao[4] == posicao[8] == char: return True
	elif posicao[2] == posicao[4] == posicao[6] == char: return True
	else: return False
#Variáveis
jogador = 'O'
proximo = 'X'
memoria = list()
posicao = ['']*9
#Inicialização
pygame.init()
pygame.display.set_caption('Tic-Tac-Toe')
tela = pygame.display.set_mode((329,329))
fonte = pygame.font.SysFont('Arial', 30, True, False)
#LoopPrincipal
while True:
	tela.fill((0,0,0))
	#Tabuleiro
	pygame.draw.line(tela, (255,255,255), (111,10), (111,319), 3)
	pygame.draw.line(tela, (255,255,255), (215,10), (215,319), 3)
	pygame.draw.line(tela, (255,255,255), (10,111), (319,111), 3)
	pygame.draw.line(tela, (255,255,255), (10,215), (319,215), 3)
	#Colisores
	colisor1 = pygame.draw.rect(tela, (0,0,0), (10,10,100,100))
	colisor2 = pygame.draw.rect(tela, (0,0,0), (113,10,101,100))
	colisor3 = pygame.draw.rect(tela, (0,0,0), (217,10,102,100))
	colisor4 = pygame.draw.rect(tela, (0,0,0), (10,113,100,101))
	colisor5 = pygame.draw.rect(tela, (0,0,0), (113,113,101,101))
	colisor6 = pygame.draw.rect(tela, (0,0,0), (217,113,102,101))
	colisor7 = pygame.draw.rect(tela, (0,0,0), (10,217,100,102))
	colisor8 = pygame.draw.rect(tela, (0,0,0), (113,217,101,102))
	colisor9 = pygame.draw.rect(tela, (0,0,0), (217,217,102,102))
	#TratadorDeEventos
	for evento in pygame.event.get():
		if evento.type == QUIT: pygame.quit(); exit()
		if evento.type == MOUSEBUTTONUP:
			ponto = pygame.mouse.get_pos()
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
			pygame.draw.line(tela, (255,255,255), (x-40,y-40), (x+40,y+40), 3)
			pygame.draw.line(tela, (255,255,255), (x+40,y-40), (x-40,y+40), 3)
		elif desenho == 'O':
			pygame.draw.circle(tela, (255,255,255), (x,y), 40)
			pygame.draw.circle(tela, (0,0,0), (x,y), 37)
	#Finalização
	pygame.display.update()
	if ganhou('X'): mensagem = 'X Ganhou!'; break
	elif ganhou('O'): mensagem = 'O Ganhou!'; break
	elif len(memoria)==9: mensagem = 'Empate!'; break
sleep(2); tela.fill((0,0,0))
x,y = pygame.font.Font.size(fonte, mensagem)
texto = fonte.render(mensagem, True, (255,255,255))
tela.blit(texto, (164-x//2,165-y//2))
pygame.display.update(); sleep(2)
pygame.quit(); exit()
