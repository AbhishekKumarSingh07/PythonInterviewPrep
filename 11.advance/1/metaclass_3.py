"""
Extension of metaclass_2.py
"""

class Foo:
    def show(self):
        print("Hello Akki")
        

def outer_method(self):
    self.variable = 9

Test = type('Test', (Foo,), {'x':5, "method":outer_method})
test : Test = Test()

test.show()
print(f"Printing 'x' from class declaration: {test.x}")
test.method()
print(f"Printing 'variable' from outer method: {test.variable}")
