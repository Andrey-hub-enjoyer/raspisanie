
class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement 'update' method")

class ScheduleNotifier:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Person(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Уведомление для {self.name}: {message}")

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.grades = {}  

    def view_schedule(self, schedule):
        print(f"\nРасписание для {self.name}:")
        for day, pairs in schedule.items():
            print(f"{day}: {', '.join(pairs)}")

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def modify_schedule(self, notifier, schedule, day, new_pairs):
        if day in schedule:
            schedule[day] = new_pairs
            notifier.notify_observers(f"{self.name} обновил расписание на {day}: {', '.join(new_pairs)}")
        else:
            print("Неверный день недели.")

    def assign_grade(self, student, subject, grade):
        student.grades[subject] = grade
        print(f"{self.name} выставил {grade} по предмету {subject} для {student.name}")

class Factory:
    @staticmethod
    def create_student(name):
        return Student(name)

    @staticmethod
    def create_teacher(name, subject):
        teacher = Teacher(name)
        teacher.subject = subject
        return teacher

schedule = {
    "Понедельник": ["Математика", "Физика", "Информатика"],
    "Вторник": ["Химия", "История", "Биология"],
    "Среда": ["География", "Литература", "Английский язык"],
    "Четверг": ["Физика", "Математика", "Информатика"],
    "Пятница": ["Физкультура", "Экономика", "Обществознание"]
}


notifier = ScheduleNotifier()

teachers = [
    Factory.create_teacher("Иван Иванович", "Математика"),
    Factory.create_teacher("Петр Петрович", "Физика"),
    Factory.create_teacher("Елена Владимировна", "Информатика"),
    Factory.create_teacher("Ольга Сергеевна", "Химия"),
    Factory.create_teacher("Наталья Михайловна", "История"),
    Factory.create_teacher("Алексей Николаевич", "Биология")
]

students = [
    Factory.create_student("Анна Кузнецова"),
    Factory.create_student("Дмитрий Иванов"),
    Factory.create_student("Мария Смирнова"),
    Factory.create_student("Иван Сидоров"),
    Factory.create_student("Ольга Петрова"),
    Factory.create_student("Александр Васильев")
]

for student in students:
    notifier.add_observer(student)


for student in students:
    student.view_schedule(schedule)


teachers[0].modify_schedule(notifier, schedule, "Понедельник", ["Математика", "Физика", "Программирование"])


teachers[0].assign_grade(students[0], "Математика", 5)
teachers[1].assign_grade(students[1], "Физика", 4)
teachers[2].assign_grade(students[2], "Информатика", 5)


for student in students:
    print(f"\nОценки {student.name}: {student.grades}")



