# def calculate(decorated):
#     def inner():
#         print("Hey this line is before the function gets decorated")
#         decorated()
#         print("Hey this line is after the function gets decorated")
#     return inner

# @calculate
# def add():
#     print("I'm executed from the decorated function")

# add()


# Decorators with Arguments and Parameters
# def calculate(func):
#     def inner(a, b):
#         print(f"Going to perform division on, {a} and {b}")
#         func(a, b)
#     return inner

# @calculate
# def divide(a, b):
#     print(a/b)

# divide(10, 5)
# divide(20, 5)


# Decorator Chaining 
def star(func):
    def inner(*agrs, **kwagrs):
        print("*" * 10)
        func(*agrs, **kwagrs)
        print("*" * 10)
    return inner

def percentage(func):
    def inner(*agrs, **kwagrs):
        print("%" * 10)
        func(*agrs, **kwagrs)
        print("%" * 10)
    return inner

@star
@percentage
def greet(msg):
    print(msg)
greet("hello")

#this will be something like star(percentage(greet))
# greet = star(percentage(greet))

