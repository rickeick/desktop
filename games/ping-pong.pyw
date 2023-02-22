#Importações
import pygame
from pygame.locals import *
from random import randint, choice
from time import sleep
from sys import exit
#ParâmetrosGerais
larMax, altMax = 800, 400
corTexto = (255,255,255)
corLinha = (255,255,0)
corFundo = (0,0,0)
#ParâmetrosDeControle
tempo = 3
cont = 0
mult = 1
vel = 0.5
#ParâmetrosDoJogador1
corJ1 = (255,0,0)
pontosJ1 = 0
posJ1 = 150
larJ1 = 20
altJ1 = 80
velJ1 = 1
#ParâmetrosDoJogador2
corJ2 = (0,255,0)
pontosJ2 = 0
posJ2 = 150
larJ2 = 20
altJ2 = 80
velJ2 = 1
#ParâmetrosDaBola
corBola = (255,255,255)
velx = choice([-vel,vel])
vely = choice([-vel,vel])
posy = randint(50,altMax-50)
posx = larMax//2
raio = 15
#Inicialização
pygame.init()
pygame.display.set_caption('Ping-Pong')
tela = pygame.display.set_mode((larMax,altMax))
fonte = pygame.font.SysFont('Arial', 30, True, False)
#LoopPrincipal
while True:
	tela.fill(corFundo)
	#TratadorDeEventos
	for evento in pygame.event.get():
		if evento.type == QUIT: pygame.quit(); exit()
	#MovimentoDoJogador1
	if posJ1 > 1 and pygame.key.get_pressed()[K_w]: posJ1 -= velJ1
	if posJ1 < altMax-altJ1 and pygame.key.get_pressed()[K_s]: posJ1 += velJ1
	#MovimentoDoJogador2
	if posJ2 > 1 and pygame.key.get_pressed()[K_UP]: posJ2 -= velJ2
	if posJ2 < altMax-altJ2 and pygame.key.get_pressed()[K_DOWN]: posJ2 += velJ2
	#MovimentoDaBola
	if posx >= larMax-raio:
		vel = 1
		pontosJ1 += 1
		posx = larMax//5
		posy = randint(75,altMax-75)
		vely = choice([-vel,vel])
		velx = vel
		tempo = 3
		sleep(2)
	if posx <= 0:
		vel = 1
		pontosJ2 += 1
		posx = larMax-larMax//5
		posy = randint(50,altMax-50)
		vely = choice([-vel,vel])
		velx = -vel
		tempo = 3
		sleep(2)
	if posy >= altMax-raio or posy <= 0: vely = -vely
	posx += velx; posy += vely
	#Desenhos
	bola = pygame.draw.circle(tela, corBola, (posx,posy), raio)
	jogador1 = pygame.draw.rect(tela, corJ1, (0,posJ1,larJ1,altJ1))
	jogador2 = pygame.draw.rect(tela, corJ2, (larMax-larJ2,posJ2,larJ2,altJ2))
	pygame.draw.line(tela, corLinha, (0,altMax-2), (larMax,altMax-2), 3)
	pygame.draw.line(tela, corLinha, (0,1), (larMax,1), 3)
	#Colisões
	if jogador1.colliderect(bola): velx = vel; cont += 1
	if jogador2.colliderect(bola): velx = -vel; cont += 1
	if cont == 8*mult: vel += 0.5; mult += 1
	#Textos
	x,y = pygame.font.Font.size(fonte, str(pontosJ1))
	texto1 = fonte.render(str(pontosJ1), True, corTexto)
	texto2 = fonte.render(str(pontosJ2), True, corTexto)
	tela.blit(texto1, (larMax//2-x-15,15))
	tela.blit(texto2, (larMax//2+15,15))
	#Finalização
	pygame.display.update()
	if pontosJ1 == 3: mensagem = 'Jogador1 Ganhou!'; break
	elif pontosJ2 == 3: mensagem = 'Jogador2 Ganhou!'; break
	while tempo != 0: sleep(1); tempo -= 1
x,y = pygame.font.Font.size(fonte, mensagem)
texto = fonte.render(mensagem, True, corTexto)
tela.blit(texto, (larMax//2-x//2,altMax//2-y//2))
pygame.display.update(); sleep(3)
pygame.quit(); exit()
