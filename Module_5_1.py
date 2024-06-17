def test_function(x):
    a = x

    def inner_function(x):
        a = x + "Я в области видимости функции test_function"
        print(a)

    return a
test_function()