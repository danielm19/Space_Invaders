import pygame as pg 
# import pygame.font

file = open('high_score.txt', 'r')
stat = file.read()
class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = int(stat)
        
        self.settings = game.settings
        self.screen = game.screen
        self.game = game
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.high_score_image = None
        self.high_score_rect = None
        self.prep_score()
        self.prep_high_score()
        
    def check_high_score(self, alienpoints):
        file = open('high_score.txt', 'w')
        if self.score > self.high_score:
            self.high_score = self.score
        file.write(str(self.high_score))

        self.prep_score()
        self.prep_high_score()  
        file.close()

    def increment_score(self, alienpoints): 
        self.score += alienpoints
        self.prep_score()
        
    def levelup(self):
        self.level += 1
        print("level up: level is now ",self.level)
        self.settings.alien_speed_factor *= self.settings.speedup_factor
        
    def increment_score_ufo(self):
        self.score += self.settings.ufo_points
        self.prep_score()

    def prep_score(self): 
        score = int(round(self.score, -1))
        score_str = "{:,}".format(score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.black)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        high_score = int(round(self.high_score, -1))
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, 
        self.text_color, self.settings.black)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def reset(self): 
        self.score = 0
        self.update()

    def update(self): 
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)