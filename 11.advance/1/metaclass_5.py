class Meta(type):
    def __new__(self, class_name, bases, attrs):
        new_attrs: dict = {}
        for key, val in attrs.items():
            if key.startswith("__"):
                new_attrs[key] = val
            else:
                new_attrs[key.upper()] = val
        return type(class_name, bases, new_attrs)
    

class Animal(metaclass=Meta):
    number_1: int = 5
    str_1: str = "Test Animal Class"
    
    def hello(self):
        print("Hi Akki")
        

animal: Animal = Animal()

# Below print and method call will throw errors

# print(animal.number_1)
# print(animal.str_1)
# animal.hello()


# This is how they should be called

print(animal.NUMBER_1)
print(animal.STR_1)
animal.HELLO()