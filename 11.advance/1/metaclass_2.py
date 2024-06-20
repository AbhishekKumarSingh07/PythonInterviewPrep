"""
Another way to define a class although it is not suggested.
"""

Test = type('Test', (), {})
test : Test = Test()

print(f"Type of object test: {type(test)}")
print(f"Class of object test: {test.__class__}")
print(f"Class of class of object (Class of Test Class): {test.__class__.__class__} ") 