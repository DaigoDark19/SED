import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 670))
fps = pygame.time.Clock()
runing = True


while runing:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            runing = False

    fps.tick(60)


pygame.quit()
