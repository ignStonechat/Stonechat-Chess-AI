import numpy as np
from utils import split_text
from valid_moves_funcs import get_bishop, get_rook

letter_spots = ['a','b','c','d','e','f','g','h'] # Spots of letters on the board

'''
KEEP IN MIND:
The board goes from TOP to BOTTOM
so to go from a2 to a3 you have to do VERTICAL_LOCATION - 1
'''

def get_piece(board, spot):
    horizontal_loc = letter_spots.index(spot[0])
    vertical_loc = 8-(int(spot[1]))
    piece = board[vertical_loc][horizontal_loc]

    return piece

def get_piece_color(piece):
    if piece.islower():
        return 'w'
    else:
        return 'b'

def validate_spot(board, spot):
    horizontal_loc = letter_spots.index(spot[0])
    vertical_loc = 8-(int(spot[1]))
    piece = board[vertical_loc][horizontal_loc]
    piece_color = 'b' if piece.isupper() else 'w'
    # make our lives easier
    piece = piece.lower() if piece != 'p' and piece != 'P' else piece

    if piece == 'p':
        has_double_move = vertical_loc == 6
        if vertical_loc != 7:
            top_row = board[vertical_loc-1]
            kill_left = top_row[horizontal_loc-1]
            kill_right = top_row[horizontal_loc+1]

            # get kill left and right
            # this shit ugly as fuck
            if kill_left != '-' and kill_left.isupper():
                kill_left = f'{letter_spots[letter_spots.index(spot[0])-1]}{int(spot[1])+1}'
            if kill_right != '-' and kill_right.isupper():
                kill_right = f'{letter_spots[letter_spots.index(spot[0])+1]}{int(spot[1])+1}'
            
            piece_in_front = board[vertical_loc-1][horizontal_loc]

            # Finally save and send the valid moves
            valid_moves = []
            valid_moves.append(f'{spot[0]}{int(spot[1])+1}') if piece_in_front == '-' else None
            valid_moves.append(f'{spot[0]}{int(spot[1])+2}') if has_double_move and piece_in_front == '-' else None
            valid_moves.append(kill_left) if kill_left != '-' else None
            valid_moves.append(kill_right) if kill_right != '-' else None

            return horizontal_line
            return valid_moves
        else:
            return 'X' # X means change into something else cuz we hit the end
    
    if piece == 'P':
        has_double_move = vertical_loc == 1
        if vertical_loc != 0:
            piece_in_front = board[vertical_loc+1][horizontal_loc]
            top_row = board[vertical_loc+1]
            kill_left = top_row[horizontal_loc+1]
            kill_right = top_row[horizontal_loc-1]

            # get kill left and right
            # this shit ugly as fuck
            if kill_left != '-' and kill_left.islower():
                kill_left = f'{letter_spots[letter_spots.index(spot[0])+1]}{int(spot[1])-1}'
            if kill_right != '-' and kill_right.islower():
                kill_right = f'{letter_spots[letter_spots.index(spot[0])-1]}{int(spot[1])-1}'

            # Finally save and send the valid moves
            valid_moves = []
            valid_moves.append(f'{spot[0]}{int(spot[1])+1}') if piece_in_front == '-' else None
            valid_moves.append(f'{spot[0]}{int(spot[1])+2}') if has_double_move and piece_in_front == '-' else None
            valid_moves.append(kill_left) if kill_left != '-' else None
            valid_moves.append(kill_right) if kill_right != '-' else None

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

        
        if horizontal_loc < 7:
            if vertical_loc > 1:
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