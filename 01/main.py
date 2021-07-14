# with


# 可以自动关闭，比较简便

with open('test.txt', 'r') as file:
    while True:
        st = file.read(1)
        print(st)
        if not st :
            break