def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')

    return wrap_func

@my_decorator
def hello():
    print('helllooo')
hello()
#########################################################################################
class decoratorWithArguments(object):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        def wrapped_f(*args):
            print (f'Decorator arguments: {self.arg1, self.arg2, self.arg3}')
            f(*args)
        return wrapped_f

@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print (f'sayHello arguments: {a1, a2, a3, a4}')

sayHello("say", "hello", "argument", "list")
#####################################################################################
class decoratorWithArguments(object):
    def __call__(self, function):
        def wrap_func(*args):
            addingResult = function(*args)
            if addingResult > 10:
                print('Result > 10')
            elif addingResult < 10:
                print('Result < 10')
            else:
                print('Result = 10')

        return wrap_func

@decoratorWithArguments()
def addTwoValues(a,b):
    c = a + b
    print (c)
    return c

addTwoValues(3, 7)
