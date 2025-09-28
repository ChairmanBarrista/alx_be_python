def perform_operation(num1, num2, operation):

    operation = operation.lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "DIVIDE_BY_ZERO"  # Special message your main.py can detect
        return num1 / num2
    else:
        return "INVALID_OPERATION. Use 'add', 'subtract', 'multiply', or 'divide'."
    
