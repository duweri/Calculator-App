print("Welcome to my  Calculator app")

operations = ["1. Add", "2. Subtract", "3. Multiply", "4. Divide"]  # instead of printing the list directly, we're going to print each operation on a new line
#by usng a for loop

for operation in operations:
 print(operation)

choice = input("Enter the number of your choice (1/2/3/4): ")

# Validate the user's choice

if choice != "1" and choice != "2" and choice != "3" and choice != "4": # This can also be written as not in ("1", "2", "3", "4"): 
 print("Invalid. Please run the program again and chose 1 to 4")
 quit()

else:
 print("Thank you for your input")

# Asking for 2 numbers

try: 
 num1 = float(input("Enter your first number: "))
 num2 = float(input("Enter your second number: "))
except: 
 print("Error: Unable to convert the input into a number")

else: 
 print("Success: Input converted to a number")

finally:
 print("Ended successfully")


# Performing calculation

if choice == "1":
 print("You have chosen Addition")

elif choice == "2":
 print("You have chosen Subtraction")

elif choice == "3":
 print("You have chosen Multiplication")

elif choice == "4":
 print("You have chosen Division")

