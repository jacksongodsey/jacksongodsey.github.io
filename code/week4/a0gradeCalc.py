#########################################
# Jackson Godsey
# Assignment a0
# 02/03/2022
#
# Description: This program asks the user for their scores in class A101 and calculates their final grade
# Inputs: Eight floats representing a myriad
# of different scores in their class
# Outputs: Outputs their final grade in
# the class as a percentage after calculating their final score with
# appropriate weights as seen in the syllabus
#
# 1. I am using MacOS Monterey version 12.2
# 2. I am using python 3.9.10
# 3. I am using distribution of Emacs called Doom Emacs.
# Doom version is 21.12.0-alpha and the Emacs version is 27.2
# 4. Nothing so far things have been steady. If anything making casual spelling
# mistakes and having zybooks give me errors cause of that is quite
# annoying
#########################################

# instructions
print('INTRUCTIONS')
print('For each of the following grades, enter your score out of 100')
print()
# Asking for inputs for scores
class_engagement_score = float(input('class engagement score: '))
zybook_part_score = float(input('zyBook Participation Activities score: '))
zybook_challenge_score = float(input('zyBook Challenge Activities score: '))
zylab_score = float(input('zyLab programming assignments score: '))
blackboard_assignment_score = float(input('Blackboard programming assignments score: '))
midterm1 = float(input('midterm #1 score: '))
midterm2 = float(input('midterm #2 score: '))
final_exam = float(input('final exam score: '))
print()
# final grade calculations

final_grade = ((class_engagement_score * 0.05) + (zybook_part_score * 0.05) +
(zybook_challenge_score * 0.05)+
(zylab_score * 0.4) + (blackboard_assignment_score * 0.15) +
(midterm1 * 0.1) + (midterm2 * 0.1) + (final_exam * 0.1) / 1)
print()
#print the final grade
print(f'Your final grade for CSCE A101 is {final_grade:.2f}%')
