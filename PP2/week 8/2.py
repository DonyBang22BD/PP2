#Imports
import pygame, sys, time
import random
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
W = 400
H = 600
SPEED = 5
SCORE = 0
pygame.mixer.music.load('track.mp3')
pygame.mixer.music.play() 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
sc = pygame.display.set_mode((400,600))
sc.fill(WHITE)
pygame.display.set_caption("Game")
 
class Coin(pygame.sprite.Sprite):                               #Coin
    def __init__(self):         
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,W-40),0) 
        self.cscore = 250
    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 1080):
            self.rect.top = 0
            self.rect.center = (random.randint(40, W-40), 0)
 
    def draw(self, surface):
        sc.blit(self.image, self.rect) 

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < W:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    sc.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    sc.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        sc.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          sc.fill(RED)
          sc.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)