class Person:
    def __init__(self,  last_name, first_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self) -> str:
        return f' {self.last_name} {self.first_name}, {self.age} years old'


class Student(Person):
    def __init__(self,  last_name, first_name, age, group) -> None:
        super().__init__(last_name, first_name, age)
        self.group = group

    def __str__(self) -> str:
        return f'{super().__str__()} from {self.group} group'

class Worker(Person):
    def __init__(self, last_name, first_name, age, job) -> None:
        super().__init__(last_name, first_name, age)
        self.job = job

    def __str__(self) -> str:
        return f'{super().__str__()}, my job is {self.job}'


if __name__ == '__main__':
    person = Person('Vershinin', 'Andry', 19)
    student = Student('Igor', 'Valentinovych', 19, 'KA-03')
    worker = Worker('Evgen', 'Evgenych', 36, 'Frilans')

    print(f"Hi, I'm {person}.")
    print(f"Hi, I'm {student}.")
    print(f"Hi, I'm {worker}.")