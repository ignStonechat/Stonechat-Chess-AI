import json
import move_utils as MU
from get_piece_score import get_score

letter_spots = ['a','b','c','d','e','f','g','h'] # Spots of letters on the board

# def minimax(board, color='b'):
#     black_pieces = []
#     white_pieces = []

#     # Add pieces
#     for char in letter_spots:
#         for i in range(8):
#             spot = f'{char}{i+1}'
#             piece = MU.get_piece(board, spot)
#             piece_color = MU.get_piece_color(piece)
#             items = [spot, piece]
#             if piece_color == 'b':
#                 black_pieces.append(items)
#             elif piece_color == 'w':
#                 white_pieces.append(items)

#     scored = {}
#     if color == 'b':
#         for piece in black_pieces:
#             moves = MU.validate_spot(board, piece[0])
#             moves_n = len(moves)
#             if moves_n != 0:
#                 for move in moves:
#                     score = get_score(board, move)
#                     movement = f'{piece[0]}{move}'
#                     scored[movement] = {
#                         'score': score
#                     }


#     return scored

def get_pieces(board, color='b'):
    pieces = []
    # Add pieces
    for char in letter_spots:
        for i in range(8):
            spot = f'{char}{i+1}'
            piece = MU.get_piece(board, spot)
            piece_color = MU.get_piece_color(piece)
            items = [spot, piece]
            if piece_color == color:
                pieces.append(items)
    
    return pieces

def minimax(board, color='b'):
    black_pieces = get_pieces(board, 'b')
    white_pieces = get_pieces(board, 'w')


    if color == 'b':
        layer = []
        ### Maximize
        for piece in black_pieces:
            moves = MU.validate_spot(board, piece[0])

            for move in moves:
                score = get_score(board, move)
                layer.append([piece[0], move, score])
        return layer
    
    # print(json.dumps(layers, indent=4))


# def minimaxize(board, color='b', depth=2):
    



def minimax_from_minimax(board, scored, color='b'):
    new_scored = scored


    return scored

def flatten(xss):
    return [x for xs in xss for x in xs]