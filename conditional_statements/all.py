#all caluse retruns True when all the conditions are true

# Example 1: Checking if all numbers are positive
numbers = [1, 2, 3, 4, 5]
all_positive = all(num > 0 for num in numbers)
print("All positive:", all_positive)  # True

numbers = [1, -2, 3, 4, 5]
all_positive = all(num > 0 for num in numbers)
print("All positive:", all_positive)  # False (because -2 is negative)

# Example 2: Checking if all strings have minimum length
passwords = ["secure123", "password123", "hi"]
all_valid = all(len(password) >= 8 for password in passwords)
print("All passwords valid length:", all_valid)  # False (because "hi" is too short)

# Example 3: Verifying student grades (all passing)
grades = [75, 80, 90, 65]
all_passing = all(grade >= 60 for grade in grades)
print("All students passed:", all_passing)  # True

# Example 4: Checking if all items in a list are of the same type
list1 = [1, 2, 3, 4, 5]
all_integers = all(isinstance(x, int) for x in list1)
print("All integers:", all_integers)  # True

list2 = [1, "hello", 3, 4, 5]
all_integers = all(isinstance(x, int) for x in list2)
print("All integers:", all_integers)  # False (because "hello" is a string)

# Example 5: Combining all() and any() for complex validation
def validate_password(password):
    criteria = [
        any(c.isupper() for c in password),  # Has uppercase
        any(c.islower() for c in password),  # Has lowercase
        any(c.isdigit() for c in password),  # Has number
        len(password) >= 8                   # Is long enough
    ]
    return all(criteria)  # All criteria must be met

print("Is 'Password123' valid?:", validate_password("Password123"))  # True
print("Is 'password' valid?:", validate_password("password"))       # False