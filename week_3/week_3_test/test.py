# task_1
# def task_1():
#     friend_1 = 200
#     friend_2 = 100
#     friend_3 = 300

#     if friend_1 > friend_2 and friend_1 > friend_3:
#         print("Win 1st friend")
#     elif friend_2 > friend_1 and friend_2 > friend_3:
#         print("Win 2nd friend")
#     elif friend_3 > friend_1 and friend_3 > friend_2:
#         print("Win 3rd friend")


# task_1()


# task_2


# def task_2():
#     string = "dwbvhbsvbsdbvbs. cdsbhcbsdcsdc! vdsdvnsdvsdvsv. cdscsdcsdc?"

#     count = 0

#     for i in string:
#         if i == "." or i == "!" or i == "?":
#             count += 1

#     print(count)


# task_2()


# task_3


def task_3():
    a = [1, 2, 3, 4, 45]
    b = [2, 3, 4, 67, 78]

    c = []

    for i in a:
        if i in b:
            c.append(i)

    print(c)


task_3()
