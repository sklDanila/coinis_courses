# Za svaki podcast je poznat naziv, broj pozitivnih komenatara na podcastu i broj negativnih
# komentara na podcastu. Vaš zadatak je da kreirate program kojim pronalazite podcast koji ima
# najgori odnos između pozitivnih i negativnih komentara.
# Primjer: Za niz
# [{‘naziv’:’Español para principiantes’, ‘br_pozitivni’:1000,’br_negativni’:10},
# {‘naziv’:’Philophize This!’, ‘br_pozitivni’:500,’br_negativni’: 30}, {‘naziv’:’Science VS. ’,
# ‘br_pozitivni’:600,’br_negativni’: 45}]
# treba da štampa Science VS.

import keyword


def task_5():
    name = ""
    ratio = 100
    list_dic = [
        {
            "naziv": "Español para principiantes",
            "br_pozitivni": 1000,
            "br_negativni": 10,
        },
        {"naziv": "Philophize This!", "br_pozitivni": 500, "br_negativni": 30},
        {"naziv": "Science VS. ", "br_pozitivni": 600, "br_negativni": 45},
    ]
    for list in list_dic:
        print(list.get("br_pozitivni"))
        if list.get("br_pozitivni") / list.get("br_negativni") < ratio:
            name = list.get("naziv")
    print(name)


task_5()
