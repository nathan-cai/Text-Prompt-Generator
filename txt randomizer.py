import random


def random_passage():
    f = open('sentences.txt', 'r')
    l = f.readlines()
    choice = random.randint(0, len(l) - 1)
    print(l)
    return(l[choice])


print(random_passage())
