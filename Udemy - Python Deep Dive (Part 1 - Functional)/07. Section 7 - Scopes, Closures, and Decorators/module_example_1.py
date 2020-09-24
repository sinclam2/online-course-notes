
def outer_func():
    a = 10
    def inner_func():
        print(a)

    inner_func()

outer_func()
