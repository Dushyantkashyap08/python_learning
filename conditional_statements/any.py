#any clause
#any() is used when you want to check if at least one element in an iterable (like a list, string, or generator expression) is True. It returns True if any element in the iterable is True, and False if all elements are False or if the iterable is empty.

# Example 1: Checking if any number is greater than 5
numbers = [1, 2, 3, 4, 5, 6]
result = any(num > 5 for num in numbers)
print(result)  # True (because 6 > 5)

# Example 2: Checking if any string contains 'a'
words = ['hello', 'world', 'apple']
has_a = any('a' in word for word in words)
print(has_a)  # True (because 'apple' contains 'a')

# Example 3: Checking for special characters in a password
password = "hello123!"
special_chars = ['!', '@', '#', '$']
has_special = any(char in password for char in special_chars)
print(has_special)  # True (because '!' is in the password)

# Example 4: When nothing matches
numbers = [1, 2, 3, 4]
result = any(num > 10 for num in numbers)
print(result)  # False (no number is greater than 10)


#aggregate functions
print(max(numbers))
print(min(numbers))

def avg(numbers):
    return sum(numbers) / len(numbers)

print(avg(numbers))