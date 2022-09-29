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
        
    def start_screen(self):
        font = pg.font.SysFont('arial', 72)
        text = font.render('SPACE', True, self.settings.white)
        text_rect = text.get_rect()
        text_rect.center = ((self.settings.screen_width // 2, self.settings.screen_height // 10))
        
        font1 = pg.font.SysFont('arial', 32)
        invader_txt = font.render('INVADERS', True, self.settings.green)
        invader_txt_rect = invader_txt.get_rect()
        invader_txt_rect.center = ((self.settings.screen_width // 2, self.settings.screen_height // 5))
        
        button_click = False
        
        
        while button_click == False:
            self.screen.fill(self.settings.black)
            self.screen.blit(text, text_rect)
            self.screen.blit(invader_txt, invader_txt_rect)
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


def main():
    g = Game()
    g.start_screen()
    #g.play()


if __name__ == '__main__':
    main()
