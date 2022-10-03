import imp
import pygame
from chess.board import Board
from util.utils import WINDOW_SIZE, WIDTH, HEIGHT, MARGIN, BLACK

if __name__ == "__main__":

    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                #grid[row][column] = 1
                #print("Click ", pos, "Grid coordinates: ", row, column)
    
        # Set the screen background
        screen.fill(BLACK)

        board = Board.Board()
        board.draw_grid(screen)

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()



    

