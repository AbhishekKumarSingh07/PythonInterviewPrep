class Test:
    def __init__(self, marks) -> None:
        self.marks: int = marks
    
    def __repr__(self) -> str:
        return f"Test({self.marks})"
    
    def __mul__(self, multiplied_by) -> None:
        
        if type(multiplied_by) is not int:
            raise Exception("Invalid Args, Must be Int")
        self.marks: int = self.marks * 10
        


test : Test = Test(7)

print(test)
test * 8
print(test)