#program to fund out wheather a student has passed or failed if it requires a total of 40% and 30% in each subject to pass . 
#assume 3 subjects and take marks as input from user

# Program to check if a student has passed or failed
total_marks = 300
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

# Calculate passing marks
total_pm = (total_marks * 40) / 100  # Total passing marks (40%)
each_pm = (100 * 30) / 100          # Passing marks per subject (30%)
marks_obtained = m1 + m2 + m3       # Total marks obtained

# Check conditions for passing
if marks_obtained >= total_pm:
    if m1 >= each_pm and m2 >= each_pm and m3 >= each_pm:
        print("Passed")
    else:
        print("Failed: Did not meet the passing criteria in one or more subjects.")
else:
    print("Failed: Total marks are less than 40%.")


#more optimized way 
# TOTAL_MARKS = 300
# PASS_PERCENT_TOTAL = 40  # 40% required in total
# PASS_PERCENT_SUBJECT = 30  # 30% required in each subject

# # Input marks for 3 subjects
# marks = [int(input(f"Enter marks of subject {i+1}: ")) for i in range(3)]

# total_passing_marks = TOTAL_MARKS * PASS_PERCENT_TOTAL / 100
# subject_passing_marks = 100 * PASS_PERCENT_SUBJECT / 100

# if sum(marks) >= total_passing_marks and all(mark >= subject_passing_marks for mark in marks):
#     print("Passed")
# else:
#     print("Failed")
