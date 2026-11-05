# Assignment Reminder Program
# This program helps a user keep track of assignment due dates.
# It compares assignment due dates to today's date and displays
# reminders for upcoming assignments, assignments due today,
# and overdue assignments.

from datetime import datetime

# Create an empty list to store assignment information
assignments = []

# Ask the user how many assignments they would like to enter
num_assignments = int(input("How many assignments would you like to enter? "))

# Loop through the number of assignments entered by the user
for i in range(num_assignments):
    # Ask the user for the assignment name
    assignment_name = input("Enter assignment name: ")

    # Ask the user for the due date (MM/DD/YYYY)
    due_date_input = input("Enter due date (MM/DD/YYYY): ")

    try:
        due_date = datetime.strptime(due_date_input, "%m/%d/%Y").date()
        assignments.append([assignment_name, due_date])
    except ValueError:
        print("Invalid date format. Please use MM/DD/YYYY.")

# Get today's date for comparison
today = datetime.today().date()

print("\nAssignment Reminders")
print("--------------------")

for assignment in assignments:
    assignment_name = assignment[0]
    due_date = assignment[1]
    days_remaining = (due_date - today).days

    if days_remaining > 7:
        print(f"{assignment_name}: Due on {due_date}")
        print("Assignment is not due soon.\n")
    elif days_remaining > 0:
        print(f"{assignment_name}: Due on {due_date}")
        print(f"Reminder: Assignment is due in {days_remaining} days.\n")
    elif days_remaining == 0:
        print(f"{assignment_name}: Due on {due_date}")
        print("Urgent Reminder: Assignment is due today!\n")
    else:
        overdue_days = abs(days_remaining)
        print(f"{assignment_name}: Due on {due_date}")
        print(f"Warning: Assignment is overdue by {overdue_days} days.\n")

print("Assignment Reminder Program Complete")
