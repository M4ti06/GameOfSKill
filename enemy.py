import pygame

from gameObject import GameObject

class Enemy(GameObject):
    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)
        
        self.speed = speed

    def move(self, max_width):
        if self.x >= (max_width -80 - self.width):
            self.speed = -self.speed
        elif self.x <= 90:
            self.speed = abs(self.speed)
            
        self.x += self.speed

        