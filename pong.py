import pygame

##FPS = 60
##
##size = 640, 480
##screen = pygame.display.set_mode((size[0], size[1]))
##pygame.display.set_caption("Pong")
##pygame.font.init()
##clock = pygame.time.Clock()

def sgn(x):
  return 1 if x >= 0 else -1

class Player():
        def __init__(self, size):
                self.x, self.y = 16, size[1]/2
                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
              
        def movement(self,size,direcao):

                if direcao == 1:
                        self.y -= self.speed
                elif direcao == -1:
                        self.y += self.speed        
                
                if self.y <= 0:
                        self.y = 0
                elif self.y >= size[1]-64:
                        self.y = size[1]-64
       
        def draw(self,screen):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Enemy():
        def __init__(self, size):
                self.x, self.y = size[0]-16, size[1]/2
                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
              
        def movement(self,size,ball):
##                keys = pygame.key.get_pressed()
##                if keys[pygame.K_UP]:
##                        self.y -= self.speed
##                elif keys[pygame.K_DOWN]:
##                        self.y += self.speed

                self.y = ball.y - self.padHei/2
                
                if self.y <= 0:
                        self.y = 0
                elif self.y >= size[1]-64:
                        self.y = size[1]-64
       
        def draw(self,screen):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Ball():
        def __init__(self,size):
                self.x, self.y = size[0]/2, size[1]/2
                self.speed_x = -3
                self.speed_y = 3
                self.size = 8
                self.numBat = 0
       
        def movement(self,size,player,enemy):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= size[1]-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        #self.__init__(size)
                        return False
                elif self.x >= size[0]-self.size:
                        #self.__init__(size)
                        self.speed_x = 3
                        return False
                ##wall col
                #paddle col
                        
                #player
                
                for n in range(-self.size, player.padHei):
                    if int(self.y) == int(player.y) + n:
                                if self.x <= player.x + player.padWid and self.speed_x<0:
                                        self.speed_x = abs(self.speed_x)
                                        self.numBat += 1
                                        if abs(self.speed_x) < 5:
                                              self.speed_x += .04*sgn(self.speed_x)
                                              self.speed_y += .04*sgn(self.speed_y)
                                        break
                                n += 1
                
                        
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if int(self.y) == int(enemy.y) + n:
                                if self.x >= enemy.x - enemy.padWid and self.speed_x>0:
                                        self.speed_x = -abs(self.speed_x)
                                n += 1
                ##paddle col

                return True
 
        def draw(self,screen):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))
 
