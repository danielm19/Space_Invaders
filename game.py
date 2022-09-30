import pygame as pg
from settings import Settings
import game_functions as gf
from laser import Lasers, LaserType
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from barrier import Barriers
from button import Button
import sys


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")

        self.sound = Sound(bg_music="sounds/startrek.wav")
        self.scoreboard = Scoreboard(game=self)  

        self.ship_lasers = Lasers(settings=self.settings, type=LaserType.SHIP)
        self.alien_lasers = Lasers(settings=self.settings, type=LaserType.ALIEN)
        
        self.barriers = Barriers(game=self)
        self.ship = Ship(game=self)
        self.aliens = Aliens(game=self)
        self.settings.initialize_speed_settings()
        self.play_button = Button(screen= self.screen, text= "Play", x = self.settings.screen_width // 2, y = 625)
        self.highscore_button = Button(screen= self.screen, text= "Highscores", x = self.settings.screen_width // 2, y = 675)

    def reset(self):
        print('Resetting game...')
        self.barriers.reset()
        self.ship.reset()
        self.aliens.reset()
       

    def game_over(self):
        print('All ships gone: game over!')
        self.sound.gameover()
        pg.quit()
        sys.exit()
                    
    def play(self):
        self.sound.play_bg()
        while True:     
            gf.check_events(settings=self.settings, ship=self.ship)
            self.screen.blit(self.settings.bg_image, (0,0))
            self.ship.update()
            self.aliens.update()
            self.barriers.update()
            self.scoreboard.update()
            pg.display.flip()
            
    def start_screen(self):
        ptslist = [" = 10 PTS", " = 20 PTS", "= 40 PTS", " = ???"]
        font = pg.font.SysFont('arial', 72)
        text = font.render('SPACE', True, self.settings.white)
        text_rect = text.get_rect()
        text_rect.center = ((self.settings.screen_width // 2, self.settings.screen_height // 10))
        
        font1 = pg.font.SysFont('arial', 48)
        invader_txt = font1.render('INVADERS', True, self.settings.green)
        invader_txt_rect = invader_txt.get_rect()
        invader_txt_rect.center = ((self.settings.screen_width // 2, self.settings.screen_height // 5))
        
        ptsfont = pg.font.SysFont('arial', 20)
        pts1 = ptsfont.render(ptslist[0], True, self.settings.white)
        pts1_rect = pts1.get_rect()
        pts1_rect.center = ((self.settings.screen_width // 2, 335))
        
        pts2 = ptsfont.render(ptslist[1], True, self.settings.white)
        pts2_rect = pts2.get_rect()
        pts2_rect.center = ((self.settings.screen_width // 2, 380))
        
        pts3 = ptsfont.render(ptslist[2], True, self.settings.white)
        pts3_rect = pts3.get_rect()
        pts3_rect.center = ((self.settings.screen_width // 2, 430))
        
        pts4 = ptsfont.render(ptslist[3], True, self.settings.white)
        pts4_rect = pts4.get_rect()
        pts4_rect.center = ((self.settings.screen_width // 2.07, 485))
        
        greenalien = pg.image.load('images/alien00.bmp')
        greenalien = pg.transform.scale(greenalien, (72, 72))
        greenalien_rect = greenalien.get_rect()
        greenalien_rect.center = ((self.settings.screen_width // 2.25, 350))
        
        bluealien = pg.image.load('images/alien10.bmp')
        bluealien = pg.transform.scale(bluealien, (72, 72))
        bluealien_rect = bluealien.get_rect()
        bluealien_rect.center = ((self.settings.screen_width // 2.25, 400))
        
        purplealien = pg.image.load('images/alien20.bmp')
        purplealien = pg.transform.scale(purplealien, (72, 72))
        purplealien_rect = purplealien.get_rect()
        purplealien_rect.center = ((self.settings.screen_width // 2.27, 440))
        
        alienship = pg.image.load('images/alienship.bmp')
        alienship = pg.transform.scale(alienship, (64, 64))
        alienship_rect = alienship.get_rect()
        alienship_rect.center = ((self.settings.screen_width // 2.27, 510))
        
        button_click = False
        
        while button_click == False:
            self.screen.fill(self.settings.black)
            self.screen.blit(text, text_rect)
            self.screen.blit(invader_txt, invader_txt_rect)
            self.screen.blit(greenalien, greenalien_rect)
            self.screen.blit(pts1, pts1_rect)
            self.screen.blit(bluealien, bluealien_rect)
            self.screen.blit(pts2, pts2_rect)
            self.screen.blit(purplealien, purplealien_rect)
            self.screen.blit(pts3, pts3_rect)
            self.screen.blit(alienship, alienship_rect)
            self.screen.blit(pts4, pts4_rect)
            self.play_button.draw()
            self.highscore_button.draw()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    mousepos = pg.mouse.get_pos()
                    if self.play_button.rect.collidepoint(mousepos):
                        button_click = True
                        self.play() 
            pg.display.update()


def main():
    g = Game()
    g.start_screen()
 

if __name__ == '__main__':
    main()
