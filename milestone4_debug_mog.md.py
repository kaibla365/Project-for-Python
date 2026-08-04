# CS344 Final Project
# Project Title: Study Session Planner / Focus Tracker
# Kaiden Blanchard
# Repository: https://github.com/kaibla365/Project-for-Python

# Bug 1
# Description:
# Program crashed when the user entered letters instead of
# numbers for the planned study time, actual study time,
# or focus rating.

# Context:
# This occurred in the get_study_session() function while I was testing different user inputs.

# Symptoms:
# The program displayed a ValueError because Python isn't able to convert text into an integer using int().

# Root Cause and Fix:
# The problem was caused by using int() without me validating the user's input first.
# I noted that for future versions I should include input validation that uses try/except block to prevent the program from crashing.

# Debugging Technique:
# I intentionally entered invalid inputs like "hello" instead of a number.
# Reading the error message showed exactly which line caused the ValueError which allowed me to determine the source of the problem.

# Bug 2
# Description:
# The summary totals appeared incorrect after entering several study sessions.

# Context:
# This happened while testing multiple study sessions loop in the  the main() loop.

# Symptoms:
# The totals are very inconsistent because I expected them to update after every study session.

# Root Cause and Fix:
# After tracing the variables I found that total_sessions, total_minutes, and total_focus had been
# increasing correctly inside the loop. Rather the issue was caused by my misunderstanding of the expected totals rather than a standout programming error.

# Debugging Technique:
# I added temporary print statements to display the values for better accessibility of the running totals after every iteration.
# This helped me to confirm that the calculations were correct.

# Bug 3

# Description:
# The encouragement message displayed unexpectedly during one of my early tests.

# Context:
# The issue occurred in the process_session() function.

# Symptoms:
# I expected the program to display the "Great job!"
# message but instead received the opposing encouragement message.

# Root Cause and Fix:
# After reviewing the test inputs to begin with, I discovered that the
# actual study time I entered was smaller than the planned
# study time. The program logic was correct, and no code changes were necessary.

# Debugging Technique:
# I traced the values by hand and compared them with the if/else conditions.
# This ended up confirming that the program was behaving exactly as intended.

# Bug 4

# Description:
# The average focus rating was showcasing too many
# decimal places.

# Context:
# This occurred in the display_summary() function.

# Symptoms:
# The output contained long decimal numbers which made the summary difficult to read.

# Root Cause and Fix:
# I updated the print statement to rather use the round() function for the average focus rating to display with one decimal place.

# Debugging Technique:
# I tested several different focus ratings with compared outputs before and after using round().
# The results became much easier to understand.

# Bug 5
# Description:
# The program was continuing to ask me for another study session even when users entered uppercase letters.

# Context:
# This occurs near the end of the main() function when it is checking whether the user wanted to continue.

# Symptoms:
# Entering "Y" or "N" sometimes caused unexpected behavior.

# Root Cause and Fix:
# I converted the user's response to lowercase using the
# lower() function before comparing it with "y". THIS ALLOWED me to be abel to use both uppercase and lowercase responses to work.

# Debugging Technique:
# I repeatedly tested the program using uppercase and
# lowercase responses.  Through comparing the results confirmed that lower() fixed the issue.

# Reflection and Patterns
# Pattern 1:
# Many of my upcoming issues involved user input. Invalid or unexpected
# input often caused errors or confusing results.
# Pattern 2:
# Several problems became prevalent through assumptions made during
# testing rather than actual programming mistakes. Careful
# testing showed that the program logic was functioning
# correctly.

# Lessons Learned:
# 1. Test the program with many different types of input, including the knowledge of invalid data
# 2. Use temporary print statements to check variable values during debugging.
# 3. Read Python error messages carefully because they may identify the exact line causing the problem.
# 4. Continue adding input validation in effort to improve the user experience in future milestones.