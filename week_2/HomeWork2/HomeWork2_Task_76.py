# Napraviti program koji mijenja svako pojavljivanje određenog elementa u listi sa drugim
# elementom. Na primjer, zamjena svih 2 sa -2. Npr. lista [1, 2, 3, 2, 4, 2] u [1, -2, 3, -2, 4,
# -2]


def task_76():
    list = [1, 2, 4, 5, 2, 6, 2]
    new_list = []
    for i in list:
        if i == 2:
            i = -2
            new_list.append(i)
        else:
            new_list.append(i)

    print(new_list)


task_76()
