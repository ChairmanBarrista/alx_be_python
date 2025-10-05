# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Safely divide two numbers with error handling."""
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Raised when conversion to float fails
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Raised when denominator is zero
        return "Error: Cannot divide by zero."
