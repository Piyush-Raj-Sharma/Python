def calculate(decorated):
    def inner():
        print("Hey this line is before the function gets decorated")
        decorated()
        print("Hey this line is after the function gets decorated")
    return inner

@calculate
def add():
    print("I'm executed from the decorated function")

add()