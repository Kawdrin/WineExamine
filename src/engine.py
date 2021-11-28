import sys
import pygame

from pygame import display, fastevent, time
from pygame.sprite import Group, groupcollide

from ents.janela import JanelaDetalhe, Mouse
from ents.presente import PresenteFechado

from groups import tela_group, presente_group, mouse_group

sys.path.insert(0, '/')

class WindowMain:
    def __init__(self):
        display.init()
        fastevent.init()

        self.WINDOWLOOP = True

        self.tela = display.set_mode([16*7*4, 16*5*4])
        display.set_caption("Wine Examine")

        self.FPS_TICK = time.Clock()

    def inicializar_grupos(self):
        Mouse(mouse_group)
        JanelaDetalhe(tela_group)
        PresenteFechado(presente_group)

    def eventos_tela(self):
        for evento in fastevent.get():
            if evento.type == pygame.QUIT:
                self.WINDOWLOOP = False

            for colision in groupcollide(presente_group, mouse_group, False, False):
                if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                    colision.click()

    def atualizar_tela(self):
        mouse_group.update()
        presente_group.update()
        tela_group.update()
        display.flip()


    def desenhar_tela(self):
        tela_group.draw(self.tela)
        presente_group.draw(self.tela)

    def window_loop(self):
        self.inicializar_grupos()
        while self.WINDOWLOOP:
            self.eventos_tela()
            self.desenhar_tela()
            self.atualizar_tela()
            self.FPS_TICK.tick(60)



g = WindowMain()
g.window_loop()
