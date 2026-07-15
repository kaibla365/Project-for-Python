# CS344 Final Project - milestone1_design.pdf.py
# Project Title: Study session planner/ Focus Tracker
# Kaiden Blanchard

# Problem Description
# Many students struggle to stay focused while studying because being that they do not organize their study sessions
# or seem to care to keep track of how productive they are. This program will allow users to create study sessions,
# record how long they studied and rate their focus level during their session while getting a generated report
# of their study habits.

# The intended users are high school and college students with need to improve their study routines/habits.
# Instead of writing everything down on paper, users can enter their study information into this program to get a
# correlated statistics review showing how productive they have been.

# This project is useful because it encourages better time management while helping for students to recognize patterns
# in their studying. Through the viewing of summaries of their study time and focus ratings, users can further determine
# which subjects require more attention, and which study sessions are the most productive.

# Assumptions and Limitations:
# - This version is designed for one user at a time.
# - Information is stored only while the program is running.
# - Versions in the future may save data to a file.
# - Study time is entered in whole minutes.
# - Focus ratings must be between 1 and 10.

# Inputs and Outputs
# Inputs:
# - User's name
# - Subject being studied
# - Planned study time (minutes)
# - Actual study time (minutes)
# - Focus rating (1-10)
# - Menu choice
# - Whether the user wants to add another continuous study session

# Outputs:
# - Confirmation that a study session was added
# - Total number of study sessions
# - Total study time
# - Average focus rating
# - Most studied subject
# - Productivity summary

# Example Input:
# Name: Kaiden
# Subject: Python Programming
# Planned Time: 60
# Actual Time: 75
# Focus Rating: 10


# Example Output:
# Study session recorded!
# Total Study Sessions: 1
# Total Minutes Studied: 75
# Average Focus Rating: 10.0
# Great job Kaiden! You studied longer than planned.


# Algorithm Overview
# Step 1:
# Display the main menu.
# Allow the user to choose between adding a study session, viewing statistics, or quitting the program.

# Step 2:
# Ask the user for study session information.
# Collect the subject, planned study time, actual study time, and focus rating.

# Step 3:
# Validate the user's input.
# Make sure study times are positive numbers and focus rating is between 1 and 10.

# Step 4:
# Store the study session information.
# Save information in lists so it can later be summarized.

# Step 5:
# Calculate statistics.
# Determine total study time, average focus rating, and the most studied subject.

# Step 6:
# Display updated summary.
# Show user the calculated statistics after each session.

# Step 7:
# Repeat until the user chooses to quit.
# Loop:
# Continue displaying the menu until the user exits.
# Decision:
# Use if/else statements to determine which menu option
# the user selected and whether they met their planned study time.


# Planned Structure and Functions


# Function: get_study_session()
# Purpose: Collect information about a study session from the user.
# Parameters:
# None
# Returns:
# Subject, Planned study time, Actual study time, Focus rating


# Function: calculate_statistics()
# Purpose:Calculate totals and averages using the stored study data.
# Parameters:
# Lists containing study times, focus ratings, and subjects.
# Returns:
# Total study time, Average focus rating, Most studied subject

# Function: display_summary()
# Purpose:Display the study statistics in a readable format.
# Parameters:
# Calculated statistics.
# Returns:
# Nothing (prints the results).

# Function: validate_input()
# Purpose: Ensure study times are positive numbers and focus ratings are between 1 and 10.
# Parameters:
# User input.
# Returns:
# A validated value that can safely be used in the program.
