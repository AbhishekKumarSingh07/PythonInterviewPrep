class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        return type(class_name, bases, attrs)
    

class Animal(metaclass=Meta):
    number_1: int = 5
    str_1: str = "Test Animal Class"
    
    def hello(self):
        print("Hi Akki")
        
