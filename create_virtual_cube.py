"""

Ce code permet de créer rapidement son Rubick's cube virtuel exploitable par le script "rubicks_cube.py". Il revoit une string de ce genre que l'on peut copier-coller :

face_1 = ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
face_2 = ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']
face_3 = ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']
face_4 = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
face_5 = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G']
face_6 = ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']

P.S : Il peut surement être amélioré (je n'ai pas passé beaucoup de temps dessus) alors lâchez vous ;)

"""

def create_virtual_cube():
    counter = 1
    face_counter = 0
    ALL_COLOR_NUMBER = 54
    color_list = []
    final_show = []
    while counter <= ALL_COLOR_NUMBER:
        color = input(f"color face_{face_counter}: ")
        color_list += [color.upper()]
        if counter % 9 == 0:
            face_counter += 1
            final_show += [f"face_{face_counter} = {color_list}"]
            color_list = []
        counter += 1        
        if color == 'exit':
            return None
    for element in final_show:
        print(element)
        
#create_virtual_cube()
