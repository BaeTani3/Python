
 

# 아래는 게임루프를 포함한 전체 코드입니다.

import pygame
import random
WIDTH=800
HEIGHT=400
FPS=120
BLOCK_SIZE = 40

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW=(255,255,0)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
score = 0
life = 3
all_sprites=pygame.sprite.Group()
player_sprite=pygame.sprite.Group()
coin_sprites=pygame.sprite.Group()
monster_sprites=pygame.sprite.Group()
wall_sprites=pygame.sprite.Group()
map=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
     [1,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,1],
     [1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,1,2,2,1],
     [1,2,1,1,2,1,2,2,1,2,2,2,2,2,2,2,2,2,3,1],
     [1,3,1,1,2,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1],
     [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
     [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,2,1,1,2,1],
     [1,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,1,2,1],
     [1,2,1,1,2,2,2,1,2,3,2,1,2,2,2,1,2,2,3,1],
     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
     ]

#초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("score: 0")
clock=pygame.time.Clock()

def drawmap():
    y=0
    x=0
    for i in map:
        y=0
        for j in i:
            if j==1:
                Wall(y,x)
            if j==2:
                Coin(y,x)
            if j==3:
                Monster(y,x)
            y+=1
        x+=1
class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface([BLOCK_SIZE,BLOCK_SIZE])
        self.rect=self.image.get_rect()
        self.rect.x=x*BLOCK_SIZE
        self.rect.y=y*BLOCK_SIZE
        
        wall_sprites.add(self)
        all_sprites.add(self)
        
class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        radius = 2
        # 이미지 생성
        self.image = pygame.Surface([4,4], pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (radius,radius), radius)

        # 위치 설정
        self.rect = self.image.get_rect()
        self.rect.x = x * BLOCK_SIZE + BLOCK_SIZE//2
        self.rect.y = y * BLOCK_SIZE + BLOCK_SIZE//2
        # Sprite 그룹에 추가
        all_sprites.add(self)
        coin_sprites.add(self)
    def update(self):
        if pygame.sprite.spritecollide(self,player_sprite,False):
            self.kill()
            global score
            score += 10
            pygame.display.set_caption("score: " + str(score))
class Monster(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        radius = 10
        # 이미지 생성
        self.image = pygame.Surface([20,20], pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (radius,radius), radius)

        # 위치 설정
        self.rect = self.image.get_rect()
        self.rect.x = x * BLOCK_SIZE + 10
        self.rect.y = y * BLOCK_SIZE + 10
       
        self.direction=random.choice(directions)
        # Sprite 그룹에 추가
        all_sprites.add(self)
        monster_sprites.add(self)
    def update(self):
        dx,dy=self.direction
        # 랜덤한 방향 선택
        # 현재 위치에서 dx, dy 만큼 이동
        self.rect.x += dx
        self.rect.y += dy 
        
        if pygame.sprite.spritecollide(self, wall_sprites, False, pygame.sprite.collide_rect) or not 0 <= self.rect.x < WIDTH or not 0 <= self.rect.y < HEIGHT:
            self.rect.x -= dx 
            self.rect.y -= dy
            self.direction=random.choice(directions)
    
class Pacman(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        radius = 10
    
        self.image = pygame.Surface([20,20], pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (radius,radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = x * BLOCK_SIZE + 10
        self.rect.y = y * BLOCK_SIZE + 10
      
        all_sprites.add(self)
        player_sprite.add(self)
    def update(self):
        keys = pygame.key.get_pressed()
        dx,dy = 0,0
        if keys[pygame.K_LEFT]:
            dx=-1
        elif keys[pygame.K_RIGHT]:
            dx=1    
        elif keys[pygame.K_UP]:
            dy=-1
        elif keys[pygame.K_DOWN]:
            dy=1
        self.rect.x+=dx
        self.rect.y+=dy
        #벽과 충돌 감지
        if pygame.sprite.spritecollide(self,wall_sprites,False,pygame.sprite.collide_rect):
           self.rect.x-=dx
           self.rect.y-=dy
        #몬스터와 충돌 감지
        if pygame.sprite.spritecollide(self,monster_sprites,False,pygame.sprite.collide_rect):
            pygame.quit()
            quit()
                
drawmap()
pacman=Pacman(6,5)
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLUE)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
game_loop()