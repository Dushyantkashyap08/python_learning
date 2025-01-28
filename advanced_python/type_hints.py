#type hints are used to define the data type of the variable 

n : int = 5 # n is an integer

name : str = "dushyant" # name is a string

def add(a: int, b: int) -> int: # ->int is the retrun type of function
    return a + b

#advanced type hints

from typing import List, Tuple, Dict, Union

#list of integers
l : List[int] = [1,2,3]

#tuple of integers and strings
t : Tuple[int, str] = (1, "hello")

#dictionary of strings and integers
# d : Dict[str, int, bool] = {"a": 1, "b": 2, 8: True} #this will give error as 8 is not a string
d : Dict[str, Union[int, bool]] = {"a": 1, "b": 2, "c": True} #this will be true, also Dict type takes 2 args as it stores in key-value pairs 
print(d)

#union of integers and strings can hold multiple values
value: Union[int, str, bool, float] = 42  # Valid
print(value)

value = True  # Also valid
print(value)

value = "Hello"  # Still valid
print(value)


# | (pipe operator)is a shorthand for union operator
value: int | str | bool = "Hello"


# can also add complex types in union
# data: Union[int, List[str], Dict[str, float]] = {"key": 1.2}