import numpy as np
from utils import split_text
from valid_moves_funcs import get_bishop, get_rook
import random

letter_spots = ['a','b','c','d','e','f','g','h'] # Spots of letters on the board
pawn_pieces = ['r','n','b','q'] # Pieces that a pawn can promote to


def move_piece(board, spot, destination):
    horizontal_loc = letter_spots.index(spot[0]) if spot.lower() != 'x' else None
    if horizontal_loc == None:
        return board
    vertical_loc = 8-(int(spot[1]))
    # print(f'Destination: {destination}')
    destination_horizontal_loc = letter_spots.index(destination[0].lower()) if destination[0].lower() != 'x' else None
    if destination_horizontal_loc == None:
        return board
    destination_vertical_loc = 8-(int(destination[1]))
    piece = board[vertical_loc][horizontal_loc]
    piece_color = 'b' if piece.isupper() else 'w'

    # print('='*50)
    # print(f'Spot: {spot}')
    # print(f'Destination: {destination}')
    # print(f'-- Result board --')
    # for l in board:
        # print(l)

    # print(piece)


    # piece = piece.lower()

    valid_moves = validate_spot(board, spot)
    if valid_moves != None and destination in valid_moves:
        board_initial = list(board[vertical_loc])
        board_initial[horizontal_loc] = '-'
        board[vertical_loc] = "".join(board_initial)
        board_initial = list(board[destination_vertical_loc])
        board_initial[destination_horizontal_loc] = piece
        board[destination_vertical_loc] = "".join(board_initial)

        ##### TEMPORARY FIX TO PAWN PROMOTION #####
        if piece == 'p':
            if destination[1] == '8':
                random_piece = random.choice(pawn_pieces)
                new_board = set_piece(board, destination, random_piece)
                return new_board
        elif piece == 'P':
            if destination[1] == '1':
                random_piece = random.choice(pawn_pieces).upper()
                new_board = set_piece(board, destination, random_piece)
                return new_board
        ###########################################

        return board
    else:
        return None

def move_piece_no_check(board, spot, destination):
    board = list(board)
    horizontal_loc = letter_spots.index(spot[0]) if spot.lower() != 'x' else None
    if horizontal_loc == None:
        return board
    vertical_loc = 8-(int(spot[1]))
    destination_horizontal_loc = letter_spots.index(destination[0].lower()) if destination[0].lower() != 'x' else None
    if destination_horizontal_loc == None:
        return board
    destination_vertical_loc = 8-(int(destination[1]))
    piece = board[vertical_loc][horizontal_loc]
    piece_color = 'b' if piece.isupper() else 'w'

    board_initial = list(board[vertical_loc])
    board_initial[horizontal_loc] = '-'
    board[vertical_loc] = "".join(board_initial)
    board_initial = list(board[destination_vertical_loc])
    board_initial[destination_horizontal_loc] = piece
    board[destination_vertical_loc] = "".join(board_initial)

    return board

def set_piece(board, spot, piece):
    horizontal_loc = letter_spots.index(spot[0])
    vertical_loc = 8-(int(spot[1]))

    board_initial = list(board[vertical_loc])
    board_initial[horizontal_loc] = piece
    board[vertical_loc] = "".join(board_initial)

    return board
    
def get_piece(board, spot):
    horizontal_loc = letter_spots.index(spot[0]) if spot.lower() != 'x' else None
    if horizontal_loc == None:
        return None
    vertical_loc = 8-(int(spot[1]))
    piece = board[vertical_loc][horizontal_loc]

    return piece

def get_piece_color(piece):
    if piece.islower():
        return 'w'
    elif piece.isupper():
        return 'b'
    else:
        return None

