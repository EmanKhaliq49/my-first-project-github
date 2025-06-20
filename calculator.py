# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function for power (x to the power of y)
def power(x, y):
    return x ** y # ** is the exponentiation operator in Python


print("Welcome to the Simple Python Calculator!")
print("---------------------------------------")
print("Press q or Q to exit")
print("Please select an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Power (^)")
# NEW LINE
print("---------------------------------------")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4) or 'q' to quit: ")
    if choice.lower() == 'q': # New check for quitting
      break 
    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'): # This condition remains the same for this branch
      try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
      except ValueError:
         print("Invalid input. Please enter numbers only.")
         continue

    if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(num1, "/", num2, "=", result)
    elif choice == '4':
           result = divide(num1, num2)
           if result == "Error! Division by zero.":
                print(result)
           else:
                print(num1, "/", num2, "=", result)

    elif choice == '5': # NEW BLOCK
            print(num1, "^", num2, "=", power(num1, num2))

        # Ask if the user wants another calculation
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation.lower() == "no":
            break
    else: # This is the else block for invalid choice
       print("Invalid Input. Please enter a valid choice (1/2/3/4) or 'q'.")

print("\nThank you for using the calculator!")
print("Exiting program.")
print("---------------------------------------") # Add this line for emphasis
print("Calculator program ended.")