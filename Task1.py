'''
Problem 1 : "Daily Steps Tracker"
Description:
You have a list of the number of steps taken each day in a month. 
Your task is to write a program that performs the following:
Accepts the number of steps taken each day in the month as numbers separated by spaces.
Calculates the highest and lowest step counts.
Calculates the average daily step count.
Sorts the step counts in descending order.

'''


steps = input("Enter daily steps separated by spaces: ")

steps_list = list(map(int, steps.split()))

highest_steps = max(steps_list)
lowest_steps = min(steps_list)
average_steps = sum(steps_list) / len(steps_list)
sorted_steps = sorted(steps_list, reverse=True)

print("Highest Steps:", highest_steps)
print("Lowest Steps:", lowest_steps)
print("Average Steps:", round(average_steps, 2))
print("Sorted Steps (Descending):", sorted_steps)
