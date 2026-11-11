import pygame
from pygame.locals import *
import sys

pygame.font.init()
pygame.font.get_init()

# Aken
praegune_ekraan = 'tutorial_menüü'
ekraan = pygame.display.set_mode((500, 400))
valge = (255, 255, 255)
must = (0, 0, 0)
tausta_varv = (valge)
ekraan.fill(tausta_varv)
pygame.display.flip()

# Nupu asukohad:
Nupp_liikumine = pygame.Rect(40, 240, 420, 40)
Nupp_korjamine = pygame.Rect(40, 295, 420, 40)
Nupp_menüü = pygame.Rect(200, 350, 100, 40)

nupp_edasi = pygame.Rect(350, 310, 100, 40)
nupp_tagasi = pygame.Rect(50, 310, 100, 40)

# Tekst
font1 = pygame.font.SysFont('cambriamath', 21)
font2 = pygame.font.SysFont('cambriamath', 17)

# Akna ikoon:
ikoon = pygame.image.load('tuto.png')
pygame.display.set_icon(ikoon)
pygame.display.set_caption('Tutorial')

# Teksti sisestamine
user_tekst = 'Aa'
sisestus = pygame.Rect(180, 100, 140, 32)
värv_aktiivne = pygame.Color('lightskyblue3')
värv_passiivne = pygame.Color("lightgray")
värv = värv_passiivne
active = False

# Õpetuse menüü
def tutorial_menüü():
    pygame.draw.rect(ekraan, (220, 220, 220),
                     [10, 200, 480, 200], 0)
    tekst1 = font1.render('Vali mida soovid uurida:', True, must)
    tekstRect1 = tekst1.get_rect()
    tekstRect1.center = (250, 220)
    ekraan.blit(tekst1, tekstRect1)

    # Liikumise nupp
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [40, 240, 420, 40], 0)
    tekst2 = font1.render("Liikumine", True, must)
    ekraan.blit(tekst2, (Nupp_liikumine.x + 160, Nupp_liikumine.y + 8))
    
    # Korjamise nupp
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [40, 295, 420, 40], 0)
    tekst3 = font1.render("Objektide üleskorjamine", True, must)
    ekraan.blit(tekst3, (Nupp_korjamine.x + 110, Nupp_korjamine.y + 10))

    # Tagasi nupp
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [205, 350, 100, 40], 0)
    tekst4 = font1.render("MENÜÜ", True, must)
    ekraan.blit(tekst4, (Nupp_liikumine.x + 180, Nupp_liikumine.y + 120))

    pygame.display.update()
    
def liikumine_lk1():
    ekraan.fill(tausta_varv)
    pygame.draw.rect(ekraan, (220, 220, 220),
                     [10, 200, 480, 200], 0)
    tekst5 = font2.render('''
    Liikumiseks tuleb kirjutada soovitud liikumise suund ekraanil
    olevasse tekstikasti.
    Enamasti on antud valik võimalikest liikumise suundadest.
    Võtame hetkel näiteks liikumissuunad "vasakule" ja "paremale".''', True, must)
    tekstRect5 = tekst5.get_rect()
    tekstRect5.center = (240, 235)
    ekraan.blit(tekst5, tekstRect5)
        
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [350, 310, 100, 40], 0)
    tekst6 = font1.render("Edasi", True, must)
    ekraan.blit(tekst6, (Nupp_liikumine.x + 335, Nupp_liikumine.y + 75))
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [205, 350, 100, 40], 0)
    tekst8 = font1.render("TAGASI", True, must)
    ekraan.blit(tekst8, (Nupp_liikumine.x + 180, Nupp_liikumine.y + 120))

