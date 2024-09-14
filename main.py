import pygame 
from random import randint 


pygame.init()

pygame.display.set_caption("Move the Car")
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
score = 0
game_over = False
keys = [False,False,False,False]
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("img/car.png")
    self.image = pygame.transform.scale(self.image,(100,130))
    self.rect = self.image.get_rect()

  def update(self,pressed_keys):
    if pressed_keys[pygame.K_UP]:
       self.rect.move_ip(0,-20)
    if pressed_keys[pygame.K_DOWN]:
       self.rect.move_ip(0,20)
    if pressed_keys[pygame.K_LEFT]:
        self.rect.move_ip(-20,0)
    if pressed_keys[pygame.K_RIGHT]:
        self.rect.move_ip(20,0)


    if self.rect.left <0:
        self.rect.left = 0
    if self.rect.right > screen_width:
        self.rect.right =  screen_width
    if self.rect.top <0:
        self.rect.top = 0
    if self.rect.bottom > screen_height:
        self.rect.bottom = screen_height

sprites = pygame.sprite.Group() 

def start_game():
    player = Player()
    sprites.add(player) 

    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit(0)

      pressed_keys = pygame.key.get_pressed()
      player.update(pressed_keys)

      screen.blit(pygame.image.load("img/background.png"),(0,0))
      sprites.draw(screen)
      pygame.display.update()

start_game()

