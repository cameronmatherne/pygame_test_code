import pygame
import os
import time 


pygame.init() 

# set window dimensions, initialize window, create game caption 
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Test")

WHITE = (255,255,255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

IMAGE1_WIDTH, IMAGE1_HEIGHT = 100,80


IMAGE_CHARACTER_1 = pygame.image.load(os.path.join('Assets', 'picture1.png'))
BACKGROUND = pygame.image.load(os.path.join('Assets', 'background.png'))

CHARACTER_1 = pygame.transform.scale(IMAGE_CHARACTER_1, (100,80)) # resizing original picture


# method that draws background window, as well as first entity 
def draw_window(player1):
    WIN.fill(WHITE) # white background initially / might not be needed 
    WIN.blit(BACKGROUND, (0,0))  # give environment an image background
    WIN.blit(CHARACTER_1, (player1.x, player1.y)) # co-ordinates where the item will appear
    pygame.display.update()

    
def main():

    x = 400
    y = 310
    floor = 310 
    frames = 60 

    VEL = 5
    MASS = 1 

    isJumping = False 
    jumpCount = 10

    player1 = pygame.Rect(x, y, IMAGE1_WIDTH, IMAGE1_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(frames)
        WIN
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # call method to draw background and player1 
        draw_window(player1)



        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: # left
            player1.x -= VEL
        if keys_pressed[pygame.K_d]: # right
            player1.x += VEL

        if keys_pressed[pygame.K_SPACE]: # jump 
            isJumping = True
    

        if isJumping: 
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                player1.y -= jumpCount**2 * .1 * neg
                jumpCount -= 1 
            else:
                isJumping = False
                jumpCount = 10 
       



    pygame.quit()

if __name__ == "__main__":
    main()




