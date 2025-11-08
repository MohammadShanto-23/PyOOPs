
class Student:
    # Method using 'self' to access instance variables
    def set_info(self, name, roll):
        # 'self' represents the current object
        self.name = name
        self.roll = roll

    def display_info(self):
        # Accessing variables using 'self'
        print(f"Student Name: {self.name}")
        print(f"Student Roll: {self.roll}")

student1 = Student()
student2 = Student()

student1.set_info("Hridoy", 101)
student2.set_info("Hasan", 102)

# Displaying information
print("=== Student 1 Info ===")
student1.display_info()

print("\n=== Student 2 Info ===")
student2.display_info()