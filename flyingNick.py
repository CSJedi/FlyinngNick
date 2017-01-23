import pygame
from pygame.locals import *
import sys
import random

class FlyingNick:
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 708))
        self.nick = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("assets/background.jpg").convert()
        self.nickSprite = [pygame.image.load("assets/22.png").convert_alpha(),
                            pygame.image.load("assets/02.png").convert_alpha(),
                            pygame.image.load("assets/dead.png")]                      
        self.blockUp = pygame.image.load("assets/bottom.png").convert_alpha()
        self.blockDown = pygame.image.load("assets/top.png").convert_alpha()
        self.gap = 170
        self.blockX = 400
        self.nickY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110)
        
    def updateBlocks(self):
        self.blockX -= 2
        if self.blockX < -80:
            self.blockX = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)
            
    def personageUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.nickY -= self.jumpSpeed
            self.jump -= 1
        else:
            self.nickY += self.gravity
            self.gravity += 0.2     
            self.nick[1] = self.nickY   
        up = pygame.Rect(self.blockX, 
                        360 + self.gap - self.offset + 10, 
                        self.blockUp.get_width() - 10, 
                        self.blockUp.get_height())
        down = pygame.Rect(self.blockX, 
                            0 - self.gap - self.offset - 10, 
                            self.blockUp.get_width() - 10, 
                            self.blockUp.get_height())
        if up.colliderect(self.nick):
            self.dead = True
        if down.colliderect(self.nick):
            self.dead = True
        if not 0 < self.nick[1] < 720:
            self.nick[1] = 50
            self.nickY = 50
            self.dead = False
            self.counter = 0
            self.blockX = 400
            self.offset = random.randint(-110, 110)
            self.gravity = 5
    
    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Times New Roman", 50)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 10
            
            self.screen.fill((255,255,255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.blockUp, (self.blockX ,360 + self.gap - self.offset ))
            self.screen.blit(self.blockDown, (self.blockX , 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter), -1, (255, 255, 255)), (200, 50))
            
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            
            self.screen.blit(self.nickSprite[self.sprite], (70 ,self.nickY))
            if not self.dead:
                self.sprite = 0
            self.updateBlocks()
            self.personageUpdate()
            pygame.display.update()
        
if __name__ == "__main__":
    FlyingNick().run()
    