#!/usr/bin/env python3
"""
Find and print students with the second lowest grade directly.
Prints each name on a new line, sorted alphabetically.
"""

def find_and_print_second_lowest():
    """Read input and print students with second lowest grade directly."""
    # Read number of students
    n = int(input())
    
    # Read all students
    students = []
    for _ in range(n):
        name = input().strip()
        grade = float(input())
        students.append([name, grade])
    
    # Get unique sorted grades
    grades = sorted(set([student[1] for student in students]))
    second_lowest = grades[1]
    
    # Find and print names directly (sorted alphabetically)
    for name in sorted([student[0] for student in students if student[1] == second_lowest]):
        print(name)

if __name__ == "__main__":
    find_and_print_second_lowest()
