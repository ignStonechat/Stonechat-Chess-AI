from board import Board
from move_utils import validate_spot, move_piece
from mouse_utils import get_quadrant, get_piece, get_piece_spot
import move_utils as ASS
# from load_pieces import get_piece
import pygame
import time

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

import random
def move_random_black_piece():
    while True:
        randx = random.randint(1, 7)
        randy = random.randint(1, 7)
        spot = f'{letter_spots[randx]}{randy}'
        piece = ASS.get_piece(board.board_formation, spot)

        if piece.isupper():
            valid_moves = validate_spot(board.board_formation, spot)
            if valid_moves != None and len(valid_moves) > 0:
                random_move = random.choice(valid_moves)
                new_board = move_piece(board.board_formation, spot, random_move)
                if new_board != None:
                    board.board_formation = new_board
                    scr = board.draw_board()
                    scr = board.draw_pieces(scr)
            
                break


while True:
    # try:
    mousex, mousey = pygame.mouse.get_pos()

    mouse_pos = get_piece_spot(board.board_formation, mousex, mousey)
    mouse_pressed = pygame.mouse.get_pressed()[0]

    if mouse_pressed:
        if first_piece == None:
            first_piece = mouse_pos
        elif second_piece == None:
            second_piece = mouse_pos
            new_board = move_piece(board.board_formation, first_piece, second_piece)
            if new_board != None:
                board.board_formation = new_board
                scr = board.draw_board()
                scr = board.draw_pieces(scr)
                pygame.display.update()

                # move_random_black_piece()



            first_piece = None
            second_piece = None
        time.sleep(0.1)

    # print(f'First Selected: {first_piece}')

    # move = input('Move > ')
    # spot = move[0]+move[1]
    # destination = move[2]+move[3]
    # # print(validate_spot(board.board_formation, move))
    # new_board = move_piece(board.board_formation, spot, destination)
    # if new_board != None:
    #     board.board_formation = new_board
    scr = board.draw_board()
    scr = board.draw_pieces(scr)
    # else:
    #     print(f'Invalid move')

    pygame.display.update()
    # print(f'{round(1/(time.time() - last_loop_time))} FPS')
    last_loop_time = time.time()
    # except Exception as e:
    #     print(e)




# while True:
#     # try:
#     pygame.display.update()
#     move = input('Move > ')
#     spot = move[0]+move[1]
#     destination = move[2]+move[3]
#     # print(validate_spot(board.board_formation, move))
#     new_board = move_piece(board.board_formation, spot, destination)
#     if new_board != None:
#         board.board_formation = new_board
        # scr = board.draw_board()
        # scr = board.draw_pieces(scr)
#     else:
#         print(f'Invalid move')

#     print(f'{round(1/(time.time() - last_loop_time))} FPS')
#     last_loop_time = time.time()
#     # except Exception as e:
#     #     print(e)