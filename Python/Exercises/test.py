import random


def one():
    l = []
    while len(l) < 5:
        inp = input("ANNA:")
        if inp == "":
            break
        l.append(inp)
    return l


def two(l):
    randoms = [random.randrange(0, 9) for i in range(len(l))]
    return randoms


def three(listt=one(), randomsList=two(one())):
    print(randomsList)
    for item in randomsList:
        if item < len(listt):
            print(listt[item])


three()
