#student details
student_name = input("entre the name of student")
usn = input("entre the usn")
branch = input("entre the branch")
semester = input("entre the semester")
#n.o of marks the student got
mark1 = float(input("entre the marks in subjet1"))
mark2 = float(input("entre the marks in subject2"))
mark3 = float(input("entre the marks in subject3"))
#calculating the total and average marks of the student
total = mark1 + mark2 + mark3
average = total/3
#displaying the information using formatted output
print(f"student name:{student_name}")
print(f"usn:{usn}")
print(f"branch:{branch}")
print(f"semester:{semester}")
print(f"total marks:{total}")
print(f"average marks:{average:.2f}")
