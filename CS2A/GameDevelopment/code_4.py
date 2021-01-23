import pygame, random
pygame.init()

width, height = 1000, 600

screen = pygame.display.set_mode((width, height))
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
green = 0,255,0
blue = 0,0,255
colors = [red, black, green, blue]

color = random.choice(colors)

x = 80
y = 80
move_x = 3
move_y = 3

img = pygame.image.load('football.png')

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    #pygame.draw.circle(screen, color, [x,y], 80)
    screen.blit(img, (x,y))
    x += move_x
    y += move_y

    if x >= width - 100:
        move_x = -3
        color = random.choice(colors)
    elif x <= 0:
        move_x = 3
        color = random.choice(colors)

    if y >= height - 100:
        move_y = -3
        color = random.choice(colors)
    elif y <= 0:
        move_y = 3
        color = random.choice(colors)
    pygame.display.update()





