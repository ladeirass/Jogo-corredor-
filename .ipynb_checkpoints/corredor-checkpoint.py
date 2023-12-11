import pygame
from sys import exit # importamos parte do modulo
from random import randint

def tela_ponto():    
    h_atual = int (pygame.time.get_ticks() / 1000) - ini_tempo
    score_superf = teste_font.render(f'ponto:{h_atual}', False,(64,64,64))
    score_rect = score_superf.get_rect(center = (400,50))
    screen.blit(score_superf,score_rect)
    return h_atual

def obstaculos_movimento(obstaculo_list):
    if obstaculo_list:
        for obstaculo_rect  in obstaculo_list:
            obstaculo_rect.x -= 5

            if obstaculo_rect.bottom == 300: screen.blit(caracol_superf,obstaculo_rect)
            else:screen.blit(mosca_superf, obstaculo_rect) 
                
        obstaculo_list = [obstaculo for obstaculo in obstaculo_list if obstaculo.x > - 100]    

        return obstaculo_list
    else: return []     
        
pygame.init()
#tela principal
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Corredor')
relogio = pygame.time.Clock() #objeto relógio
teste_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
ini_tempo = 0
ponto = 0

ceu_superf = pygame.image.load('graphics/Sky.png').convert()
chao_superf = pygame.image.load('graphics/ground.png').convert()

score_superf = teste_font.render('Corra Game',False,(64,64,64) ).convert() #(texto, AA, cor)
score_rect = score_superf.get_rect(center = (400, 50))      

#.convert, converte a imagem em um arquivo facilitado para execução em python
#Obstaculos
caracol_superf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
mosca_superf = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstaculo_rect_list = []

jogador_superf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
jogador_retangulo = jogador_superf.get_rect(midbottom = (80,300))   #criando um retângulo, definindo o ponto de contato
jogador_gravidade = 0 #POR PADRÃO
 
#tela de introdução
jogador_fixo = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
jogador_fixo = pygame.transform.rotozoom(jogador_fixo, 0,2)
jogador_fixo_retangulo = jogador_fixo.get_rect(center = (400,200))

nome_jogo = teste_font.render('Crystallife', False,(111,196,169))
nome_jogo_retangulo = nome_jogo.get_rect(center = (400,80)) 
    
jogo_msg = teste_font.render('Pressione Espaço para correr',False,(111,196,169))
jogo_msg_retangulo = jogo_msg.get_rect(center = (400,340))

#cronometro 
tempo_obstaculos = pygame.USEREVENT +1
pygame.time.set_timer(tempo_obstaculos,1500)

# desenha todos os nossos elementos   
#atualização tudo
while True:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:#Verifica se algum botão do mouse esta pressionado
                if jogador_retangulo.collidepoint(event.pos) and jogador_retangulo.bottom >=300:#a ação so aparece quando se clica em cima do personagem 
                    jogador_gravidade = -20  
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jogador_retangulo.bottom >=300:
                    jogador_gravidade = -20  
        
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                ini_tempo = int (pygame.time.get_ticks() / 1000)

        if event.type == tempo_obstaculos and game_active:
            if randint(0,2): 
                obstaculo_rect_list.append(caracol_superf.get_rect(bottomright = (randint(900,1100),300 )))
            else:
                obstaculo_rect_list.append(mosca_superf.get_rect(bottomright = (randint(900,1100),210 )))

    # blit significa tranfêrencia de imagem em bloco
    # foi passado dois argumentos o primeiro referente a tela e o outro a posição.)
    # a ordem que você coloca os elementos, interfere na sua aparição em python
   
    if game_active:
        screen.blit(ceu_superf, (0, 0)) #1
        screen.blit(chao_superf, (0,300)) #2
        ponto = tela_ponto()
        
                    
             
        #Jogador
        jogador_gravidade +=1
        jogador_retangulo.y += jogador_gravidade #mapeia a gravidade atraves do retangulo do personagem
        if jogador_retangulo.bottom >= 300: jogador_retangulo.bottom = 300
        screen.blit(jogador_superf, jogador_retangulo)
        
        #movimento obstaculos
        obstaculo_rect_list = obstaculos_movimento(obstaculo_rect_list)
        
        #Função para encerrar o jogo quando os personagens se colidem
        
    else:
        screen.fill((94,129,162)) 
        screen.blit(jogador_fixo,jogador_fixo_retangulo)

        ponto_msg = teste_font.render(f'ponto: {ponto}', False,(111,196,169))
        ponto_msg_retangulo = ponto_msg.get_rect(center = (400,300))
        screen.blit(nome_jogo,nome_jogo_retangulo) 

        if ponto == 0:
            screen.blit(jogo_msg,jogo_msg_retangulo)
        else:
             screen.blit(ponto_msg,ponto_msg_retangulo)    
    #pygame.draw.rect(screen, '#c0e8ec', score_rect ) #modulo de desenho pygame
    #pygame.draw.rect(screen, '#c0e8ec', score_rect, 20) #modulo de desenho pygame
    #screen.blit(score_superf,score_rect)
    tela_ponto()
    
    pygame.display.update()
    relogio.tick(60 ) #limita o jogo a 60fps

