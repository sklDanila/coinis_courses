# 4. Data je lista ["Hello, World!", "Python is cool", "Functional programming rocks"]. Napisati funkciju
# koja broji ukupan broj riječi u svim stringovima koristeći map i reduce

from functools import reduce


def task_4(list_of_sentences):
    split_words_in_all_sentences = map(
        lambda sentence: sentence.split(), list_of_sentences
    )
    in_all_sentences = reduce(lambda x, y: x + y, split_words_in_all_sentences)
    count_words_in_all_sentences = len(in_all_sentences)
    return count_words_in_all_sentences


print(task_4(["Hello, World!", "Python is cool", "Functional programming rocks"]))
