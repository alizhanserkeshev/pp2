import pygame, time
import random
pygame.init()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

carimg = pygame.image.load("racer/Player.png")

car_width = 44

grass = pygame.image.load("racer/grass.jpg")
yellow_strip = pygame.image.load("racer/yellow_strip.jpg")
strip = pygame.image.load("racer/strip.jpg")


MyFont = pygame.font.SysFont("None", 100)
render_text  = MyFont.render("Game over", 0 , (255,255,255) )

pygame.display.set_caption("RACER")

def obstacle(obs_x, obs_y, obs):
    if obs == 0:
        obs_pic = pygame.image.load("racer/1.png")
    if obs == 1:
        obs_pic = pygame.image.load("racer/2.png")
    if obs == 2:
        obs_pic = pygame.image.load("racer/3.png")
    if obs == 3:
        obs_pic = pygame.image.load("racer/4.png")
    if obs == 4:
        obs_pic = pygame.image.load("racer/5.png")
    if obs == 5:
        obs_pic = pygame.image.load("racer/6.png")
    screen.blit(obs_pic, (obs_x, obs_y))
    

def backround():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(375,0))
    screen.blit(yellow_strip,(375,100))
    screen.blit(yellow_strip,(375,200))
    screen.blit(yellow_strip,(375,300))
    screen.blit(yellow_strip,(375,400))
    screen.blit(yellow_strip,(375,500))
    screen.blit(yellow_strip,(375,600))
    screen.blit(strip, (120,0))
    screen.blit(strip, (680,0))


def car(x,y):
    screen.blit(carimg,(x,y))


screen.fill((119,119,119))


clock = pygame.time.Clock() #

def game_loop():
    bump = True
    x_change = 0
    x = 400
    y = 500
    obstacle_speed = 10
    obs = 0
    y_change = 0
    obs_x = random.randrange(200,650)
    obs_y = -750
    enemy_width = 56
    enemy_height = 125
    
    
    while bump:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bump  = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        
        x += x_change
        

        screen.fill((119,119,119))
        backround()
        obs_y -= (obstacle_speed / 4)
        obstacle(obs_x,obs_y,obs)
        obs_y += obstacle_speed

        car(x,y)
        if x > 680 - car_width or x < 110:
            screen.blit(render_text, (80,200))
            pygame.display.update()
            time.sleep(5)
            game_loop()

        if obs_y > height:
            obs_y = 0 - enemy_height
            obs_x = random.randrange(170, width - 170)
            obs = random.randrange(0,6)
        
        if y < obs_y + enemy_height:
            if x > obs_x and x < obs_x + enemy_width or x + car_width > obs_x and x + car_width < obs_x + enemy_width: 
                screen.blit(render_text, (100,200))
                pygame.display.update()
                time.sleep(2)
                game_loop()


        pygame.display.update() 
        clock.tick(100)


game_loop()
pygame.quit()
quit()


