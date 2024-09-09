

def text_function():
    x='объемлющая'

    def inner_function():
        nonlocal x
        x='Я в области видимости функции text_function'

    inner_function()
    print(x)
    return x

text_function()
