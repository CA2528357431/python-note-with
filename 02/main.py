# 上下文管理器

# 特点是可以用with方法
# 有enter（上文）、exit（下文）方法

class myfile:

    def __enter__(self):
        print('enter successfully')
        self.obj = open(self.file,self.model)
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit successfully')
        self.obj.close()

    def __init__(self, file, model):
        self.file = file
        self.model = model

with myfile('test.txt','r') as f:
    while True:
        st = f.read(1)
        print(st)
        if not st :
            break