def liikumine_lk2():
    ekraan.fill(tausta_varv)
    
    pygame.draw.rect(ekraan, (220, 220, 220),
                     [10, 200, 480, 200], 0)
    tekst9 = font2.render('''
    Liikuda saad kui kirjutad tekstikasti "liigu ...", asendades "..."
    valitud suunaga.
    Näiteks: "liigu vasakule".
    Proovi see üleval tekstikastis läbi.''', True, must)
    tekstRect9 = tekst9.get_rect()
    tekstRect9.center = (240, 235)
    ekraan.blit(tekst9, tekstRect9)
    
    #Tekst
    if active:
        värv = värv_aktiivne
    else:
        värv = värv_passiivne
    pygame.draw.rect(ekraan, värv, sisestus, 0)
    tekst = font1.render(user_tekst, True, (0, 0, 0))
    ekraan.blit(tekst, (sisestus.x + 5, sisestus.y + 5))
    img = font1.render(user_tekst, True, must)
    rect = img.get_rect()
    rect.topleft = (20, 20)
    cursor = pygame.Rect(rect.topright, (3, rect.height))
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [350, 310, 100, 40], 0)
    tekst6 = font1.render("Edasi", True, must)
    ekraan.blit(tekst6, (Nupp_liikumine.x + 335, Nupp_liikumine.y + 75))
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                      [50, 310, 100, 40], 0)
    tekst7 = font1.render("Tagasi", True, must)
    ekraan.blit(tekst7, (Nupp_liikumine.x + 30, Nupp_liikumine.y + 75))

def liikumine_lk3():
    ekraan.fill(tausta_varv)
    
    pygame.draw.rect(ekraan, (220, 220, 220),
                     [10, 200, 480, 200], 0)
    tekst10 = font2.render('''
    Tegid õpetuse läbi!''', True, must)
    tekstRect10 = tekst10.get_rect()
    tekstRect10.center = (240, 235)
    ekraan.blit(tekst10, tekstRect10)
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                      [50, 310, 100, 40], 0)
    tekst7 = font1.render("Tagasi", True, must)
    ekraan.blit(tekst7, (Nupp_liikumine.x + 30, Nupp_liikumine.y + 75))
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [205, 350, 100, 40], 0)
    tekst8 = font1.render("TAGASI", True, must)
    ekraan.blit(tekst8, (Nupp_liikumine.x + 180, Nupp_liikumine.y + 120))
    
def korjamine_lk1():
    ekraan.fill(tausta_varv)
    
    pygame.draw.rect(ekraan, (220, 220, 220),
                     [10, 200, 480, 200], 0)
    tekst10 = font2.render('''
    Selleks, et lossist pääseda võib sul vaja minna
    lossis ringi lebavaid esemeid.
    Nüüd õpime kuidas asju üles korjata ja endaga kaasa võtta.''', True, must)
    tekstRect10 = tekst10.get_rect()
    tekstRect10.center = (240, 235)
    ekraan.blit(tekst10, tekstRect10)
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [350, 310, 100, 40], 0)
    tekst6 = font1.render("Edasi", True, must)
    ekraan.blit(tekst6, (Nupp_liikumine.x + 335, Nupp_liikumine.y + 75))
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [205, 350, 100, 40], 0)
    tekst8 = font1.render("TAGASI", True, must)
    ekraan.blit(tekst8, (Nupp_liikumine.x + 180, Nupp_liikumine.y + 120))

def korjamine_lk2():
    ekraan.fill(tausta_varv)
    
    pygame.draw.rect(ekraan, (220, 220, 220),
                     [10, 200, 480, 200], 0)
    tekst11 = font2.render('''
    Selleks, et eset üles korjata tuleb kirjutada tekstikasti
    käsk "võta ...", asendades "..." valitud esemega.
    Näiteks: "võta raamat"
    Proovi see ülemises tekstikastis läbi.''', True, must)
    tekstRect11 = tekst11.get_rect()
    tekstRect11.center = (240, 235)
    ekraan.blit(tekst11, tekstRect11)
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [350, 310, 100, 40], 0)
    tekst6 = font1.render("Edasi", True, must)
    ekraan.blit(tekst6, (Nupp_liikumine.x + 335, Nupp_liikumine.y + 75))
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                      [50, 310, 100, 40], 0)
    tekst7 = font1.render("Tagasi", True, must)
    ekraan.blit(tekst7, (Nupp_liikumine.x + 30, Nupp_liikumine.y + 75))
    
