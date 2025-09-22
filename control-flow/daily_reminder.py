# Prompt for user input
task = input("Please enter your task for today: ")
time_bound = input("Is this task time-bound? (yes/no): ").lower()
priority = input("What is the priority of this task? (high/medium/low): ").lower()


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
print(reminder)
