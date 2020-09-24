
a = 10

def outer_func():
    def inner_func():
        print(a)

    inner_func()

outer_func()
