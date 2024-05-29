def create_matrix(width, height):
    '''Creates a matrix filled with 0s. 0 meaning not stepped on yet'''
    return [[0 for col in range(width)] for row in range(height)]




def basic_info():
    display_size = [1000,1000]

    #matrix/grid creation
    tile_size = 50
    horizontal_tile_len = int(display_size[0]/tile_size)
    vertical_tile_len = int(display_size[1]/tile_size)

    matrix = create_matrix(width=horizontal_tile_len,height=vertical_tile_len)

    #pixel position on the window
    ant_position = [int(horizontal_tile_len/2)*tile_size, int(vertical_tile_len/2)*tile_size]

    return display_size, tile_size, horizontal_tile_len, vertical_tile_len, matrix, ant_position