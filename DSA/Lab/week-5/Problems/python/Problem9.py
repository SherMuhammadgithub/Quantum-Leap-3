class_students = []

def add_student(std_name):
    class_students.append(std_name)

def remove_student(std_name):
    class_students.remove(std_name)

def display_students():
    for std in class_students:
        print(std)
        
        
        
        
        
        