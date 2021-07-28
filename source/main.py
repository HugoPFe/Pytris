import pygame as pg
from pygame.locals import *

from sprites import *
from constants import *

class Game:
    def __init__(self) -> None:
        pg.init()
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Pytris')

        self.all_sprites = pg.sprite.Group()
        self.current_block = ZBlock(WIDTH/2, 45, self.all_sprites)

        self.running = True
        self.clock = pg.time.Clock()

    def update(self):
        self.all_sprites.update()

    def run(self):
        self.clock.tick(FPS)
        self.check_events()
        self.update()
        self.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

    def draw(self):
        self.screen.fill('black')

        self.all_sprites.draw(self.screen)
        
        pg.display.flip()


if __name__ == '__main__':
    game = Game()

    while game.running:
        game.run()

pg.quit()
