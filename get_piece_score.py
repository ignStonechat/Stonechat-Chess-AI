from move_utils import get_piece

values = {
    '-': 0,
    'p': 1,
    'n': 3,
    'b': 3,
    'r': 5,
    'q': 9,
    'k': 10,
    'x': 10,
}

def get_score(board, spot):
    score = 0
    piece = get_piece(board, spot)
    if piece != None:
        score = values[piece.lower()]

    return score