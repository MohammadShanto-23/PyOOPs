
# Topic: Instance Variables, Class Variables, and Their Differences

class Student:
    # Class Variable (shared by all objects)
    school_name = "Green Valley High School"

    # Constructor to initialize instance variables
    def __init__(self, name, roll):
        self.name = name      # Instance Variable (unique for each object)
        self.roll = roll      # Instance Variable

    # Instance Method to display student details
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"School: {Student.school_name}")


# Creating objects (each has different instance variable values)
student1 = Student("Hridoy", 101)
student2 = Student("Hasan", 102)

# Display student details
print("=== Student 1 Info ===")
student1.show_info()

print("\n=== Student 2 Info ===")
student2.show_info()

# Changing class variable (affects all objects)
print("\n--- Changing Class Variable ---")
Student.school_name = "Blue Sky International School"

# Display updated info
print("\n=== After Changing Class Variable ===")
student1.show_info()
student2.show_info()