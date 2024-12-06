# Function   len(),print(),sum()
def square(number):
    return number ** 2

# Method list.append(),list.remove()
class MathOperations:
    def square(self, number):
        return number ** 2

# Calling the function
print(square(4))  # Output: 16

# Calling the method
math_ops = MathOperations()
print(math_ops.square(4))  # Output: 16


"""Summary

Functions are standalone and independent.

Methods are functions tied to classes and instances.
"""