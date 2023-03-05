# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(x = "angela"):
    print(f"first lane {x}")
    print("second lane")
    print(f"third lane {x}") 

greet()

# another variation

def greet(x):
    print(f"first lane {x}")
    print("second lane")
    print(f"third lane {x}") 

greet("angela")