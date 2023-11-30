# import the pygame module, so you can use it
import pygame
from src.Screen import Screen
 
# define a main function
def main():

    # initialize the pygame module
    pygame.init()

    # initialize Screen
    screen = Screen()
    
    #gameloop
    while screen.isRunning():
        screen.update()
        screen.render()
     
if __name__=="__main__":
    # call the main function
    main()