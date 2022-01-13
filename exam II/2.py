class Human:
    def __init__(self, fname, bdate, pol, faculty):
        self.name = fname
        self.born_date = bdate
        self.pol = pol
        self.faculty = faculty
        self.__taxpayerIN = 123456

    def job(self):
        print(f"Я на факультете {self.faculty}")

class Student(Human):
    def __init__(self, fname, bdate, pol, faculty, group, number_student, scholarship):
        super().__init__(fname, bdate, pol, faculty)
        self.group = group
        self.number_student = number_student
        self.__scholarship = scholarship
    
    def job(self):
        print(f"Я учусь на факультете {self.faculty}")


class Teacher(Human):
    def __init__(self, fname, bdate, pol, faculty, salary, hours_work, academic_title):
        super().__init__(fname, bdate, pol, faculty)
        self.__salary = salary
        self.hours_work = hours_work
        self.academic_title = academic_title
    
    def job(self):
        print(f"Я работаю на факультете {self.faculty}")

x = Student("Mike", "12.12.1999", "male", "Science", "Math", "1212.2017", 4000)
x.job()
