import os


def n_fc(limit):
    i = 0
    while i < limit:
        os.mkdir("tmp/" + str(i))
        i = i + 1


def folders_creator(dirs: str):
    dir_lst = dirs.split(' ')
    for f in dir_lst:
        os.mkdir('tmp/' + f)


n_fc(3)
folders_creator("cat dog mouse")
