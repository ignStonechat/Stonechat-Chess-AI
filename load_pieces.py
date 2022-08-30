import pygame

PIECE_SIZE = 48

# White pieces
w_pawn = pygame.image.load('./Stripes/White/pawn.png')
w_pawn = pygame.transform.scale(w_pawn, (PIECE_SIZE,PIECE_SIZE))

w_rook = pygame.image.load('./Stripes/White/rook.png')
w_rook = pygame.transform.scale(w_rook, (PIECE_SIZE,PIECE_SIZE))

w_knight = pygame.image.load('./Stripes/White/knight.png')
w_knight = pygame.transform.scale(w_knight, (PIECE_SIZE,PIECE_SIZE))

w_bishop = pygame.image.load('./Stripes/White/bishop.png')
w_bishop = pygame.transform.scale(w_bishop, (PIECE_SIZE,PIECE_SIZE))

w_queen = pygame.image.load('./Stripes/White/queen.png')
w_queen = pygame.transform.scale(w_queen, (PIECE_SIZE,PIECE_SIZE))

w_king = pygame.image.load('./Stripes/White/king.png')
w_king = pygame.transform.scale(w_king, (PIECE_SIZE,PIECE_SIZE))


# Black pieces
b_pawn = pygame.image.load('./Stripes/Black/pawn.png')
b_pawn = pygame.transform.scale(b_pawn, (PIECE_SIZE,PIECE_SIZE))

b_rook = pygame.image.load('./Stripes/Black/rook.png')
b_rook = pygame.transform.scale(b_rook, (PIECE_SIZE,PIECE_SIZE))

b_knight = pygame.image.load('./Stripes/Black/knight.png')
b_knight = pygame.transform.scale(b_knight, (PIECE_SIZE,PIECE_SIZE))

b_bishop = pygame.image.load('./Stripes/Black/bishop.png')
b_bishop = pygame.transform.scale(b_bishop, (PIECE_SIZE,PIECE_SIZE))

b_queen = pygame.image.load('./Stripes/Black/queen.png')
b_queen = pygame.transform.scale(b_queen, (PIECE_SIZE,PIECE_SIZE))

b_king = pygame.image.load('./Stripes/Black/king.png')
b_king = pygame.transform.scale(b_king, (PIECE_SIZE,PIECE_SIZE))

pieces = {
    'p': 'w_pawn',
    'r': 'w_rook',
    'n': 'w_knight',
    'b': 'w_bishop',
    'q': 'w_queen',
    'k': 'w_king',

    'P': 'b_pawn',
    'R': 'b_rook',
    'N': 'b_knight',
    'B': 'b_bishop',
    'Q': 'b_queen',
    'K': 'b_king'
}

def get_piece(piece):
    if piece != '-':
        return eval(pieces[piece])
    else:
        return None