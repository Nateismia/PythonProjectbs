import pygame

#the following is taken from the offical documentation (so edit as we go for tictactoe)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    #(documentation says "poll for events" so i assume that means put the input listeners here)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fills screen with purple to clear away last frame
    screen.fill("white")

    # Render game here
    colour = (000, 0, 0)
    Lrect = (450, 50, 25, 525)
    Rrect = (725, 50, 25, 525)
    Trect = (300, 200, 600, 25)
    Brect = (300, 400, 600, 25)
    pygame.draw.rect(screen, colour, Lrect)
    pygame.draw.rect(screen, colour, Rrect)
    pygame.draw.rect(screen, colour, Trect)
    pygame.draw.rect(screen, colour, Brect)

    #below displays the rendered stuff to screen
    pygame.display.flip()

    clock.tick(60)#60 fps limit

pygame.quit()