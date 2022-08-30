from board import Board
from move_utils import move_piece_no_check, validate_spot, move_piece
from mouse_utils import get_quadrant, get_piece, get_piece_spot
import move_utils as MU
from get_piece_score import get_score
from minimax import minimax, minimax_from_minimax,flatten
# from load_pieces import get_piece
import pygame
import time
import json
import numpy as np

pygame.init()

board = Board()
scr = board.draw_board()
scr = board.draw_pieces(scr)
pygame.display.set_caption('Stonechat\'s Chess AI')

last_loop_time = time.time()

mouse = pygame.mouse

first_piece = None
second_piece = None

letter_spots = ['a','b','c','d','e','f','g','h'] # Spots of letters on the board

TREE_DEPTH = 1
def move_black_piece(board):
    mm1 = minimax(board)
    print('Finished MM-1')
    # mm2 = minimax_from_minimax(board, mm1)
    # print('Finished MM-2')

    # mm2_move = min(mm2)
    # mm1_move = max(mm1)

    print(mm1)
    # print('='*50)
    # print(mm2)

last_loop_time = time.time()
while True:

    mouse_pressed = pygame.mouse.get_pressed()[0]

    if mouse_pressed:
        mousex, mousey = pygame.mouse.get_pos()
        mouse_pos = get_piece_spot(board.board_formation, mousex, mousey)
        if first_piece == None:
            first_piece = mouse_pos
        elif second_piece == None:
            second_piece = mouse_pos
            new_board = move_piece(board.board_formation, first_piece, second_piece)
            if new_board != None:
                board.board_formation = new_board
                move_black_piece(board.board_formation)
                pygame.display.update()



            first_piece = None
            second_piece = None
        time.sleep(0.2)

    # print(f'First Selected: {first_piece}')
    scr = board.draw_board()
    scr = board.draw_pieces(scr)



    pygame.display.update()
    # print(f'{round(1/(time.time() - last_loop_time))} FPS')
    last_loop_time = time.time()