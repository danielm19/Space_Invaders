import pygame as pg
from pygame.sprite import Sprite, Group
from timer import Timer

class Barrier(Sprite):
    color = 255, 0, 0
    black = 0, 0, 0
    barrier_images = [pg.transform.rotozoom(pg.image.load(f'images/barrier{n}.png'), 0, 2) for n in range(4)]

    def __init__(self, game, rect):
        super().__init__()
        self.screen = game.screen
        self.rect = rect
        self.settings = game.settings
        self.barrier_timer = Timer(image_list= Barrier.barrier_images, is_loop= False)
        
    def hit(self): 
        self.barrier_timer.next_frame()
        if self.barrier_timer.is_expired():
            self.kill()
      
    def update(self):
        self.draw()
        
    def draw(self): 
        image = self.barrier_timer.current_image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)


class Barriers:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.barriers = Group()
        self.create_barriers()

    def create_barriers(self):     
        width = self.settings.screen_width / 10
        height = 2.0 * width / 2.15
        top = self.settings.screen_height - 2.1 * height
        rects = [pg.Rect(x * 2 * width + 1.5 * width, top, width, height) for x in range(4)]   # SP w  3w  5w  7w  SP
        #self.barriers = [Barrier(game=self.game, rect=rects[i]) for i in range(4)]
        for i in range(4):
            self.barriers.add(Barrier(game= self.game, rect= rects[i]))
    
    def check_collisions(self):
        #check if alien laer hit barrier
        collisions = pg.sprite.groupcollide(self.barriers, self.game.alien_lasers.lasers, False, True)
        if collisions:
            for barrier in collisions:
                barrier.hit()
        
        #check if ship laser hit barrier
        collisions = pg.sprite.groupcollide(self.barriers, self.game.ship_lasers.lasers, False, True)
        if collisions:
            for barrier in collisions:
                barrier.hit()
                
    def reset(self):
        self.create_barriers()

    def update(self):
        self.check_collisions()
        for barrier in self.barriers: 
            barrier.update()

  
