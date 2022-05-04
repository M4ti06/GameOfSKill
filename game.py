import pygame
from pygame.constants import K_DOWN, KEYDOWN, KEYUP

from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:

    def __init__(self):
        
        self.Height = 700 
        self.Width = 1250
        self.white_colour = (0, 150, 250)

        self.Game_Window = pygame.display.set_mode((self.Width, self.Height))
        
        self.Clock = pygame.time.Clock()

       
        self.background = GameObject(0, 0, self.Width, self.Height, "assets/background.png")

        
               
        self.treasure = GameObject(600, 20, 50, 50,"assets/treasure.png")
        
        
        self.level = 1.0
        
        self.reset_map()
        

    def reset_map(self):
        
        self.player = Player (600, 650, 50, 50, "assets/player.png", 7)
        
        speed = 5 + (self.level *5)

        if self.level >= 4.0:
        
            self.enemies = [
            Enemy(110, 160, 50, 50, "assets/enemy.png", speed),
            Enemy(600, 440, 50, 50, "assets/enemy.png", speed),
            Enemy(1100, 280, 50, 50, "assets/enemy.png", speed)
            ]

        elif self.level >= 2.0:
            
            self.enemies = [
            Enemy(110, 160, 50, 50, "assets/enemy.png", speed),
            Enemy(1100, 280, 50, 50, "assets/enemy.png", speed)
            ]
        elif self.level >= 1.0:
            
            self.enemies = [
            Enemy(600, 440, 50, 50, "assets/enemy.png", speed),
            ]

    
        
    def draw_object(self):
        self.Game_Window.fill (self.white_colour)
        
        self.Game_Window.blit (self.background.image, (self.background.x,self.background.y))

        self.Game_Window.blit (self.treasure.image, (self.treasure.x, self.treasure.y))

        self.Game_Window.blit (self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemies:

            self.Game_Window.blit (enemy.image, (enemy.x, enemy.y))

      

        pygame.display.update()

    def move_objects(self,player_direction):
        self.player.move(player_direction,self.Height)
        for enemy in self.enemies:
            enemy.move(self.Width)
       

    
    def detect_collision(self, object_1, object_2):
            if object_1.y > (object_2.y + object_2.height):
                return False
            elif (object_1.y + object_1.height) < object_2.y: 
                return False
            if object_1.x > (object_2.x + object_2.width):
                return False
            elif (object_1.x + object_1.width) < object_2.x:
                return False
            return True

    def is_collision(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
        if self.detect_collision(self.player,self.treasure):
            self.level += 0.5 
            self.reset_map()
        return False
            
               
    
    
    
    
    def run_game_loop(self):

        player_direction = 0
   

        while True:

            # handle events
            events = pygame.event.get()
            for event in events:
               
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
                   

        
            

            #Execute Logic
            self.move_objects(player_direction)
          
            if self.is_collision():
               self.reset_map()
            #Update Display
            self.draw_object()

            self.Clock.tick (60)