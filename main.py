import pygame as pg
import time
import setup
import copy

#colors
background = (60,60,60)
white = (255,255,255)
black = (0,0,0)


def run():
    # grabbing setup info
    display_size, tile_size, horizontal_tile_len, vertical_tile_len, matrix, mario_position = setup.basic_info()

    #making screen
    pg.init()

    pg.display.set_caption("Langton's Super Mario Ant")

    screen = pg.display.set_mode(display_size)

    # loading in / resizing images
    mario_image = pg.image.load("mario.png")
    mario_image = pg.transform.rotozoom(mario_image,0,0.13)

    coin_image = pg.image.load("coin.png")
    coin_image = pg.transform.rotozoom(coin_image,0,0.1)
    


    # angle mario starts on, upright.
    mario_angle = 0

    #updating mario and background
    running = True
    first_run = True
    while running:
        screen.fill(background)
        draw_grid_lines(display_size, tile_size, screen)

        # for the first run, we just want to draw mario and draw the coins. no movement
        if first_run:
            draw_coins(matrix=matrix, screen=screen, coin_image=coin_image, tile_size=tile_size)
            screen.blit(mario_image, mario_position)

            pg.display.update()

            time.sleep(2)
            first_run = False 
            continue

        update_matrix(matrix=matrix, prev_mario_position=mario_position, tile_size=tile_size)
        draw_coins(matrix=matrix, screen=screen, coin_image=coin_image, tile_size=tile_size)

        # moves mario and saves the angle for the next time we move mario
        mario_angle = move_mario(matrix=matrix, mario_position=mario_position, tile_size=tile_size, screen=screen, mario_image=mario_image, mario_angle=mario_angle)
        
        pg.display.update()

        
        time.sleep(1)


        #a quit event so the window doesnt freeze
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    pg.quit()


def move_mario(matrix, mario_position, tile_size, screen, mario_image, mario_angle):
    '''Mario goes left on when on a coin and right when he isnt on one. Since left and right are relative, we must save what direction Mario is facing.'''
    x_coord = int(mario_position[0]/tile_size)
    y_coord = int(mario_position[1]/tile_size)

    # if mario on coin, turn left
    if matrix[x_coord][y_coord] == 0:
        mario_angle -= 90
    else:
        mario_angle += 90

    # assures angles dont overload
    if mario_angle == -90:
        mario_angle = 270
    elif mario_angle == 450:
        mario_angle = 90

    # rotates marios image
    mario_image = pg.transform.rotozoom(mario_image,mario_angle,1)

    # determines what direction mario goes in based on where hes facing
    if mario_angle == 0 or mario_angle == 360:
        mario_position[1] -= tile_size
    elif mario_angle == 90:
        mario_position[0] -= tile_size
    elif mario_angle == 180:
        mario_position[1] += tile_size
    elif mario_angle == 270:
        mario_position[0] += tile_size

    screen.blit(mario_image, mario_position)

    return mario_angle

def draw_grid_lines(display_size, tile_size, screen):
    '''No functional value, just draws grid lines so its easier to understand'''
    for x in range(0, display_size[0], tile_size):
        pg.draw.line(screen, black, (x,0),(x,display_size[0]))
    
    for y in range(0, display_size[1], tile_size):
        pg.draw.line(screen, black, (0,y),(display_size[1],y))

def update_matrix(matrix, prev_mario_position, tile_size):
    '''updates grid/matrix based on what tile mario just left'''
    x_coord = int(prev_mario_position[0]/tile_size)
    y_coord = int(prev_mario_position[1]/tile_size)

    if matrix[x_coord][y_coord] == 0:
        matrix[x_coord][y_coord] = 1

    elif matrix[x_coord][y_coord] == 1:
        matrix[x_coord][y_coord] = 0

def draw_coins(matrix, screen, coin_image, tile_size):
    '''populates grid with coin images'''
    for x_index, row in enumerate(matrix):
        for y_index, val in enumerate(row):
            # +5 to center coin ever so slightly
            coin_position = [x_index*tile_size + 5, y_index*tile_size]
            if val == 0:
                screen.blit(coin_image, coin_position)





run()