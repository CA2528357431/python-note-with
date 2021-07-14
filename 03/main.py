# 上下文管理

import contextlib


@contextlib.contextmanager
def myfile(file, model):

    # enter
    print('enter successfully')
    print('-'*50)
    f = open(file, model)
    yield f

    # exit
    f.close()
    print('-' * 50)
    print('exit successfully')

with myfile('test.txt','r') as f:
    while True:
        st = f.read(1)
        print(st)
        if not st:
            break
