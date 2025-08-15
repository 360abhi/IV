def deco(func):
    def wrapper():
        print("Before calling function")
        func()
        print("After calling function")
    return wrapper


@deco
def hello():
    print("this is inside hello function")

hello()