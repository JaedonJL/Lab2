def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    checking = 0
    BMI = weight/(height*height)
    print("BMI = ", BMI)
    if (BMI<18.5):
        checking = -1
    if (BMI>25):
        checking = 1

    else :
        checking = 0
    print(checking)
    return checking


calculate_bmi(weight=57, height=1.73)