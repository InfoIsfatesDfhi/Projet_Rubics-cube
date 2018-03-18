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

from rubicks_cube import *
from random import choice

NUMBER_OF_FACES = 9

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