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
