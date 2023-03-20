# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet(x = "Bob"):
#     print(f"first lane {x}")
#     print("second lane")
#     print(f"third lane {x}") 

# greet()

# another variation that allows for input

# def greet(x):
#     print(f"first lane {x}")
#     print("second lane")
#     print(f"third lane {x}") 

# greet("Bob")

#Function with more than on input

# def greet(x, y, z):
#     print(f"first lane {x}")
#     print(f"second lane {y}")
#     print(f"third lane {z}")

# greet("Bob", "Henry", "Steve")

x = input("Tell me your name: ")
y = input("Tell me where you live: ")

def greet():
    print(f"Welcome {x} from {y}")

greet()