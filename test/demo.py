def func1():
    return func3()

def func3():
    return(func2())

def func2():
    print("Hello")

func1()