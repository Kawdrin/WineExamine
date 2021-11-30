import sys
import pygame

from pygame import display, fastevent, time, Surface
from pygame.sprite import Group, groupcollide

from pygame.font import Font

from ents.janela import JanelaDetalhe, Mouse, JanelaVinhos, ListaVinhos, Vinho, VinhosMask
from ents.presente import PresenteFechado

from groups import tela_group, presente_group, mouse_group, vinhos_lista, tela_detalhes_group

import sqlite3

sys.path.insert(0, '/')

class WindowMain:
    def __init__(self):
        display.init()
        fastevent.init()
        pygame.font.init()

        banco = sqlite3.connect("res/vinhos.db")
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM vinhos")
        self.lista_vinhos = cursor.fetchall()
        self.WINDOWLOOP = True

        self.tela = display.set_mode([16*7*4, 16*5*4])
        display.set_caption("Wine Examine")

        self.FPS_TICK = time.Clock()
        self.COLETAR_DADOS = pygame.USEREVENT + 1
        pygame.time.set_timer(self.COLETAR_DADOS, 100000)
        self.dados = ['','','','','','']

        self.tm_40_font = Font("res/fonts/AvenuePixel-Regular.ttf", 40)
        self.tm_35_font = Font("res/fonts/AvenuePixel-Regular.ttf", 35)
        self.tm_25_font = Font("res/fonts/AvenuePixel-Regular.ttf", 25)
        self.tm_18_font = Font("res/fonts/AvenuePixel-Regular.ttf", 18)

    def inicializar_grupos(self):
        self.detalhes = Surface((16*4, 16*6*4*100))
        Mouse(mouse_group)
        JanelaDetalhe(tela_detalhes_group)
        self.ls = ListaVinhos(tela_group)
        VinhosMask(vinhos_lista)
        JanelaVinhos(tela_detalhes_group)
        PresenteFechado(presente_group)
        for vinho in self.lista_vinhos:
            Vinho(vinho, vinhos_lista)

    def eventos_tela(self):
        for evento in fastevent.get():
            if evento.type == pygame.QUIT:
                self.WINDOWLOOP = False

            for colission in groupcollide(vinhos_lista, mouse_group, False, False):
                if evento.type == pygame.MOUSEWHEEL:
                    vinhos_lista.update(evento.y)
                if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                    self.dados = colission.click()

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
