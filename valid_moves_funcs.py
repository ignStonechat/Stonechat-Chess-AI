letter_spots = ['a','b','c','d','e','f','g','h'] # Spots of letters on the board

def get_bishop(board, spot):
    horizontal_loc = letter_spots.index(spot[0])
    vertical_loc = 8-(int(spot[1]))
    piece = board[vertical_loc][horizontal_loc]
    piece_color = 'b' if piece.isupper() else 'w'
    # make our lives easier
    piece = piece.lower() if piece != 'p' and piece != 'P' else piece

    left_top = []
    left_bottom = []
    right_top = []
    right_bottom = []

    # Adding positions
    # left_top
    for i in range(1, vertical_loc+1):
        if horizontal_loc-i >= 0:
            future_key = board[vertical_loc-i][horizontal_loc-i]
            key_loc = f'{letter_spots[horizontal_loc-i]}{8-(vertical_loc-i)}'
            if future_key == '-':
                left_top.append(key_loc)
            elif piece_color == 'b' and future_key.islower() or piece_color == 'w' and future_key.isupper():
                left_top.append(key_loc)
                break
            else:
                break
    # left_bottom
    for i in range(1, 8-vertical_loc):
        if horizontal_loc-i >= 0:
            future_key = board[vertical_loc+i][horizontal_loc-i]
            key_loc = f'{letter_spots[horizontal_loc-i]}{8-(vertical_loc+i)}'
            if future_key == '-':
                left_bottom.append(key_loc)
            elif piece_color == 'b' and future_key.islower() or piece_color == 'w' and future_key.isupper():
                left_bottom.append(key_loc)
                break
            else:
                break

    # right_top
    for i in range(1, vertical_loc+1):
        if horizontal_loc+i <= 7:
            future_key = board[vertical_loc-i][horizontal_loc+i]
            key_loc = f'{letter_spots[horizontal_loc+i]}{8-(vertical_loc-i)}'
            if future_key == '-':
                right_top.append(key_loc)
            elif piece_color == 'b' and future_key.islower() or piece_color == 'w' and future_key.isupper():
                right_top.append(key_loc)
                break
            else:
                break
    # right_bottom
    for i in range(1, 8-vertical_loc):
        if horizontal_loc+i <= 7:
            future_key = board[vertical_loc+i][horizontal_loc+i]
            key_loc = f'{letter_spots[horizontal_loc+i]}{8-(vertical_loc+i)}'
            if future_key == '-':
                right_bottom.append(key_loc)
            elif piece_color == 'b' and future_key.islower() or piece_color == 'w' and future_key.isupper():
                right_bottom.append(key_loc)
                break
            else:
                break
    
    valid_moves = left_top + left_bottom + right_top + right_bottom

    return valid_moves


def get_rook(board, spot):
    horizontal_loc = letter_spots.index(spot[0])
    vertical_loc = 8-(int(spot[1]))
    piece = board[vertical_loc][horizontal_loc]
    piece_color = 'b' if piece.isupper() else 'w'
    # make our lives easier
    piece = piece.lower() if piece != 'p' and piece != 'P' else piece

    valid_moves = []
    h_char = spot[0]
    horizontal_line = board[vertical_loc]
    
    # This is just a mess... just typing in random shit at this point
    # It was a mistake making my own chess engine RIP
    left_side = horizontal_line[:horizontal_loc][::-1]
    right_side = horizontal_line[horizontal_loc+1:]
    top_side = [board[i][horizontal_loc] for i in range(0, vertical_loc)][::-1]
    bottom_side = [board[vertical_loc+i][horizontal_loc] for i in range(1, 8-vertical_loc)]

    # HORIZONTAL MOVEMENT
    # Check left
    for i, p in enumerate(left_side):
        if piece_color == 'w' and p.isupper() or piece_color == 'b' and p.islower():
            valid_moves.append(f'{letter_spots[horizontal_loc-(i+1)]}{spot[1]}')
        if p != '-':
            break
        valid_moves.append(f'{letter_spots[horizontal_loc-(i+1)]}{spot[1]}')

    # Check right
    for i, p in enumerate(right_side):
        if piece_color == 'w' and p.isupper() or piece_color == 'b' and p.islower():
            valid_moves.append(f'{letter_spots[horizontal_loc+(i+1)]}{spot[1]}')
        if p != '-':
            break
        valid_moves.append(f'{letter_spots[horizontal_loc+(i+1)]}{spot[1]}')

    # VERTICAL MOVEMENT
    # Check top
    for i, p in enumerate(top_side):
        if piece_color == 'w' and p.isupper() or piece_color == 'b' and p.islower():
            valid_moves.append(f'{spot[0]}{int(spot[1])+(i+1)}')
        if p != '-':
            break
        valid_moves.append(f'{spot[0]}{int(spot[1])+(i+1)}')

    # Check bottom
    for i, p in enumerate(bottom_side):
        if piece_color == 'w' and p.isupper() or piece_color == 'b' and p.islower():
            valid_moves.append(f'{spot[0]}{int(spot[1])-(i+1)}')
        if p != '-':
            break
        valid_moves.append(f'{spot[0]}{int(spot[1])-(i+1)}')

    return valid_moves