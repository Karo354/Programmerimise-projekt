"""Oluline info:
Projekti teema: tekstipõhine fantaasiamäng
Projekti autorid: Fiona Valkenklau ja Karoliine Torp"""

import pygame
import sys

"""ekraani loomine"""
pygame.init()
pygame.font.init()
pikkus, kõrgus = 700, 550
ekraan = pygame.display.set_mode((pikkus, kõrgus))
font = pygame.font.SysFont('timesnewroman', 35)
pygame.display.set_caption("Teksti põhine fantaasiamäng")

"""osad värvid"""
hele= [182, 7, 168]
tume = [211, 101, 245]


def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        ekraan.fill((0, 0, 0))
        tekst2 = font.render("Mäng käivitatud", True, (255, 255, 255))
        ekraan.blit(tekst2, (200, 350))
        pygame.display.update()
        
"""algus ekraan"""
def algus_ekraan():
    while True:
        """sündmused"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mängi_nupp.collidepoint(hiir):
                    game()

                if lõpeta_nupp.collidepoint(hiir):
                    pygame.quit()
                    sys.exit()
                    
        ekraan.fill((226, 129, 255))
        """suurim ristkülik"""
        pygame.draw.rect(ekraan,[153, 8, 141],[46, 46, 600, 450], 4)
        pygame.draw.rect(ekraan,[198, 40, 185],[42, 42, 600, 450], 4)
        pygame.draw.rect(ekraan,[221, 59, 208],[38, 38, 600, 450], 4)
        pygame.draw.rect(ekraan,[250, 100, 238],[34, 34, 600, 450], 4)
        
        """ülemine tekst"""
        tekst1 = font.render('Kas soovid mängida?', True,(111, 4, 144))
        ekraan.blit(tekst1, (190, 150))
        
        """nupud"""
        hiir = pygame.mouse.get_pos()
        
        mängi_nupp = pygame.Rect(150, 250, 150, 50)
        pygame.draw.rect(ekraan,[221, 59, 208],[142, 242, 150, 50],4)
        pygame.draw.rect(ekraan,[153, 8, 141],[146, 246, 150, 50],4)
        lõpeta_nupp = pygame.Rect(400, 250, 150, 50)
        pygame.draw.rect(ekraan,[221, 59, 208],[392, 242, 150, 50],4)
        pygame.draw.rect(ekraan,[153, 8, 141],[396, 246, 150, 50],4)
        
        pygame.draw.rect(ekraan, hele if mängi_nupp.collidepoint(hiir) else tume, mängi_nupp)
        pygame.draw.rect(ekraan, hele if lõpeta_nupp.collidepoint(hiir) else tume, lõpeta_nupp)
        
        mängi_tekst = font.render("Mängi", True, (111, 4, 144))
        lõpeta_tekst = font.render("Lõpeta", True,(111, 4, 144))
        
        ekraan.blit(mängi_tekst, (180, 257))
        ekraan.blit(lõpeta_tekst, (425, 257))

        pygame.display.update()
algus_ekraan()
