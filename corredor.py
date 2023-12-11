import pygame
from sys import exit # importamos parte do modulo

pygame.init()

#tela principal
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Corredor')
relogio = pygame.time.Clock() #objeto relógio
teste_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

ceu_superf = pygame.image.load('graphics/Sky.png').convert()
chao_superf = pygame.image.load('graphics/ground.png').convert()

score_superf = teste_font.render('Corra Game',False,(64,64,64) ).convert() #(texto, AA, cor)
score_rect = score_superf.get_rect(center = (400, 50))  
             

#.convert, converte a imagem em um arquivo facilitado para execução em python
caracol_superf = pygame.image.load('graphics/snail/snail1.png').convert_alpha( )
caracol_retangulo = caracol_superf.get_rect(bottomright = (600,300 ) )

jogador_superf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
jogador_retangulo = jogador_superf.get_rect(midleft = (80,260))   #criando um retângulo, definindo o ponto de contato
jogador_gravidade = 0 #POR PADRÃO

    # desenha todos os nossos elementos 
    #atualização tudo
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
       
        if event.type == pygame.MOUSEBUTTONDOWN:#Verifica se algum botão do mouse esta pressionado
            if jogador_retangulo.collidepoint(event.pos) and jogador_retangulo.bottom >=300:#a ação so aparece quando se clica em cima do personagem 
                jogador_gravidade = -20  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jogador_retangulo.bottom >=300:
                jogador_gravidade = -20 
    
    # blit significa tranfêrencia de imagem em bloco
    # foi passado dois argumentos o primeiro referente a tela e o outro a posição.)
    # a ordem que você coloca os elementos, interfere na sua aparição em python
   
    
    screen.blit(ceu_superf, (0, 0)) #1
    screen.blit(chao_superf, (0,300)) #2
    
                
    caracol_retangulo.x -= 4   
    if caracol_retangulo.right <= 0: caracol_retangulo.left = 800
    screen.blit(caracol_superf, caracol_retangulo)

    #Jogador
    jogador_gravidade +=1
    jogador_retangulo.y += jogador_gravidade #mapeia a gravidade atraves do retangulo do personagem
    if jogador_retangulo.bottom >= 300: jogador_retangulo.bottom = 300
    screen.blit(jogador_superf, jogador_retangulo)
    
    #Função para encerrar o jogo quando os personagens se colidem
    if caracol_retangulo.colliderect(jogador_retangulo):
        pygame.QUIT()
        exit()

    
    pygame.draw.rect(screen, '#c0e8ec', score_rect ) #modulo de desenho pygame
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20) #modulo de desenho pygame
    screen.blit(score_superf,score_rect)
   
    pygame.display.update()
    relogio.tick(60 ) #limita o jogo a 60fps

