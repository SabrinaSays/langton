import pygame as pg
import time
import setup

#colors
background = (60,60,60)
white = (255,255,255)
black = (0,0,0)

def run():
    # grabbing setup info
    display_size, tile_size, horizontal_tile_len, vertical_tile_len, matrix, ant_position = setup.basic_info()

    #making screen
    pg.init()

    pg.display.set_caption("Langton's Ant")

    screen = pg.display.set_mode(display_size)
    ant_image = pg.image.load("ant.png")
    ant_image = pg.transform.rotozoom(ant_image,0,0.1)
    

    #updating ant and background
    running = True
    while running:
        screen.fill(background)
        draw_grid(display_size, tile_size, screen)
        screen.blit(ant_image,ant_position)
        ant_position[1] += tile_size
        pg.display.update()
        
        time.sleep(1)


        #so the window doesnt freeze
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    pg.quit()




def draw_grid(display_size, tile_size, screen):
    for x in range(0, display_size[0], tile_size):
        pg.draw.line(screen, black, (x,0),(x,display_size[0]))
    
    for y in range(0, display_size[1], tile_size):
        pg.draw.line(screen, black, (0,y),(display_size[1],y))




run()