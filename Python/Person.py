class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")


# person1 = Person("Alice", 30)
# person1.greet()
# person1.birthday()
# person1.greet()

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

    def greet(self):
        print(
            f"Hello, my name is {self.name}, I am {self.age} years old and my student ID is {self.student_id}.")


student1 = Student("Bob", 30, "S12345")
student1.greet()
student1.study()
