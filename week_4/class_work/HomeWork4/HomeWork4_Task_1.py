# 1. Data je lista stringova ["flower","flow","flight"]. Napisati funkciju koja koristi reduce da nađe najduži
# string među datim stringovima.

from functools import reduce


def task_1(words_list):
    max_string = reduce(lambda x, y: x if len(x) > len(y) else y, words_list)
    return max_string


words_list = ["flower", "flow", "flight"]
print(task_1(words_list))
