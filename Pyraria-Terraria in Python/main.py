import pygame
import sys
from globals import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.close()
        pygame.display.update()
        self.clock.tick(FPS)
    def draw(self):
        self.screen.fill('lightblue')
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()