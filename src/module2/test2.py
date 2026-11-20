

def my_decorator(fun):
    print('decorator')
    def wrapper():
        print('before function execution')
        fun()
        print('after function execution')
    return wrapper

@my_decorator
def welcome():
    print('welcome function is called in test2')

@my_decorator
def addition():
    print('addition')

welcome
addition

