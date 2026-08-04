# CS344 Final Project - Milestone 3 Test Plan
# Project Title: Study Session Planner / Focus Tracker
# Student: Kaiden Blanchard
# Repository: https://github.com/kaibla365/Project-for-Python

# Overview and Scope
# This milestone tests the current implementation of the
# Study Session Planner and Focus Tracker.
#
# Features being tested:
# - User input
# - Study session processing
# - Goal comparison (planned vs. actual study time)
# - Summary calculations
# - Average focus rating
# - Loop for multiple study sessions
# - Program exit
#
#  Features NOT yet implemented:
# - Save study sessions
# - Load previous study sessions
# - Edit study sessions
# - Delete study sessions
# - Study history

# Test Case 1
# Description: One study session where actual time is greater than planned.
# Input:
# Subject: Math
# Planned Time: 60
# Actual Time: 75
# Focus Rating: 9

# Expected Result:
# "Great job!" message appears.
# Total sessions = 1
# Total minutes = 75
# Average focus = 9.0
# Actual Result:
# Program displayed correct message and summary.
# Status: PASS

# Test Case 2
# Description: Actual study time equals planned study time.
# Input:
# Science
# 45
# 45
# 8

# Expected Result:
# Great job message.
# Actual Result:
# Correct message displayed.
# Status: PASS

# Test Case 3
# Description:Actual study time is less than planned.
# Input:
# History
# 60
# 40
# 7

# Expected Result:
# Encouragement message displayed.
# Actual Result:
# Program displayed the correct encouragement.
# Status: PASS

# Test Case 4
# Description:
# Enter three different study sessions.
# Input:
# Three study sessions
# Expected Result:
# Totals and averages update after each session.
# Actual Result:
# Summary updated correctly.
# Status: PASS

# Test Case 5
# Description: Highest possible focus rating.
# Input:
# English
# 30
# 30
# 10

# Expected Result:
# Average focus = 10.0
# Actual Result:
# Average displayed correctly.
# Status: PASS

# Test Case 6
# Description: Lowest possible focus rating.
# Input:
# Biology
# 20
# 20
# 1

# Expected Result:
# Average updates correctly.
# Actual Result:
# Program calculated correctly.
# Status: PASS

# Test Case 7
# Description:
# Continue entering study sessions.
# Input: y

# Expected Result:
# Program asks for another study session.
# Actual Result:
# Program continued correctly.
# Status: PASS

# Test Case 8
# Description:
# Quit the program.

# Input: n
# Expected Result:
# Program exits and displays thank-you message.
# Actual Result:
# Program exited correctly.
# Status: PASS

# Test Case 9
# Description:
# Multiple focus ratings.

# Input:
# Focus ratings:
# 6
# 8
# 10

# Expected Result:
# Average focus calculated correctly.
# Actual Result:
# Correct average displayed.
# Status: PASS

# Test Case 10
# Description:
# Total study time calculation.

# Input:
# 20
# 40
# 60

# Expected Result:
# Total minutes = 120
# Actual Result:
# Total displayed correctly.
# Status: PASS

# Findings:
# The program successfully:
# - Accepts a user input.
# - Compares planned and actual study times.
# - Calculates total study time.
# - Calculates average focus rating.
# - Displayed summary information.
# - Allows multiple study sessions.
# - Ended correctly when the user selected "n".
# One issue discovered is that invalid input (such as entering
# letters instead of numbers) causes the program to crash
# because input validation has not yet been implemented.

# Next Steps
# Before the final project submission I plan to:
# - Add input validation.
# - Save study sessions to a file.
# - Load previous study sessions.
# - Display the most studied subject.
# - Add a menu system.
# - Allow users to edit and delete study sessions.
# - Improve formatting of the summary.
# Features not yet implemented and therefore not tested:
# - Study history
# - File saving/loading
# - Edit sessions
# - Delete sessions
# - Subject search