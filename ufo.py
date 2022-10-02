from random import randint, choice
from pygame.sprite import Sprite, Group, GroupSingle
import pygame as pg

class Ufo(Sprite):
    
    def __init__(self, game, pos):
        super().__init__()
        self.image = pg.image.load('images/alienship.bmp')
        self.screen = game.screen
        self.settings = game.settings
        self.sound = game.sound
        self.sb = game.scoreboard
        self.ufo_points = randint(500, 1500)
        self.settings.ufo_points = self.ufo_points
        self.ufo_hover = self.sound.sounds['ufohover']        
        if pos == 'right':
            self.x = self.settings.screen_width + 50
            self.speed = -2.5
            
        else:
            self.x = -50
            self.speed = 2.5
        
        self.rect = self.image.get_rect(topleft= (self.x, 0))
        self.rect.y = self.rect.height
        
    def hit(self):
        self.sb.increment_score_ufo()
        
    def update(self):
        self.rect.x += self.speed
        self.draw()
        
    def draw(self):
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(self.image, rect)
        
class Ufos:
    
    def __init__(self, game):
        self.game = game 
        self.sb = game.scoreboard
        self.ufos = GroupSingle()
        self.spawn_time = randint(500, 1500)
        self.ship_lasers = game.ship_lasers.lasers
        self.screen = game.screen
        self.settings = game.settings 
        self.ship = game.ship
        
    def ufo_timer(self):
        self.spawn_time -= 0.5
        if self.spawn_time < 0:
            spawn = choice(['left', 'right'])
            ufo = Ufo(game = self.game, pos= spawn)
            self.ufos.add(ufo)
            ufo.ufo_hover.play()
            self.spawn_time = randint(500, 1500)
    
    def check_collision(self):
        collisons = pg.sprite.groupcollide(self.ufos, self.ship_lasers, True, True)
        if collisons:
            for ufo in collisons:
                ufo.hit()
    
    def update(self):
        self.check_collision()
        self.ufo_timer()
        for ufo in self.ufos.sprites():
            ufo.update()
    
    def draw(self):
        for ufo in self.ufos.sprites():
            ufo.draw()
            
        
        