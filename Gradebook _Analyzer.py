"""
-------------------------------------------------------------
Project Title : GradeBook Analyzer
Course        : Programming for Problem Solving using Python
Student Name  : Rohan Vashisth
Date          : 4 November 2025
Description   : Reads student marks from a CSV file, analyzes
                data, assigns grades, and displays results.
-------------------------------------------------------------
"""

import csv
import statistics


print("=" * 60)
print(" Welcome to GradeBook Analyzer (CSV Version) - by Rohan Vashisth ")
print("=" * 60)


def read_marks_from_csv(filename):
    marks = {}
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                marks[row['Name']] = int(row['Marks'])
        return marks
    except FileNotFoundError:
        print("⚠️ CSV file not found! Please make sure 'students.csv' is in the same folder.")
        return {}

marks = read_marks_from_csv("students.csv")

if not marks:
    exit()


def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())


def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def separate_pass_fail(marks_dict):
    passed = [n for n, m in marks_dict.items() if m >= 40]
    failed = [n for n, m in marks_dict.items() if m < 40]
    return passed, failed


def display_results(marks_dict, grades_dict):
    print("\n📊 Student Grade Report")
    print("-" * 40)
    print(f"{'Name':<12}{'Marks':<10}{'Grade':<5}")
    print("-" * 40)
    for name in marks_dict:
        print(f"{name:<12}{marks_dict[name]:<10}{grades_dict[name]:<5}")
    print("-" * 40)


def display_grade_distribution(grades_dict):
    print("\n🎯 Grade Distribution")
    print("-" * 40)
    grade_count = {}
    for grade in grades_dict.values():
        grade_count[grade] = grade_count.get(grade, 0) + 1
    for grade, count in grade_count.items():
        print(f"Grade {grade}: {count} student(s)")
    print("-" * 40)


def display_statistics(marks_dict):
    print("\n📈 GradeBook Statistics")
    print("-" * 40)
    print(f"Average Marks : {calculate_average(marks_dict):.2f}")
    print(f"Median Marks  : {calculate_median(marks_dict):.2f}")
    print(f"Highest Marks : {find_max_score(marks_dict)}")
    print(f"Lowest Marks  : {find_min_score(marks_dict)}")
    print("-" * 40)

def main_menu():
    grades = assign_grades(marks)
    while True:
        print("\n🔸 Main Menu:")
        print("1. View Student Grades")
        print("2. View Statistics")
        print("3. View Grade Distribution")
        print("4. View Pass/Fail Summary")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_results(marks, grades)
        elif choice == "2":
            display_statistics(marks)
        elif choice == "3":
            display_grade_distribution(grades)
        elif choice == "4":
            passed, failed = separate_pass_fail(marks)
            print(f"\n✅ Passed: {passed} ({len(passed)})")
            print(f"❌ Failed: {failed} ({len(failed)})")
        elif choice == "5":
            print("\n👋 Exiting GradeBook Analyzer. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Try again!")

main_menu()
