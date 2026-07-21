# Course Project: Study Session Planner by Kaiden Blanchard
# Repository: https://github.com/kaibla365/Project-for-Python

# Functions to get study session information
def get_study_session():

    subject = input("Enter the subject you studied: ")

    planned_time = int(input("Enter planned study time (minutes): "))

    actual_time = int(input("Enter actual study time (minutes): "))

    focus_rating = int(input("Enter your focus rating (1-10): "))

    return subject, planned_time, actual_time, focus_rating

# Functions to process each study sessions information
def process_session(planned_time, actual_time, focus_rating):

    if actual_time >= planned_time:
        message = "Great job! You met or exceeded your study goal."
    else:
        message = "Keep practicing! Try reaching your planned study time next session."

    return message

# Functions set toward displaying results
def display_summary(total_sessions, total_minutes, average_focus):

    print("\n========== Study Summary ==========")
    print("Total Study Sessions:", total_sessions)
    print("Total Minutes Studied:", total_minutes)
    print("Average Focus Rating:", round(average_focus, 1))
    print("===================================\n")

# Main functions
def main():

    total_sessions = 0
    total_minutes = 0
    total_focus = 0
    while True:

        subject, planned, actual, focus = get_study_session()

        feedback = process_session(planned, actual, focus)

        total_sessions += 1
        total_minutes += actual
        total_focus += focus

        average_focus = total_focus / total_sessions

        print("\nSubject:", subject)
        print(feedback)

        display_summary(total_sessions, total_minutes, average_focus)

        again = input("Would you like to enter another study session? (y/n): ").lower()

        if again != "y":
            break

    print("\nThank you for using the Study Session Planner!")
    print("Good luck with your studying!")
# Start of program
main()