def korjamine_lk3():
    ekraan.fill(tausta_varv)
    
    pygame.draw.rect(ekraan, (220, 220, 220),
                     [10, 200, 480, 200], 0)
    tekst12 = font2.render('''Tegid õpetuse läbi!''', True, must)
    tekstRect12 = tekst12.get_rect()
    tekstRect12.center = (240, 235)
    ekraan.blit(tekst12, tekstRect12)
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                      [50, 310, 100, 40], 0)
    tekst7 = font1.render("Tagasi", True, must)
    ekraan.blit(tekst7, (Nupp_liikumine.x + 30, Nupp_liikumine.y + 75))
    
    pygame.draw.rect(ekraan, (250, 250, 250),
                     [205, 350, 100, 40], 0)
    tekst8 = font1.render("TAGASI", True, must)
    ekraan.blit(tekst8, (Nupp_liikumine.x + 180, Nupp_liikumine.y + 120))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if praegune_ekraan == 'tutorial_menüü' and event.type == pygame.MOUSEBUTTONDOWN:
            if Nupp_liikumine.collidepoint(event.pos):
                praegune_ekraan = 'liikumine1'
            if Nupp_korjamine.collidepoint(event.pos):
                praegune_ekraan = 'korjamine1'
#             if Nupp_tagasi.collidepoint(event.pos):
#                 praegune_ekraan = 'sissejuhatus'
        elif praegune_ekraan == 'liikumine1' and event.type == pygame.MOUSEBUTTONDOWN:
             if Nupp_menüü.collidepoint(event.pos):
                praegune_ekraan = 'tutorial_menüü'
             if nupp_edasi.collidepoint(event.pos):
                 praegune_ekraan = 'liikumine2'
        elif praegune_ekraan == 'liikumine2' and event.type == pygame.MOUSEBUTTONDOWN:
            if nupp_edasi.collidepoint(event.pos):
                 praegune_ekraan = 'liikumine3'
            if nupp_tagasi.collidepoint(event.pos):
                 praegune_ekraan = 'liikumine1'
            if sisestus.collidepoint(event.pos):
                active = True
            else:
                active = False
        elif praegune_ekraan == 'korjamine2' and event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_BACKSPACE:
                user_tekst = user_tekst[:-1]
            else:
                user_tekst += event.unicode
        elif praegune_ekraan == 'liikumine3' and event.type == pygame.MOUSEBUTTONDOWN:
            if Nupp_menüü.collidepoint(event.pos):
                praegune_ekraan = 'tutorial_menüü'
            if nupp_tagasi.collidepoint(event.pos):
                 praegune_ekraan = 'liikumine2'
        elif praegune_ekraan == 'korjamine1' and event.type == pygame.MOUSEBUTTONDOWN:
            if Nupp_menüü.collidepoint(event.pos):
                praegune_ekraan = 'tutorial_menüü'
            if nupp_edasi.collidepoint(event.pos):
                praegune_ekraan = 'korjamine2'
        elif praegune_ekraan == 'korjamine2' and event.type == pygame.MOUSEBUTTONDOWN:
            if nupp_edasi.collidepoint(event.pos):
                 praegune_ekraan = 'korjamine3'
            if nupp_tagasi.collidepoint(event.pos):
                praegune_ekraan = 'korjamine1'
            if sisestus.collidepoint(event.pos):
                active = True
            else:
                active = False
        elif praegune_ekraan == 'korjamine2' and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_tekst = user_tekst[:-1]
            else:
                user_tekst += event.unicode
            img = font.render(text, True, (255, 0, 0))
            rect.size = img.get_size()
            cursor.topleft = rect.topright
        elif praegune_ekraan == 'korjamine3' and event.type == pygame.MOUSEBUTTONDOWN:
            if nupp_tagasi.collidepoint(event.pos):
                praegune_ekraan = 'korjamine2'
            if Nupp_menüü.collidepoint(event.pos):
                praegune_ekraan = 'tutorial_menüü'

    if praegune_ekraan == 'tutorial_menüü':
        tutorial_menüü()
    elif praegune_ekraan == 'liikumine1':
        liikumine_lk1()
    elif praegune_ekraan == 'korjamine1':
        korjamine_lk1()
    elif praegune_ekraan == 'liikumine2':
        liikumine_lk2()
    elif praegune_ekraan == 'liikumine3':
        liikumine_lk3()
    elif praegune_ekraan == 'korjamine2':
        korjamine_lk2()
    elif praegune_ekraan == 'korjamine3':
        korjamine_lk3()
        
    pygame.display.flip()
    
pygame.quit()
