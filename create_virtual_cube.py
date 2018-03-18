"""

Ce code permet de créer rapidement son Rubick's cube virtuel exploitable par le script "rubicks_cube.py". Il renvoit une string de ce genre que
l'on peut copier-coller :

face_1 = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
face_2 = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
face_3 = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
face_4 = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
face_5 = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
face_6 = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']

P.S : Il peut surement être amélioré (je n'ai pas passé beaucoup de temps dessus) alors lâchez vous ;)

"""

from random import choice, randrange
from rubicks_cube import *

NUMBER_OF_FACES = 9
MOVEMENTS = [r, ri, l, li, b, bi, d, di, f, fi, u, ui]
ONE_MOVE = 1

def create_virtual_cube():
    print("""
        Insert color from top-left to bottom-right.
        That is to say:
        1 2 3
        4 5 6
        7 8 9
        """)
    cube = []
    for n_face in range(1, NUMBER_OF_FACES+1):
        cube += [input(f"color face n°{n_face}: ").replace(' ', '').upper()]
    return cube

def random_cube():
    (face_1, face_2, face_3) = (['W'] * 9, ['B'] * 9, ['Y'] * 9)
    (face_4, face_5, face_6) = (['O'] * 9, ['G'] * 9, ['R'] * 9)
    cube = [face_1, face_2, face_3, face_4, face_5, face_6]

    for loop in range(randrange(30, 50)): # How many iterations ?
        MOVEMENTS[randrange(12)](cube, ONE_MOVE)
    return cube

print(random_cube())