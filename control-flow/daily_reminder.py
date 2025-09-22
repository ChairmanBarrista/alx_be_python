# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


# Process and provide reminder using Match Case and if statement
match priority:
    case "high":
        reminder = f"Your task '{task}' is a high priority"
    case "medium":
        reminder = f"Your task '{task}' is a medium priority"
    case "low":
        reminder = f"Your task '{task}' is a low priority"
    case _:
        reminder = f"Your task '{task}' has an unrecognized priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print("Reminder:" reminder)
