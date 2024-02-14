import os
def walk(dirname):
    print(dirname)
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
dir = os.getcwd()
walk(dir)