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

def calculate(func):
    def inner(a, b):
        print(f"Going to perform division on, {a} and {b}")
        func(a, b)
    return inner

@calculate
def divide(a, b):
    print(a/b)

divide(10, 5)

