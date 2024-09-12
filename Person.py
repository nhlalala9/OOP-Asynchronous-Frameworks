class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm {self.age} years old and my gender is {self.gender}.")

# Creating  an instance of the Person class
person_instance = Person(name="Alice", age=30, gender="Female")

# Calling the introduce method
person_instance.introduce()
