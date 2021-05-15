import pygame as pg
import Engine

WIDTH = HEIGHT = 512
DIMENSIONS = 8
SIZE = HEIGHT // DIMENSIONS
MAX_FPS = 15
Images = {}


def loadImages():
    pieces = ['wp', 'wB', 'wQ', 'wK', 'wR', 'wN', 'bp', 'bQ', 'bK', 'bR', 'bB', 'bN']
    for piece in pieces:
        Images[piece] = pg.transform.scale(pg.image.load('images/' + piece + '.png'), (SIZE, SIZE))


def drawGameState(screen, gs):
    drawBoard(screen, gs.board)
    # drawPieces(screen,gs.board)


def drawBoard(screen, board):
    for i in range(8):
        for j in range(8):
            if ((i + j) % 2) == 0:
                pg.draw.rect(screen, pg.Color('white'), pg.Rect(j * SIZE, i * SIZE, SIZE, SIZE))
            else:
                pg.draw.rect(screen, pg.Color('sea green'), pg.Rect(j * SIZE, i * SIZE, SIZE, SIZE))
            img = board[i][j]
            if img != "--":
                screen.blit(Images[img], pg.Rect(j * SIZE, i * SIZE, SIZE, SIZE))


def main():
    pg.init()
    screen = pg.display.set_mode((HEIGHT, WIDTH))
    clock = pg.time.Clock()
    screen.fill(pg.Color('black'))
    gs = Engine.GameState()
    loadImages()
    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        pg.display.flip()


if __name__ == "__main__":
    main()
