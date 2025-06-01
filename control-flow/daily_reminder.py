#!/usr/bin/env python3
# Daily reminder script for a single task based on priority and time sensitivity

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Base reminder message
reminder = f"'{task}' is a {priority} priority task"

# Use Match Case to handle priority levels
match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += ". Plan to address it soon"
    case "low":
        reminder += ". Consider completing it when you have free time"
    case _:
        reminder = f"'{task}' has an invalid priority. Please use high, medium, or low."

# Modify reminder if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " today!"

# Print the final reminder
if priority in ["high", "medium", "low"]:
    print(f"\nReminder: {reminder}")
else:
    print(f"\n{reminder}")
