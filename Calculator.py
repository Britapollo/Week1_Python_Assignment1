#Basic  Calculator Program

#Step 1: Collect user input
num1_input = input ("Enter the first number:")
num2_input = input ("Enter the second number:")
operation = input ("Choose operation (+, -, *, /): ")

#Step 2: Convert inputs to float
num1 = float(num1_input)
num2 = float(num2_input)

#step 3: Perform calculation based on operation
if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} = {result}")
elif operation == "-":
    result = num1-num2
    print(f"The result of {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} ")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The results of {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
        print("Invalid operation! Please choose +, -, *, or /.")

#Step 4: Display variable data types for learning purposes
print("\n--- Varibale Data Types ---")
print(f"num1: {type(num1)}")
print(f"num2: {type(num2)}")
print(f"operation: {type(operation)}")        

