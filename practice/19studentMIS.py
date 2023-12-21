# A class is a blue-print for creating objects.
# In this code implementation of OOP in Python, 
# we shall implement an object-oriented database for the UG Student MIS


# SECTION ONE
# 1. Define a class for Person
# 2. Create a person object from the Person class
# 3. Use the constructor method to define attribute for the Person class
# 4. Write a full_name method that returns the full name of the object

class Person:
    def __init__(self,firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
      
        
    def fullName(self):
        return f'{self.firstName} {self.lastName}'
    
    def studentMail(self):
        return f'{self.firstName[0].lower()}.{self.lastName.lower()}@st.ug.edu.gh'

    def initials(self):
        return f'{self.firstName[0]}.{self.lastName[0]}'    
person1= Person('Andrews', 'Kwarteng', 20)
person2 = Person('Hughes', 'Jackman', 20)

print(person1.studentMail()) # a.kwarteng@st.ug.edu.gh
print(person1.fullName()) #  Andrews Kwarteng
print(person1.initials()) # A.K

print(person2.studentMail()) # h.jackman@st.ug.edu.gh
print(person2.fullName()) # Hughes Jackson 
print(person2.initials()) # H.J


# SECTION TWO
# 1. Define a class Student which inherites from the Person class
# 2. Define extra attributes for student, such as hall of residence and courses
# 3. Create a student object from the Student class

class Student(Person):
    def __init__(self, firstName, lastName, age, residence, courses=None):
        super().__init__(firstName, lastName, age)
        self.residence = residence
        self.residence = f'{self.residence} Hall' 
        if courses == None:
            self.courses = []
        self.courses = courses
        
    def addCourse(self, course_title):
        if course_title not in self.courses:
            self.courses.append(course_title)
        
    def dropCourse(self, course_title):
        if course_title in self.courses:
            self.courses.remove(course_title)
        
    def printCourses(self):
        print(f'{self.fullName()} has registered {len(self.courses)} courses:')
        print('-'*40)
        for courses in self.courses:  
            print(courses)
        
 
student1 = Student('Devin', 'Weston', 19,'Pent', ['Discrete Math', 'DSA', 'Digital Circuit', 'Algebra'])
student2 = Student('Sam', 'Friedman', 21, 'Akuafo',['Thermodynamics', 'Biochemistry', 'African Art'])
student3 = Student('Ava', 'Jacobs', 20, 'Evandy')

        
print(student1.studentMail()) # d.weston@st.ug.edu.gh
print(student2.residence) # Akuafo Hall
print(student1.courses) # ['Discrete Math', 'DSA', 'Digital Circuit', 'Algebra']
print(student3.courses) # None
    

"""
4. Write a add_course, drop_course, print_all_courses method to mimic 
a real-world use-case of activities of adding a course, 
deleting a course and printing registered courses respectively
a student will perform on the Student MIS 

"""
student1.addCourse('Anatomy')
print(student1.courses) # ['Discrete Math', 'DSA', 'Digital Circuit', 'Algebra', 'Anatomy']

student2.dropCourse('Biochemistry')
print(student2.courses) # ['Thermodynamics', 'African Art']

student1.dropCourse('Digital Circuit')
print(student1.courses) # ['Discrete Math', 'DSA', 'Algebra', 'Anatomy']

(student1.printCourses()) 
# Devin Weston has registered 4 courses:
# ----------------------------------------
# Discrete Math
# DSA
# Algebra
# Anatomy

# Magic Methods
# Overwrite string method