import pygame
import pong

size = [640, 480]
screen = pygame.display.set_mode((size[0], size[1]))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

def jogar(individuo,numBat=30, multVel = 1):

    FPS = int(multVel*60)

    ball = pong.Ball(size)
    player = pong.Player(size)
    enemy = pong.Enemy(size)

    cont = True
    ganhou = False
    while cont:
            #process
            for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    print ("Game exited by user")
                                    exit()
            ##process

            #entradas = player.y, ball.x, ball.y, ball.speed_x, ball.speed_y
            entradas = [2.0*(player.y + player.padHei/2)/size[1] -1, 2.0*ball.x/size[0]-1, 2.0*ball.y/size[1]-1, ball.speed_x/3.0, ball.speed_y/3.0]

            direcao = individuo.calcular_acao(entradas)
               
            #logic
            cont = ball.movement(size,player,enemy)
            player.movement(size,direcao)
            enemy.movement(size, ball)
            ##logic
            
            #draw
            screen.fill((0, 0, 0))
            ball.draw(screen)
            player.draw(screen)
            enemy.draw(screen)
            ##draw
            
            #_______
            pygame.display.flip()
            clock.tick(FPS)

            if ball.numBat > numBat:
                cont = False
                ganhou = True

    gameState = [2.0*(player.y + player.padHei/2)/size[1] -1, 2.0*ball.x/size[0]-1, 2.0*ball.y/size[1]-1, ball.speed_x/3.0, ball.speed_y/3.0, ball.numBat, ganhou]

    return(gameState)

