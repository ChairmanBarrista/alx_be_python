def perform_operation(num1, num2, operation):

    match operation.lower():
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Division by zero!"
            return num1 / num2
        case _:
            raise ValueError("Invalid operation! Use 'add', 'subtract', 'multiply', or 'divide'.")
