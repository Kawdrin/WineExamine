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

        self.aberto = False
        self.botao_pressionado = None
        self.dados = ['','','','','','','']

        self.tm_40_font = Font("res/fonts/AvenuePixel-Regular.ttf", 40)
        self.tm_35_font = Font("res/fonts/AvenuePixel-Regular.ttf", 35)
        self.tm_25_font = Font("res/fonts/AvenuePixel-Regular.ttf", 25)
        self.tm_18_font = Font("res/fonts/AvenuePixel-Regular.ttf", 18)

    def inicializar_grupos(self):
        VinhosMask(vinhos_lista)
        JanelaDetalhe(tela_detalhes_group)
        ListaVinhos(tela_group)
        JanelaVinhos(tela_detalhes_group)
        PresenteFechado(presente_group)
        Mouse(mouse_group)
        for vinho in self.lista_vinhos:
            Vinho(vinho, vinhos_lista)

    def eventos_tela(self):
        for evento in fastevent.get():
            if evento.type == pygame.QUIT:
                self.WINDOWLOOP = False

            for colission in groupcollide(vinhos_lista, mouse_group, False, False):
                if evento.type == pygame.MOUSEWHEEL:
                    vinhos_lista.update(evento.y)
                if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1 and colission.rect.y > 16*5*4 and colission.rect.y < 16*9*4:
                    if self.botao_pressionado != None:
                        self.botao_pressionado.pressionar()
                    self.dados = colission.click()
                    self.botao_pressionado = colission


            for colision in groupcollide(presente_group, mouse_group, False, False):
                if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                    self.aberto = True
                    colision.click()



    def atualizar_tela(self):
        presente_group.update()
        tela_group.update()
        mouse_group.update()
        display.flip()

    def draw_text(self, text, x, y, font):
        texto_outline = font.render(text, False, (0,0,0))
        texto = font.render(text, False, (255,255,255))

        self.tela.blit(texto_outline, (x+1, y))
        self.tela.blit(texto_outline, (x-1, y))
        self.tela.blit(texto_outline, (x, y+1))
        self.tela.blit(texto_outline, (x, y-1))
        self.tela.blit(texto, (x, y))

    def escrever_dados(self):
        self.draw_text("Tipo", 16*2*4+15, 16*4+60, self.tm_25_font)
        self.draw_text("Classificação", 16*2*4+100, 16*4+60, self.tm_25_font)
        self.draw_text("Premios", 16*2*4+4, 16*4*2+60, self.tm_25_font)
        self.draw_text("Safra", 253, 16*4*2+60, self.tm_25_font)

        nome = self.dados[0]
        if len(nome) > 29:
            nome = nome[:29] + "..."
        self.draw_text(nome, (224-55)-(len(nome)*3), 16*4+3, self.tm_35_font)
        self.draw_text(self.dados[1], (128+28)-len(self.dados[1])*3, 16*4+80, self.tm_25_font)
        self.draw_text(self.dados[2], (218+45)-(len(self.dados[2])*3), 16*4+80, self.tm_25_font)
        self.draw_text(f"{self.dados[3]}", 16*2*4+28, 16*4*2+80, self.tm_25_font)
        self.draw_text(f"{self.dados[6]}", (228+28), 16*4*2+80, self.tm_25_font)
        self.draw_text(self.dados[5], (224-10)-(len(self.dados[5])*3), 16*4+35, self.tm_25_font)

    def desenhar_tela(self):
        tela_group.draw(self.tela)
        vinhos_lista.draw(self.tela)
        tela_detalhes_group.draw(self.tela)
        presente_group.draw(self.tela)
        if self.aberto:
            self.escrever_dados()

    def window_loop(self):
        self.inicializar_grupos()
        while self.WINDOWLOOP:
            self.eventos_tela()
            self.desenhar_tela()
            self.atualizar_tela()
            self.FPS_TICK.tick(60)


g = WindowMain()
g.window_loop()
