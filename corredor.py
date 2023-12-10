import pygame
from sys import exit # importamos parte do modulo

pygame.init()

#tela principal
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Corredor')
relogio = pygame.time.Clock() #objeto relógio
teste_font = pygame.font.Font('font/Pixeltype.ttf', 50)

ceu_superficie = pygame.image.load('graphics/Sky.png').convert()
chao_superficie = pygame.image.load('graphics/ground.png').convert()
texto_superficie = teste_font.render('Corra --- Run',False,'Black' ).convert() #(texto, AA, cor)

#.convert, converte a imagem em um arquivo facilitado para execução em python
caracol_superficie = pygame.image.load('graphics/snail/snail1.png').convert_alpha( )
caracol_retangulo = caracol_superficie.get_rect(bottomright = (600,300 ) )

jogador_superficie = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
jogador_retangulo = jogador_superficie.get_rect(midleft = (80,260))   #criando um retângulo, definindo o ponto de contato


    # desenha todos os nossos elementos 
    #atualização tudo
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  
    
    # blit significa tranfêrencia de imagem em bloco
    # foi passado dois argumentos o primeiro referente a tela e o outro a posição.)
    # a ordem que você coloca os elementos, interfere na sua aparição em python
    screen.blit(ceu_superficie, (0, 0)) #1
    screen.blit(chao_superficie, (0,300)) #2
    screen.blit(texto_superficie,(300,50))

    caracol_retangulo.x -= 4   
    if caracol_retangulo.right <= 0: caracol_retangulo.left = 800
    screen.blit(caracol_superficie, caracol_retangulo)
    screen.blit(jogador_superficie, jogador_retangulo)
    
    pygame.display.update()
    relogio.tick(60 ) #limita o jogo a 60fps

