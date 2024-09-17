class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"the person {self.name} is {self.age} years old"
    def walk(self):
        print(f"{self.name} can walk")

obj1 = person("John", 25)
obj2 = person("Dave", 21)
obj3 = person("Jimmy", 31)

obj1.walk()
obj2.walk()
obj3.walk()

