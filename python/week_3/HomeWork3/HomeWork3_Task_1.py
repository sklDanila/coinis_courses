# Napisati funkciju koja za zadati string i slovo vraća listu torki. Svaka torka se odnosi na rečenicu,
# a sastoji se od svih riječi koje se završavaju sa zadatim slovom u toj rečenici, kao i broj riječi koje
# se završavaju sa zadatim slovom u toj rečenici. Primjer: get_words_ends_with_letter (“Print only
# the words that end with the chosen letter in those sentences. Example can contains one or more
# sentences.”, “s”) vraća listu sljedećeg oblika: [(“words”, “sentences”, 2), (“contains”, “sentences”,
# 2)]

import re


def get_words_ends_with_(string, char):
    strings = re.split("[.!?]", string)
    del strings[-1]
    stringse = []
    result = []
    count = 0
    for i in range(len(strings)):
        new_str = strings[i].split(" ")
        for j in new_str:
            if j:
                if j.endswith(char):
                    stringse.append(j)
                    count += 1
        stringse.append(len(stringse))
        result.append(tuple(stringse))
        new_str = []
        stringse = []

    print(result)


get_words_ends_with_(
    "Print onls the words that end with the chosen letter in those sentences. Example can contains one or more sentences.",
    "s",
)


# get_words_ends_with_(
#     "Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences.",
#     "s",
# )
