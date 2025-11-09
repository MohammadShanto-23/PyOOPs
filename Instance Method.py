
# Topic: Instance Methods in Python OOP

class Car:
    # Constructor to initialize instance variables
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Instance method to display car information
    def show_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    # Instance method to update car year
    def update_year(self, new_year):
        self.year = new_year
        print(f"{self.brand} {self.model} year updated to {self.year}")


# Creating car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)

print("=== Car 1 Info ===")
car1.show_info()

print("\n=== Car 2 Info ===")
car2.show_info()

# Update year using instance method
print("\n--- Updating Year ---")
car1.update_year(2025)

# Display updated info
print("\n=== Updated Car 1 Info ===")
car1.show_info()