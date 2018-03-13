# Projet__Rubics-cube
Now we have a nice virtual Rubick's cube


* Ce code, qui utilise les propriétés des listes, permet de réaliser tous les mouvements conventionnels d'un Rubick's Cube 3x3:

![Mouvements conventionnels du Rubick's Cube 3x3](https://www.rubiks.com/uploads/blog_entries/8.png)

* Chaques listes correspondent à une face du Rubick's Cube selon cet ordre:

![Les faces du Rubick's Cube](https://image.noelshack.com/fichiers/2018/11/1/1520875166-rubick-s-cube.jpg)

* Pour réaliser un mouvement souhaité il suffit d'appeller la fonction correspondante (à savoir le nom du mouvement en minuscule avec comme paramètre *cube* et *amount* qui correspond au nombre de tour que l'on veut réaliser) comme ceci: `ui(cube, 2)` ce code permet de réaliser deux fois le mouvement UI au cube. 

* Pour ensuite afficher le cube utilisez la fonction `show_cube()` de cette manière: `show_cube(ui(cube, 2))` 
