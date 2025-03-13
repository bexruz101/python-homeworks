# Decorator function to check for division by zero
def check(func):
    def wrapper(a, b):  # Wrapper function that takes two arguments
        if b == 0:  # Check if the denominator is zero
            raise Exception("Denominator can't be zero")  # Raise an exception if denominator is zero
        return func(a, b)  # Call the original function if denominator is valid
    return wrapper  # Return the wrapper function

# Applying the @check decorator to the div function
@check
def div(a, b):
    print(a // b)  # Perform integer division and print the result

# Main program execution with exception handling
try:
    x, y = map(int, input().split())  # Take two space-separated integer inputs from the user
    div(x, y)  # Call the decorated function
except Exception as e:  # Catch any exceptions that occur
    print(e)  # Print the exception message
