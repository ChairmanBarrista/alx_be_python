from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a formatted way."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # returning in case we want to reuse it


def calculate_future_date(days_to_add: int):
    """Calculate and display the future date after adding days_to_add days."""
    future_date = datetime.now() + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date


def main():
    # Part 1: Show current date and time
    display_current_datetime()

    # Part 2: Ask user for days and calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for days.")


if __name__ == "__main__":
    main()
