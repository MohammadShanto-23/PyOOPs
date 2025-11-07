
# Topic: Simple Class and Object (without constructor)

class Student:
    # Simple method to display student info
    def display_info(self, name, roll):
        print(f"Name: {name}")
        print(f"Roll: {roll}")


# Creating object of the class
student1 = Student()
student2 = Student()

# Calling method using objects
student1.display_info("Hridoy", 101)
student2.display_info("Hasan", 102)