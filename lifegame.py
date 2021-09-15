#!/usr/bin/env python3
import pygame
import numpy as np
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 50
HEIGHT = 50

pygame.init()

WINDOW_SIZE = [WIDTH*10, HEIGHT*10]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Life Game")
clock = pygame.time.Clock()


class LifeGame:
    def __init__(self):
        self.initial()

    def initial(self):
        self.cell_array = np.random.rand(WIDTH, HEIGHT)
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if self.cell_array[row][col] < 0.1:
                    color = BLACK
                    self.cell_array[row][col] = 1
                    pygame.draw.rect(screen, color, [row * 10, col * 10, 10, 10])
                else:
                    self.cell_array[row][col] = 0

    def update(self):
        for row in range(1, HEIGHT - 2):
            for col in range(1, WIDTH - 2):
                if self.cell_array[row][col] > 0:
                    crop = self.cell_array[row-1:row+2, col-1:col+2]

                    crop_alive_count = np.count_nonzero(crop > 0)
                    crop_alive_row = np.where(crop > 0)[0]
                    crop_alive_col = np.where(crop > 0)[1]

                    # crop_dead_count = np.count_nonzero(crop < 1)
                    crop_dead_row = np.where(crop < 1)[0]
                    crop_dead_col = np.where(crop < 1)[1]

                    # 周围网格中数量多于3个的时候，随机减少至3
                    if crop_alive_count > 3:
                        for i in range(crop_alive_count - 3):
                            krow = np.random.choice(crop_alive_row)
                            kcol = np.random.choice(crop_alive_col)
                            self.cell_array[krow][kcol] = 0
                            pygame.draw.rect(screen, WHITE, [row * 10, col * 10, 10, 10])
                    # 周围网格中数量少于3个时向其周围网格中随机生成一个细胞
                    else:
                        srow = np.random.choice(crop_dead_row)
                        scol = np.random.choice(crop_dead_col)
                        self.cell_array[srow][scol] = 1
                        pygame.draw.rect(screen, BLACK, [row * 10, col * 10, 10, 10])
                time.sleep(1)


screen.fill(WHITE)
game = LifeGame()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    time.sleep(5)
    print("start game!")
    game.update()
    clock.tick(60)
    pygame.display.flip()
    time.sleep(1)
