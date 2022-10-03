import pygame
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 215, 0)
        self.blue = (30, 145, 250)
        self.bg_image = pygame.image.load('images/space_backgroud.png')
        
        self.laser_width = 5
        self.laser_height = 30
        self.laser_color = 255, 0, 0
        self.lasers_every = 8          # change to 1 to see faster lasers

        self.aliens_shoot_every = 120    # about every 2 seconds at 60 fps
        self.ufo_points = 0
        
        self.ship_limit = 3         # total ships allowed in game before game over
        
        self.speedup_factor = 1.2
        self.fleet_drop_speed = 1
        self.fleet_direction = 1     # change to a Vector(1, 0) move to the right, and ...
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.alien_speed_factor = 1
        self.ship_speed_factor = 3
        self.laser_speed_factor = 2

    def increase_speed(self):
        scale = self.speedup_scale
        self.ship_speed_factor *= scale
        self.laser_speed_factor *= scale
