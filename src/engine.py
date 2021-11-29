import sys
import pygame

from pygame import display, fastevent, time, Surface
from pygame.sprite import Group, groupcollide

from ents.janela import JanelaDetalhe, Mouse, JanelaVinhos, ListaVinhos, Vinho
from ents.presente import PresenteFechado

from groups import tela_group, presente_group, mouse_group, vinhos_lista, tela_detalhes_group

sys.path.insert(0, '/')

class WindowMain:
    def __init__(self):
        display.init()
        fastevent.init()

        self.lista_vinhos = ['Tinto','Rosé','Espumante','Branco','','Tinto','Rosé','Espumante','Branco','','Tinto','Rosé','Espumante','Branco','','Tinto','Rosé','Espumante','Branco','','Tinto','Rosé','Espumante','Branco','']
        self.WINDOWLOOP = True

        self.tela = display.set_mode([16*7*4, 16*5*4])
        display.set_caption("Wine Examine")

        self.FPS_TICK = time.Clock()
        self.COLETAR_DADOS = pygame.USEREVENT + 1
        pygame.time.set_timer(self.COLETAR_DADOS, 5000)

    def inicializar_grupos(self):
        self.detalhes = Surface((16*4, 16*6*4))
        Mouse(mouse_group)
        JanelaDetalhe(tela_detalhes_group)
        ListaVinhos(tela_group)
        JanelaVinhos(tela_detalhes_group)
        PresenteFechado(presente_group)

    def adicionar_vinhos(self):
        for vinho in self.lista_vinhos:
            Vinho(vinhos_lista)

    def eventos_tela(self):
        for evento in fastevent.get():
            if evento.type == pygame.QUIT:
                self.WINDOWLOOP = False

            if evento.type == self.COLETAR_DADOS:
                self.adicionar_vinhos()

            for colission in groupcollide(vinhos_lista, mouse_group, False, False):
                if evento.type == pygame.MOUSEWHEEL:
                    vinhos_lista.update(evento.y)

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
        vinhos_lista.draw(self.tela)
        tela_detalhes_group.draw(self.tela)
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
