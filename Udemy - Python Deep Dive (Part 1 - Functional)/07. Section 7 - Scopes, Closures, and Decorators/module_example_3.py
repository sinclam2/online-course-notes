
def outer_func():
    def inner_func():
        global a
        a = 'hello'
        print(a)

    inner_func()

outer_func()
print(a)
