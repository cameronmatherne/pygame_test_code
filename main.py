import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Test")

WHITE = (255,255,255)

FPS = 60
VEL = 5
FRIC = -.12

IMAGE1_WIDTH, IMAGE1_HEIGHT = 100,80
IMAGE_CHARACTER_1 = pygame.image.load(os.path.join('Assets', 'picture1.png'))
CHARACTER_1 = pygame.transform.scale(IMAGE_CHARACTER_1, (100,80)) # resizing original picture

def draw_window(player1):
    WIN.fill(WHITE)   # give environment a white background
    WIN.blit(CHARACTER_1, (player1.x, player1.y)) # co-ordinates where the item will appear
    pygame.display.update()

def main():

    player1 = pygame.Rect(400, 420, IMAGE1_WIDTH, IMAGE1_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]: # left
            player1.x -= VEL
        if keys_pressed[pygame.K_d]: # right
            player1.x += VEL
    



        draw_window(player1)


    pygame.quit()

if __name__ == "__main__":
    main()




