import pygame
from sys import exit # importamos parte do modulo

pygame.init()

#tela principal
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Corredor')
relogio = pygame.time.Clock() #objeto relógio
teste_font = pygame.font.Font('font/Pixeltype.ttf', 50)

ceu_superf = pygame.image.load('graphics/Sky.png').convert()
chao_superf = pygame.image.load('graphics/ground.png').convert()

score_superf = teste_font.render('Corra Game',False,(64,64,64) ).convert() #(texto, AA, cor)
score_rect = score_superf.get_rect(center = (400, 50))  
             

#.convert, converte a imagem em um arquivo facilitado para execução em python
caracol_superf = pygame.image.load('graphics/snail/snail1.png').convert_alpha( )
caracol_retangulo = caracol_superf.get_rect(bottomright = (600,300 ) )

jogador_superf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
jogador_retangulo = jogador_superf.get_rect(midleft = (80,260))   #criando um retângulo, definindo o ponto de contato


    # desenha todos os nossos elementos 
    #atualização tudo
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if jogador_retangulo.collidepoint(event.pos): print('colisão') 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('pular')
    
    # blit significa tranfêrencia de imagem em bloco
    # foi passado dois argumentos o primeiro referente a tela e o outro a posição.)
    # a ordem que você coloca os elementos, interfere na sua aparição em python
   
    
    screen.blit(ceu_superf, (0, 0)) #1
    screen.blit(chao_superf, (0,300)) #2
    
                
    caracol_retangulo.x -= 4   
    if caracol_retangulo.right <= 0: caracol_retangulo.left = 800
    screen.blit(caracol_superf, caracol_retangulo)
    
    screen.blit(jogador_superf, jogador_retangulo)
   # pygame.draw.line(screen, 'gold', (0,0), pygame.mouse.get_pos(), 10)
    
    #colisão de retangulos
    # este método retorna um e zero
    #if jogador_retangulo.colliderect(caracol_retangulo):
     #   print('Colisão')
    pygame.draw.rect(screen, '#c0e8ec', score_rect ) #modulo de desenho pygame
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20) #modulo de desenho pygame
    screen.blit(score_superf,score_rect)
    '''teclado_acao = pygame.key.get_pressed()
    if jogador_retangulo.collidepoint((teclado_acao)): # copiando a posição do mouse para a colisão 
        print('Colisão')'''

    # implementando uma lista especifica do pygame
    '''keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: 
        print('jump')'''
    
    #mouse_pos = pygame.mouse.get_pos()
   # if jogador_retangulo.collidepoint((mouse_pos)): # copiando a posição do mouse para a colisão 
       # print(pygame.mouse.get_pressed())
        
    pygame.display.update()
    relogio.tick(60 ) #limita o jogo a 60fps

