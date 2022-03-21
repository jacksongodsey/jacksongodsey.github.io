#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Hello World")
homework_completed = int(
    input("How many homework assignments have" " you completed so far: "))
tests_completed = int(input("How many test assignments have you completed: "))
labs_completed = int(input("How many labs have you completed: "))

homework_value = int(input("Enter how much your homework is worth: "))
tests_value = int(input("Enter how much your tests are worth: "))
labs_value = int(input("Enter how much your labs are worth: "))

total_points = int(input("How many points were possible in your course: "))

homework_grade = homework_completed * homework_value
homework_grade2 = homework_grade / 100
tests_grade = tests_completed * tests_value
tests_grade2 = tests_grade / 100
labs_grade = labs_completed * labs_value
labs_grade2 = labs_grade / 100

final_grade_on_assignments = homework_grade2 * tests_grade2 * labs_grade2

final_overall_grade = ((final_grade_on_assignments / total_points) * 100)

print(final_overall_grade)
