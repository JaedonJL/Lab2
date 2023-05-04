def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight/(height*height)
    print("BMI = ", BMI)
    if (BMI<18.5):
        print("-1")
    if (BMI>25):
        print("1")

    else :
        print("0")



calculate_bmi(weight=57, height=1.73)