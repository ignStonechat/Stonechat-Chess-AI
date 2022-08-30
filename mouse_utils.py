import numpy as np
import pygame

letter_spots = ['a','b','c','d','e','f','g','h'] # Spots of letters on the board

# Epic high IQ maths here
def get_quadrant(x,y):
    xloc = int(x/64)
    yloc = int(y/64)

    return xloc, yloc

def get_piece(board,x,y):
    xloc, yloc = get_quadrant(x,y)

    return board[yloc][xloc]

def get_piece_spot(board,x,y):
    xloc, yloc = get_quadrant(x,y)

    return f'{letter_spots[xloc]}{8-yloc}'
