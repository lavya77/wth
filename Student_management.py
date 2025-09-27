class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        self.courses_enrolled = []
        self.marks = {}

    def view_marks(self):
        print(f"\nMarks for {self.name}:")
        if not self.marks:
            print("Marks not assigned")
        for course, marks in self.marks.items():
            print(f"{course}: {marks}")

    def enroll_in_course(self, course):
        if course not in self.courses_enrolled:
            self.courses_enrolled.append(course)
            course.add_student(self)
            print(f"{self.name} enrolled in {course.course_name}")
        else:
            print(f"{self.name} already enrolled in {course.course_name}")


class Teacher(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.course_teach = []
        self.employee_id = employee_id

    def assign_marks(self, student, course, mark):
        if course in self.course_teach and student in course.enrolled_students:
            student.marks[course.course_name] = mark
            print(f"{self.name} assigned {mark} to {student.name} in {course.course_name}")
        else:
            print(f"{self.name} cannot assign marks for {course.course_name}")

    def take_attendance(self, course):
        if course in self.course_teach:
            print(f"Attendance taken by {self.name} for {course.course_name}")
        else:
            print(f"{self.name} does not teach {course.course_name}")


class Course:
    def __init__(self, course_name, credits, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
        self.enrolled_students = []
        self.assigned_teacher = None

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)

    def assign_teacher(self, teacher):
        self.assigned_teacher = teacher
        teacher.course_teach.append(self)
        print(f"{teacher.name} assigned to teach {self.course_name}")


class Admin(Person):
    def __init__(self, name):
        super().__init__(name)

    def generate_report(self, students):
        print("\n--- Students Report ---")
        for student in students:
            print(f"Name: {student.name}, Roll No: {student.roll_no}")
            for course in student.courses_enrolled:
                mark = student.marks.get(course.course_name, "N/A")
                print(f"  {course.course_name}: {mark}")


python_course = Course("Python Programming", 4, "CS101")
math_course = Course("Mathematics", 3, "MA101")

priya = Teacher("Priya", 101)
python_course.assign_teacher(priya)

ravi = Student("Ravi", 1)
anita = Student("Anita", 2)

ravi.enroll_in_course(python_course)
anita.enroll_in_course(python_course)
ravi.enroll_in_course(math_course)

priya.assign_marks(ravi, python_course, 95)
priya.assign_marks(anita, python_course, 88)

ravi.view_marks()
anita.view_marks()

priya.take_attendance(python_course)

admin = Admin("College Admin")
admin.generate_report([ravi, anita])
