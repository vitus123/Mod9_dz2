
def create_operation(operation):
    if operation == "divide":
        def divide(x, y):
            return x / y
        return divide
    elif operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply


square = lambda x: x * x


def square_def(x):
    return x * x


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return [self.a * self.b]


my_func_divide = create_operation('divide')
print(my_func_divide(10, 2))
my_func_multiply = create_operation('multiply')
print(my_func_multiply(5, 4))

print(square(3))
print(square_def(4))

rect_area = Rect(5, 7)
print(rect_area())
