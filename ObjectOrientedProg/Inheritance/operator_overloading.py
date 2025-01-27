#Operator overloading in Python allows you to define custom behavior for operators (like +, -, *, etc.) using special methods called dunder (double underscore) or magic methods. These methods are predefined in Python and are invoked automatically when the corresponding operator is used.

class Point:
    def __init__(self, x):
        self.x = x

    # Overload the + operator using __add__
    def __add__(self, other):
        return Point(self.x + other.x)

    # For better representation when printing the object
    def __repr__(self):
        return f"Point({self.x})"

# Usage
p1 = Point(1)
p2 = Point(3)
p3 = p1 + p2  # Calls __add__ method
print(p3)  # Output: Point(4, 6)



#we need to return Point in __add__ method becoz the + operator is expected to return a new object that represents the result of the addition, rather than modifying the existing objects.


# Arithmetic Operators:

# __add__(self, other) → For +
# __sub__(self, other) → For -
# __mul__(self, other) → For *
# __truediv__(self, other) → For /
# __floordiv__(self, other) → For //
# __mod__(self, other) → For %
# __pow__(self, other) → For **
# Comparison Operators:

# __eq__(self, other) → For ==
# __ne__(self, other) → For !=
# __lt__(self, other) → For <
# __le__(self, other) → For <=
# __gt__(self, other) → For >
# __ge__(self, other) → For >=
# Unary Operators:

# __neg__(self) → For unary - (e.g., -x)
# __pos__(self) → For unary + (e.g., +x)
# __abs__(self) → For abs()
# Assignment Operators:

# __iadd__(self, other) → For +=
# __isub__(self, other) → For -=
# __imul__(self, other) → For *=
# __itruediv__(self, other) → For /=
# Bitwise Operators:

# __and__(self, other) → For &
# __or__(self, other) → For |
# __xor__(self, other) → For ^
# __lshift__(self, other) → For <<
# __rshift__(self, other) → For >>