def validate_spot(board, spot, calling_from=None):
    horizontal_loc = letter_spots.index(spot[0]) if spot.lower() != 'x' else None
    if horizontal_loc == None:
        return None
    vertical_loc = 8-(int(spot[1]))
    piece = board[vertical_loc][horizontal_loc]
    piece_color = 'b' if piece.isupper() else 'w'
    # make our lives easier
    piece = piece.lower() if piece != 'p' and piece != 'P' else piece

    if piece == 'p':
        has_double_move = vertical_loc == 6
        if vertical_loc != 7:
            top_row = board[vertical_loc-1]
            kill_left = None
            kill_right = None
            piece_in_front = None
            double_in_front = None
            if vertical_loc > 0:
                piece_in_front = board[vertical_loc-1][horizontal_loc]
            if has_double_move:
                double_in_front = board[vertical_loc-2][horizontal_loc]
            if horizontal_loc > 0:
                kill_left = top_row[horizontal_loc-1]
            if horizontal_loc < 7:
                kill_right = top_row[horizontal_loc+1]

            # get kill left and right
            # this shit ugly as fuck
            if kill_left != None and kill_left != '-' and kill_left.isupper():
                kill_left = f'{letter_spots[letter_spots.index(spot[0])-1]}{int(spot[1])+1}'
            if kill_right != None and kill_right != '-' and kill_right.isupper():
                kill_right = f'{letter_spots[letter_spots.index(spot[0])+1]}{int(spot[1])+1}'
            

            # Finally save and send the valid moves
            valid_moves = []
            valid_moves.append(f'{spot[0]}{int(spot[1])+1}') if piece_in_front == '-' else None
            valid_moves.append(f'{spot[0]}{int(spot[1])+2}') if has_double_move and piece_in_front == '-' and double_in_front == '-' else None
            valid_moves.append(kill_left) if kill_left != None and kill_left != '-' and kill_left.isupper() else None
            valid_moves.append(kill_right) if kill_right != None and kill_right != '-' and kill_right.isupper() else None

            return valid_moves
        else:
            return 'X' # X means change into something else cuz we hit the end
    
    if piece == 'P':
        has_double_move = vertical_loc == 1
        if vertical_loc != 0:
            piece_in_front = None
            double_in_front = None
            if vertical_loc < 7:
                piece_in_front = board[vertical_loc+1][horizontal_loc]
            if has_double_move:
                double_in_front = board[vertical_loc+2][horizontal_loc]
            top_row = board[vertical_loc+1]
            kill_left = None
            kill_right = None
            if horizontal_loc < 7:
                kill_left = top_row[horizontal_loc+1]
            if horizontal_loc > 0:
                kill_right = top_row[horizontal_loc-1]

            # get kill left and right
            # this shit ugly as fuck
            if kill_left != None and kill_left != '-' and kill_left.islower():
                kill_left = f'{letter_spots[letter_spots.index(spot[0])+1]}{int(spot[1])-1}'
            if kill_right != None and kill_right != '-' and kill_right.islower():
                kill_right = f'{letter_spots[letter_spots.index(spot[0])-1]}{int(spot[1])-1}'

            # Finally save and send the valid moves
            valid_moves = []
            valid_moves.append(f'{spot[0]}{int(spot[1])-1}') if piece_in_front == '-' else None
            valid_moves.append(f'{spot[0]}{int(spot[1])-2}') if has_double_move and piece_in_front == '-' and double_in_front == '-' else None
            valid_moves.append(kill_left) if kill_left != None and kill_left != '-' and kill_left.islower()else None
            valid_moves.append(kill_right) if kill_right != None and kill_right != '-' and kill_right.islower() else None

            return valid_moves
        else:
            return 'X' # X means change into something else cuz we hit the end
    
    

    if piece == 'r':
        valid_moves = get_rook(board, spot)

        return valid_moves

    if piece == 'n':
        valid_moves = []

        top_left = None
        top_right = None
        bottom_left = None
        bottom_right = None
        right_top = None
        right_bottom = None
        left_top = None
        left_bottom = None

        # This was a pain to code holy shit finally its done
        if vertical_loc > 1:
            if horizontal_loc > 0:
                top_left = board[vertical_loc-2][horizontal_loc-1]
            if horizontal_loc < 7:
                top_right = board[vertical_loc-2][horizontal_loc+1]

        if vertical_loc < 6:
            if horizontal_loc > 0:
                bottom_left = board[vertical_loc+2][horizontal_loc-1]
            if horizontal_loc < 7:
                bottom_right = board[vertical_loc+2][horizontal_loc+1]

        
        if horizontal_loc < 6:
            if vertical_loc > 0:
                right_top = board[vertical_loc-1][horizontal_loc+2]
            if vertical_loc < 7:
                right_bottom = board[vertical_loc+1][horizontal_loc+2]

        if horizontal_loc > 1:
            if vertical_loc > 0:
                left_top = board[vertical_loc-1][horizontal_loc-2]
            if vertical_loc < 7:
                left_bottom = board[vertical_loc+1][horizontal_loc-2]

        # Convert to board locations
        if top_left != None:
            if top_left == '-' or piece_color == 'b' and top_left.islower() or piece_color == 'w' and top_left.isupper():
                top_left = f'{letter_spots[horizontal_loc-1]}{8-(vertical_loc-2)}'
                valid_moves.append(top_left)
        if top_right != None:
            if top_right == '-' or piece_color == 'b' and top_right.islower() or piece_color == 'w' and top_right.isupper():
                top_right = f'{letter_spots[horizontal_loc+1]}{8-(vertical_loc-2)}'
                valid_moves.append(top_right)

        if bottom_left != None:
            if bottom_left == '-' or piece_color == 'b' and bottom_left.islower() or piece_color == 'w' and bottom_left.isupper():
                bottom_left = f'{letter_spots[horizontal_loc-1]}{8-(vertical_loc+2)}'
                valid_moves.append(bottom_left)
        if bottom_right != None:
            if bottom_right == '-' or piece_color == 'b' and bottom_right.islower() or piece_color == 'w' and bottom_right.isupper():
                bottom_right = f'{letter_spots[horizontal_loc+1]}{8-(vertical_loc+2)}'
                valid_moves.append(bottom_right)

        if right_top != None:
            if right_top == '-' or piece_color == 'b' and right_top.islower() or piece_color == 'w' and right_top.isupper():
                right_top = f'{letter_spots[horizontal_loc+2]}{8-(vertical_loc-1)}'
                valid_moves.append(right_top)
        if right_bottom != None:
            if right_bottom == '-' or piece_color == 'b' and right_bottom.islower() or piece_color == 'w' and right_bottom.isupper():
                right_bottom = f'{letter_spots[horizontal_loc+2]}{8-(vertical_loc+1)}'
                valid_moves.append(right_bottom)

        if left_top != None:
            if left_top == '-' or piece_color == 'b' and left_top.islower() or piece_color == 'w' and left_top.isupper():
                left_top = f'{letter_spots[horizontal_loc-2]}{8-(vertical_loc-1)}'
                valid_moves.append(left_top)
        if left_bottom != None:
            if left_bottom == '-' or piece_color == 'b' and left_bottom.islower() or piece_color == 'w' and left_bottom.isupper():
                left_bottom = f'{letter_spots[horizontal_loc-2]}{8-(vertical_loc+1)}'
                valid_moves.append(left_bottom)

        return valid_moves

    if piece == 'b':
        valid_moves = get_bishop(board, spot)

        return valid_moves

    if piece == 'q':
        rook_moves = get_rook(board, spot)
        bishop_moves = get_bishop(board, spot)

        return rook_moves + bishop_moves

    if piece == 'k':
        valid_moves = []

        top = None
        bottom = None
        left = None
        right = None
        top_left = None
        top_right = None
        bottom_left = None
        bottom_right = None

        # More epic ugly code (I'll probably fix this later)
        if vertical_loc > 0:
            test_piece = board[vertical_loc-1][horizontal_loc]
            if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                top = f'{letter_spots[horizontal_loc]}{8-(vertical_loc)+1}'

            if horizontal_loc > 0:
                test_piece = board[vertical_loc-1][horizontal_loc-1]
                if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                    top_left = f'{letter_spots[horizontal_loc-1]}{8-(vertical_loc)+1}'

                if vertical_loc < 7:
                    test_piece = board[vertical_loc+1][horizontal_loc-1]
                    if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                        bottom_left = f'{letter_spots[horizontal_loc-1]}{8-(vertical_loc)-1}'

            if horizontal_loc < 7:
                test_piece = board[vertical_loc-1][horizontal_loc+1]
                if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                    top_right = f'{letter_spots[horizontal_loc+1]}{8-(vertical_loc)+1}'

        if horizontal_loc > 0:
            test_piece = board[vertical_loc][horizontal_loc-1]
            if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                left = f'{letter_spots[horizontal_loc-1]}{8-(vertical_loc)}'
        if horizontal_loc < 7:
            test_piece = board[vertical_loc][horizontal_loc+1]
            if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                right = f'{letter_spots[horizontal_loc+1]}{8-(vertical_loc)}'
        if vertical_loc < 7:
            test_piece = board[vertical_loc+1][horizontal_loc]
            if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                bottom = f'{letter_spots[horizontal_loc]}{8-(vertical_loc)-1}'
            if horizontal_loc < 7:
                test_piece = board[vertical_loc+1][horizontal_loc+1]
                if test_piece == '-' or piece_color == 'b' and test_piece.islower() or piece_color == 'w' and test_piece.isupper():
                    bottom_right = f'{letter_spots[horizontal_loc+1]}{8-(vertical_loc)-1}'


        valid_moves.append(top) if top != None else None
        valid_moves.append(right) if right != None else None
        valid_moves.append(bottom) if bottom != None else None
        valid_moves.append(left) if left != None else None
        valid_moves.append(top_left) if top_left != None else None
        valid_moves.append(top_right) if top_right != None else None
        valid_moves.append(bottom_right) if bottom_right != None else None
        valid_moves.append(bottom_left) if bottom_left != None else None

        # print(f'Initial Valid Moves: {valid_moves}')
        if calling_from != 'k':
            valid_moves = check_king_move(board, valid_moves, spot, piece_color)

        return valid_moves


def check_king_move(board, valid_moves, spot, king_color):
    for move in valid_moves:
        new_board = move_piece_no_check(list(board), spot, move)
        # print(new_board)
        for char in letter_spots:
            for i in range(8):
                test_spot = f'{char}{i+1}'
                test_piece = get_piece(new_board, test_spot)
                test_piece_color = get_piece_color(test_piece)
                if test_piece != '-' and test_spot != spot and test_piece_color != king_color:
                    # print(f'[{test_piece}] {test_spot}')
                    test_piece_moves = validate_spot(new_board, test_spot, calling_from='k')
                    for test_move in test_piece_moves:
                        if test_move in valid_moves:
                            valid_moves.remove(test_move)
    
    return valid_moves