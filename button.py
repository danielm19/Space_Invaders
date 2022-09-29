import pygame as pg

#set colors as class variable 
green = (0, 200, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
light_blue = (100, 150, 200)

class Button:
    def __init__(self, screen, message):
        #initialize buttion attributes 
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #setup the button properties and size 
        self.width, self.height = 200, 50
        self.button_color = blue
        self.text_color = white
        self.font = pg.font.SysFont(None, 48)
        
        #create the button rect and center it and prep the button message
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect_center = self.screen_rect.center
        
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_center = self.rect.center
        
        self.hover_color = light_blue
        self.hover_image = self.font.render(message, True, self.text_color, self.hover_color)
        
            
    def draw(self):
        #draw a blank button and draw the message to display 
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        mouse_pos_x, mouse_pos_y = pg.mouse.get_pos()
        if self.rect.collidepoint(x= mouse_pos_x, y= mouse_pos_y):
            if self.button_color == blue:
                self.screen.fill(self.hover_color, self.rect)
                self.screen.blit(self.hover_image, self.msg_image_rect)
            
        
            
        
        