#functions with arguments

def goodDay(name): #here name is a parameter which will be provided while function calling
    print(f"Good Evening !,{name}")
    
a = goodDay("jatin") #parameter during function call is called argument , (here, jatin is the argument)
print(a) #this will give None as goodDay is nor returning anything, but just printing a formatted string


# a function can also return something 
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    if not isinstance(a, int) or not isinstance(b, int): #enforcing type checking
        raise TypeError(f"Both arguments must be integers.")
    return a + b

# Function call example
sum_of_numbers = add_numbers(3, 3)
print(f"The sum is: {sum_of_numbers}")  # Output: The sum is: 8, here becoz the function is returning some value so it gives the same as output
