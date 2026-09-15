grade = int(input("Enter your grade: "))
if grade == 100:
    print("You got an A+")
elif grade >= 90:
    print("You got an A")
elif grade >= 80:
    print("You got a B")
elif grade >= 70:
    print("You got a C")
elif grade >= 60:
    print("You got a D")
elif grade < 60:
    print("You got an F")
elif grade == 0:
    print("You got an F")