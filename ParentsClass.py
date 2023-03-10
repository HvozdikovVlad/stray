class Grandparents:
    def __init__(self, age, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.age = age

class Parents:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = "4k"
class Child:
    def print_info(self):
        print(self.age)
        print(self.resolution)
smartchild = Child(age ="age")
smartchild.print_info()