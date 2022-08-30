import time
import pygame
import json

from load_pieces import get_piece

BLOCK_SIZE = 64
MARGIN = 6

# More eye friendly but ORANGE
# white_block_color = pygame.Color(230, 153, 76)
# black_block_color = pygame.Color(219, 126, 33)

# Less eye-friendly board :sob:
white_block_color = pygame.Color(232, 202, 158)
black_block_color = pygame.Color(180, 136, 102)

class Board():
    def __init__(self):
        board_formation = 'RNBQKBNR/PPPPPPPP/--------/--------/--------/--------/pppppppp/rnbqkbnr'
        # board_formation = 'RNBQKBNR/PPPPPPPP/--------/--------/--------/--------/pppppppp/rnbqkbnr'
        # board_formation = 'kk-b----/k-P-N-b-/-RN--B--/--n-pkP-/-r---k--/--q-b---/--------/--------'
        self.board_formation = board_formation.split('/')
        

    def draw_board(self):
        scr = pygame.display.set_mode((512,512))
        for n in range(8):
            if n % 2 == 0:
                for i in range(8):
                    if i % 2 == 0:
                        pygame.draw.rect(scr, black_block_color, pygame.Rect(i*BLOCK_SIZE, n*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                for i in range(8):
                    if not i % 2 == 0:
                        pygame.draw.rect(scr, white_block_color, pygame.Rect(i*BLOCK_SIZE, n*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            else:
                for i in range(8):
                    if not i % 2 == 0:
                        pygame.draw.rect(scr, black_block_color, pygame.Rect(i*BLOCK_SIZE, n*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

                for i in range(8):
                    if i % 2 == 0:
                        pygame.draw.rect(scr, white_block_color, pygame.Rect(i*BLOCK_SIZE, n*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        return scr


    def draw_pieces(self, scr):
        for i, pieces in enumerate(self.board_formation):
            for n, c in enumerate(pieces):
                piece = get_piece(c)
                scr.blit(piece, (n*BLOCK_SIZE+MARGIN,i*BLOCK_SIZE+MARGIN)) if piece != None else None

        return scr