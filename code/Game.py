from operator import truediv

import pygame

from assets.projet.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Meu Jogo")
        self.running = True

    def run(self):

        while self.running:
            # passa a janela correta para o Menu
            menu = Menu(self.screen)
            menu.run()


            # loop de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            # atualiza a tela
            pygame.display.flip()

        pygame.quit()


