import pygame as pg
from settings import Settings
import sys

class Button:
    def __init__(self, screen, text, x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = Settings()
        self.x = x
        self.y = y
        
        #set the button dimensions
        self.width, self.height = 200, 50
        self.button_color = self.settings.black
        self.text_color = self.settings.green
        self.font = pg.font.SysFont('cambria', 40)
        
        #make the button rect and center it 
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)
        
        self.hover_color = self.settings.blue
        self.hover_image = self.font.render(text, True, self.text_color, self.hover_color)
        
        self.prep_text(text)
    
    def prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center
        
    def draw(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
        
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.button_color == self.settings.black:
                self.screen.fill(self.hover_color, self.rect)
                self.screen.blit(self.hover_image, self.text_image_rect)
        


        
            
        
        