"""
Author: John Kuronya
Date: 6-23-25
File Name: Kuronya_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand using
lists, loops, and conditionals.
"""

# List of tasks for running a lemonade stand
tasks = [
    "Buy lemons and sugar",
    "Clean and set up the stand",
    "Make lemonade",
    "Advertise in the neighborhood",
    "Count profits and restock supplies"
]

# Print each task using a for loop
print("Lemonade Stand Weekly Tasks:")
for task in tasks:
    print("- " + task)

print("\nWeekly Schedule:")

# List of days in the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# for loop and if-else to assign tasks or rest days
for index, day in enumerate(days):
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off – Time to rest and relax.")
    else:
        # Use modulo to loop through tasks if there are fewer tasks than weekdays
        task = tasks[index % len(tasks)]
        print(f"{day}: Task – {task}")
