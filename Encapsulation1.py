
# Topic: Encapsulation using Public, Protected, and Private Variables in Python

class Employee:
    # Constructor to initialize all types of variables
    def __init__(self, name, position, salary):
        self.name = name            # Public variable
        self._position = position   # Protected variable (single underscore)
        self.__salary = salary      # Private variable (double underscore)

    # Instance method to display employee details
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self._position}")
        print(f"Salary: ${self.__salary}")

    # Method to modify private variable safely inside the class
    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"{self.name}'s salary increased by ${amount}")
        else:
            print("❌ Invalid amount! Must be positive.")

    # Internal method to access private variable
    def _show_private_data(self):
        print(f"Accessing Private Salary inside class: ${self.__salary}")


# Creating object
emp1 = Employee("Hridoy", "System Admin", 40000)

print("=== Employee Information ===")
emp1.show_info()

# Accessing Public variable (Allowed)
print("\nPublic Access:")
print("Employee Name:", emp1.name)

# Accessing Protected variable (Allowed but Not Recommended)
print("\nProtected Access (Not Recommended):")
print("Employee Position:", emp1._position)

# Accessing Private variable directly (❌ Not Allowed)
print("\nPrivate Access:")
try:
    print(emp1.__salary)
except AttributeError:
    print("Cannot access private variable directly!")

# Accessing Private variable using name mangling
print("\nAccess Private Variable (Using Name Mangling):")
print("Employee Salary:", emp1._Employee__salary)

# Increase salary using method
print("\n--- Updating Salary ---")
emp1.increase_salary(5000)

# Accessing private data inside class
print("\n--- Accessing Private Data Safely ---")
emp1._show_private_data()