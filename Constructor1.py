
# Topic: Constructor (__init__ method) and Instance Variables Initialization

class Employee:
    # Constructor: initializes instance variables
    def __init__(self, name, position, salary):
        self.name = name          # Instance variable
        self.position = position
        self.salary = salary     

    # Method to display employee details
    def show_details(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")


# Creating employee objects (constructor runs automatically)
emp1 = Employee("Hridoy", "System Administrator", 45000)
emp2 = Employee("Hasan", "Cybersecurity Analyst", 55000)

# Display employee info
print("=== Employee 1 ===")
emp1.show_details()

print("\n=== Employee 2 ===")
emp2.show_details()