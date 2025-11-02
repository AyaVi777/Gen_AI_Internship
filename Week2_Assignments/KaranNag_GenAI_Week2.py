#Task 1:Python Basics&Operators

#1.1: Create a Python script that accepts two numbers from the user
n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))

#1.2:Perform all basic arithmetic operations (add, subtract, multiply, divide, modulus, power)
add=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2
mod=n1%n2
power=n1**n2

#1.3:Demonstrate use of comparison and logical operators (>, <, ==, !=, and, or, not).
greater = n1 > n2
less = n1 < n2
equal = n1 == n2
not_equal = n1 != n2

and_op = (n1 > 0) and (n2 > 0)
or_op = (n1 > 0) or (n2 > 0)
not_op = not (n1 > n2)

# 1.4:Print results clearly using formatted output (f-strings)
print("\nFormatted Summary (Using f-strings)")
print(f"Numbers entered: {n1} and {n2}")

print("\n___ Arithmetic Operations ___")
print(f"Sum: {add}")
print(f"Difference: {sub}")
print(f"Product: {mul}")
print(f"Division: {div:.2f}")
print(f"Modulus: {mod}")
print(f"Power: {power}")

print("\n___ Comparison Operators ___")
print(f"{n1} > {n2}  = {greater}")
print(f"{n1} < {n2}  = {less}")
print(f"{n1} == {n2} = {equal}")
print(f"{n1} != {n2} = {not_equal}")

print("\n___ Logical Operators ___")
print(f"({n1} > 0) and ({n2} > 0) = {and_op}")
print(f"({n1} > 0) or ({n2} > 0)  = {or_op}")
print(f"not ({n1} > {n2}) = {not_op}")

import pandas as pd
import numpy as np
import random

# Task 2: Lists and Arrays

# 2.1:Create a list of 10 random integers (between 1 and 100)
randomizer = [random.randint(1, 100) for _ in range(10)]
print("Original list:", randomizer)

# 2.2:Perform list operations

# Add an element
randomizer.append(7)
print("\nAfter adding 7:", randomizer)

# Remove an element (example: remove first element)
removed_value = randomizer.pop(0)
print(f"After removing first element ({removed_value}):", randomizer)

# Find maximum and minimum values
max_value = max(randomizer)
min_value = min(randomizer)
print(f"\nMaximum value: {max_value}")
print(f"Minimum value: {min_value}")

# Sort the list
randomizer.sort()
print("\nSorted list:", randomizer)

# 2.3:Convert the list into a NumPy array
arr = np.array(randomizer)
print("\nNumPy Array:", arr)

# Calculate Mean, Median, and Standard Deviation
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print(f"\nMean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")

# Task 3: Dictionaries and Sets

# 3.1:Create a dictionary named student with keys: name, course, marks
student = {
    "Name": "Karan Nag",
    "Course": "Artificial Intelligence",
    "Marks": 75
}

# 3.2:Add a new key 'grade' based on marks
if student["Marks"] >= 90:
    student["Grade"] = "A"
elif student["Marks"] >= 75:
    student["Grade"] = "B"
elif student["Marks"] >= 60:
    student["Grade"] = "C"
else:
    student["Grade"] = "D"

# 3.3:Print all keys and values using a loop
print("--- Student Details ---")
for key, value in student.items():
    print(f"{key}: {value}")

# 3.4:Create two sets of AI tools
set1 = {"Bard", "Claude", "Copilot", "Gumloop", "Zapier"}
set2 = {"Gemini", "Copilot", "Perplexity", "Algolia", "Influencity"}

# Display both sets
print("\nSet 1 (AI Tools):", set1)
print("Set 2 (AI Tools):", set2)

# Perform common set operations
print("\n___ Set Operations ___")
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (Set1 - Set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Task 4: File Handling

# 4.1:Create a text file named ai_students.txt and write details of 5 students
students = [
    {"name": "Karan", "marks": 95, "grade": "A"},
    {"name": "Valentino", "marks": 77, "grade": "B"},
    {"name": "Rocca", "marks": 98, "grade": "A"},
    {"name": "Giorgio", "marks": 62, "grade": "C"},
    {"name": "Lisa", "marks": 75, "grade": "B"}
]

# Write student details into the file
with open("ai_students.txt", "w") as file:
    for s in students:
        file.write(f"{s['name']}, {s['marks']}, {s['grade']}\n")

print("Data written successfully!")

# 4.2:Read the file and display students who scored above 75 marks
print("\n___Students with Marks > 75___")
with open("ai_students.txt", "r") as file:
    for line in file:
        name, marks, grade = line.strip().split(", ")
        marks = int(marks)
        if marks > 75:
            print(f"Name: {name}, Marks: {marks}, Grade: {grade}")

# Task 5: Real-World Mini Project
# File: ai_prompt_logger.py

from datetime import datetime

# 5.1:Accept user input (simulating an AI prompt)
prompt = input("Enter your AI prompt: ")

# 5.2:Each time you run the program, new prompts are appended with timestamps
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"[{timestamp}] {prompt}\n"

# 5.3:Append the prompt to 'prompt_history.txt'
with open("prompt_history.txt", "a") as file:
    file.write(log_entry)

print("\nPrompt saved successfully in 'prompt_history.txt'!")
