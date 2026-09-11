total = 0

for i in range(5):
    marks = int(input("Enter marks: "))
    total = total + marks

percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Total =", total)
print("Percentage =", percentage,"%")
print("Grade =", grade)