import pygame
import sys
from random import randint

class JogoCorredor:
    def __init__(self):
        pygame.init()

        # Configuração inicial do jogo
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('Corredor')

        self.relogio = pygame.time.Clock()
        self.teste_font = pygame.font.Font('font/Pixeltype.ttf', 50)
        self.game_active = True
        self.ini_tempo = 0
        self.ponto = 0

        # Carregar recursos gráficos
        self.ceu_superf, self.chao_superf, self.caracol_superf, self.mosca_superf, \
        self.jogador_superf, self.jogador_fixo = self.carregar_recursos()

        # Inicializar elementos do jogo
        self.obstaculo_rect_list = []
        self.jogador_retangulo = self.jogador_superf.get_rect(midbottom=(80, 300))
        self.jogador_gravidade = 0
        self.jogador_fixo_retangulo = self.jogador_fixo.get_rect(center=(400, 200))

        self.nome_jogo = self.teste_font.render('Crystallife', False, (111, 196, 169))
        self.nome_jogo_retangulo = self.nome_jogo.get_rect(center=(400, 80))

        self.jogo_msg = self.teste_font.render('Pressione Espaço para correr', False, (111, 196, 169))
        self.jogo_msg_retangulo = self.jogo_msg.get_rect(center=(400, 340))

        # Configurar temporizador para criar obstáculos
        self.tempo_obstaculos = pygame.USEREVENT + 1
        pygame.time.set_timer(self.tempo_obstaculos, 1500)

    def carregar_recursos(self):
        # Carregar imagens e retornar superfícies
        ceu_superf = pygame.image.load('graphics/Sky.png').convert()
        chao_superf = pygame.image.load('graphics/ground.png').convert()
        caracol_superf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
        mosca_superf = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
        jogador_superf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        jogador_fixo = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
        jogador_fixo = pygame.transform.rotozoom(jogador_fixo, 0, 2)
        return ceu_superf, chao_superf, caracol_superf, mosca_superf, jogador_superf, jogador_fixo

    def exibir_mensagem(self, texto, posicao, cor=(111, 196, 169)):
        # Exibir mensagens na tela
        mensagem = self.teste_font.render(texto, False, cor)
        retangulo = mensagem.get_rect(center=posicao)
        self.screen.blit(mensagem, retangulo)

    def tela_ponto(self):
        # Atualizar e exibir a pontuação
        if self.game_active:
            h_atual = int(pygame.time.get_ticks() / 1000) - self.ini_tempo
            score_superf = self.teste_font.render(f'Pontos: {h_atual}', False, (64, 64, 64))
            score_rect = score_superf.get_rect(center=(400, 50))
            self.screen.blit(score_superf, score_rect)
            return h_atual
        else:
            return 0

    def obstaculos_movimento(self):
        # Mover obstáculos na tela
        if self.obstaculo_rect_list:
            for obstaculo_rect in self.obstaculo_rect_list:
                obstaculo_rect.x -= 5

                if obstaculo_rect.bottom == 300:
                    self.screen.blit(self.caracol_superf, obstaculo_rect)
                else:
                    self.screen.blit(self.mosca_superf, obstaculo_rect)

            # Remover obstáculos que saíram da tela
            self.obstaculo_rect_list = [obstaculo for obstaculo in self.obstaculo_rect_list if obstaculo_rect.x > -100]

    def colisao(self):
        # Verificar colisão entre jogador e obstáculos
        if self.obstaculo_rect_list:
            for obstaculo_rect in self.obstaculo_rect_list:
                if self.jogador_retangulo.colliderect(obstaculo_rect):
                    return True
        return False

    def executar(self):
        # Loop principal do jogo
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.game_active:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.jogador_retangulo.collidepoint(event.pos) and self.jogador_retangulo.bottom >= 300:
                            self.jogador_gravidade = -20
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and self.jogador_retangulo.bottom >= 300:
                            self.jogador_gravidade = -20
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.game_active = True
                        self.ini_tempo = int(pygame.time.get_ticks() / 1000)
                if event.type == self.tempo_obstaculos and self.game_active:
                    # Criar novos obstáculos em intervalos de tempo
                    if randint(0, 2):
                        self.obstaculo_rect_list.append(self.caracol_superf.get_rect(bottomright=(randint(900, 1100), 300)))
                    else:
                        self.obstaculo_rect_list.append(self.mosca_superf.get_rect(bottomright=(randint(900, 1100), 210)))

            if self.game_active:
                # Atualizar elementos durante o jogo ativo
                self.screen.blit(self.ceu_superf, (0, 0))
                self.screen.blit(self.chao_superf, (0, 300))
                self.ponto = self.tela_ponto()

                self.jogador_gravidade += 1
                self.jogador_retangulo.y += self.jogador_gravidade
                if self.jogador_retangulo.bottom >= 300:
                    self.jogador_retangulo.bottom = 300
                self.screen.blit(self.jogador_superf, self.jogador_retangulo)

                self.obstaculos_movimento()

                # Verificar colisão para encerrar o jogo
                self.game_active = not self.colisao()

            else:
                # Atualizar elementos durante a tela de game over
                self.screen.fill((94, 129, 162))
                self.screen.blit(self.jogador_fixo, self.jogador_fixo_retangulo)
                self.obstaculo_rect_list.clear()
                self.jogador_retangulo.midbottom = (80, 300)
                self.jogador_gravidade += 1

                self.exibir_mensagem('Crystallife', (400, 80))
                if self.ponto == 0:
                    self.exibir_mensagem('Pressione Espaço para correr', (400, 340))
                else:
                    self.exibir_mensagem(f'Pontos: {self.ponto}', (400, 340))

            self.tela_ponto()

            pygame.display.update()
            self.relogio.tick(60)

# Instanciar e executar o jogo
jogo = JogoCorredor()
jogo.executar()
