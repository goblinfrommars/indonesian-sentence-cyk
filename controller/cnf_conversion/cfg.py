import os

start_symbol = 'K'
dic = {}


def display(get_dic):
    for i in get_dic:
        print(i, '-->', end='')
        print(*get_dic[i], sep='|')
        print()


def insert_grammar():
    global dic

    text = open('controller/cnf_conversion/cfg.txt', 'r')
    cfg = text.read().splitlines()

    for i in range(len(cfg)):
        lhs = cfg[i].split(' -> ')[0]
        rhs = set(cfg[i].split(' -> ')[1].split(' | '))
        dic.update({lhs: list(rhs)})

insert_grammar()
