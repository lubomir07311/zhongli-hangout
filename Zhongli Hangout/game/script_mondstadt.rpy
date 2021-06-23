define s = Character("Sara", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])
define tim = Character("Timaeus", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])
define n = Character("Noelle", color="#FFD700", who_outlines=[(2, "#000", 0, 0)])

label mondstadt_square:
    scene bg ms_sq with fade
    pause 3
    show zh happy at left
    show paimon happy at center

    p "We made it!"
