def compute_grade(marks):
    try:
        marks = float(marks)
        if marks>1.0 or marks<0.0:
            return "Invalid Marks Entered"
        else:
            if marks<0.6:
                return "F"
            elif marks<0.7:
                return "D"
            elif marks<0.8:
                return "C"
            elif marks<0.9:
                return "B"
            else:
                return "A"
    except:
        return "Invalid Marks Entered"


score = input("Enter the score: ")
grade = compute_grade(score)
print("Marks = ",score," Grade = ",grade)
