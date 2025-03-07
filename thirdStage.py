class Student:
    def __init__(self, student_id, name , age):
        self.classes = {}
        self.student_id = student_id
        self.name = name
        self.age = age
        
    def enroll_in_class(self, class_id):
        if class_id not in self.classes:
            self.classes[class_id] = []
            print(f"{class_id} записан")
        else:
            print("Ты уже записан")
            
    def list_classes(self):
        list = []
        for i in self.classes:
            list.append(i)
        return list
    
    def add_grade(self, class_id, grade):
        if class_id in self.classes:
            self.classes[class_id].append(grade)
        else:
            print("Сначала запишитесь на этот урок")
            
    def get_average_grade(self):
        avg = []
        for i in self.classes:
            for v in self.classes[i]:
                avg.append(v)
        return sum(avg)/len(avg)
    
class Class:
    def __init__(self, class_id, name, instructor):
        self.students = {}
        self.class_id = class_id
        self.name = name
        self.instructor = instructor
    
    def add_student(self, student_id):
        if student_id not in self.students:
            self.students[student_id] = []
            print(f"{student_id} was added")
        else:        
            print("Already exists")
            
    def list_students(self):
        list = []
        for i in self.students:
            list.append(i)
        return list

    def add_grade(self,student_id, grade):
        if student_id in self.students:
            self.students[student_id].append(grade)
            return self.students[student_id]
        else:
            return None
        
    def get_average_grade(self):
        avg = []
        for i in self.students:
            for v in self.students[i]:
                avg.append(v)
        return sum(avg)/len(avg)
    
class SalymbekovUniversity:
    def __init__(self):
        self.students = []
        self.classes = []
    
    def add_student(self,student):
        self.students.append(student)
        
    def add_class(self, university_class):
        self.classes.append(university_class)
        
    def enroll_student(self, student_id, class_id):
        for i in self.students:
            if i.student_id == student_id:
                i.enroll_in_class(class_id)
        
        for i in self.classes:
            if i.class_id == class_id:
                i.add_student(student_id)
                
    def search_student(self, student_id):
        for i in self.students:
            if i.student_id == student_id:
                return i
            
    def search_class(self,class_id):
        for i in self.classes:
            if i.class_id == class_id:
                return i
            
    def total_student(self):
        return len(self.students)
    
    def total_classes(self):
        return len(self.classes)

    def classes_for_student(self,class_id):
        for i in self.classes:
            if i.class_id == class_id:
                return i.list_students()

    def students_in_class(self,student_id):
        for i in self.students:
            if i.student_id == student_id:
                return i.list_classes()
            
    def average_grade_for_student(self,student_id):
        for i in self.students:
            if i.student_id == student_id:
                return i.get_average_grade()
            
    def average_grade_for_class(self,class_id):
        for i in self.classes:
            if i.class_id == class_id:
                i.get_average_grade()
        
# Создание экземпляра университета
university = SalymbekovUniversity()

# Добавление студентов
student1 = Student(1, "Иван Иванов", 20)
student2 = Student(2, "Мария Смирнова", 21)
university.add_student(student1)
university.add_student(student2)

# Добавление классов
class1 = Class(101, "Математика", "Проф. Петров")
class2 = Class(102, "Физика", "Проф. Сидоров")
university.add_class(class1)
university.add_class(class2)

# Запись студента в класс
university.enroll_student(1, 101)
university.enroll_student(2, 101)
university.enroll_student(1, 102)

# Проверка списка классов студента
print(student1.list_classes())  # Ожидаемый вывод: [101, 102]

# Проверка списка студентов в классе
print(class1.list_students())  # Ожидаемый вывод: [1, 2]

# Добавление оценок студенту
student1.add_grade(101, 85)
student1.add_grade(101, 90)
student1.add_grade(102, 78)
student2.add_grade(101, 88)

# Проверка среднего балла студента
print(student1.get_average_grade())  # Ожидаемый вывод: (85+90+78) / 3 = 84.33

# Добавление оценок в класс и проверка
class1.add_grade(1, 85)
class1.add_grade(1, 90)
class1.add_grade(2, 88)

print(class1.get_average_grade())  # Ожидаемый вывод: (85+90+88) / 3 = 87.67

# Поиск студента
found_student = university.search_student(1)
print(found_student.name)  # Ожидаемый вывод: Иван Иванов

# Поиск класса
found_class = university.search_class(101)
print(found_class.name)  # Ожидаемый вывод: Математика

# Общее количество студентов и классов
print(university.total_student())  # Ожидаемый вывод: 2
print(university.total_classes())  # Ожидаемый вывод: 2