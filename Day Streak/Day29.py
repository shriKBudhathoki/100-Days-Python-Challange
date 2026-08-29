
print("Harry Code")
def name(a):
    
    '''
    Here is my function
    '''
    print(a**2)
name(5)

print(name.__doc__)

#whenever string literals are present just after the definations of a function module, class or method, they are associated with the object as
#the object as their doc attribute (.__doc__) for accesing the docstring

print("Another code")

# following PEP8: imports first
def add_numbers(a, b):
    """
    Adds two numbers together.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b


# following PEP8: 2 blank lines before functions
def greet_user(name):
    """
    Greets the user with their name.

    Parameters:
    name (str): The name of the user

    Returns:
    str: Greeting message
    """
    return f"Hello, {name}! 👋"


# using the functions
result = add_numbers(5, 10)
print(result)  # Output: 15

message = greet_user("Shree")
print(message)  # Output: Hello, Shree! 👋


#Simply PEP-8 Tells us how to style your code.so it's clean readable and less crusty.