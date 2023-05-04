def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight/(height*height)
    print("BMI = ", BMI)
    if (BMI<18.5):
        print("Under Weight")
    if (BMI>25):
        print("Over Weight")

    else :
        print("Normal Weight")



calculate_bmi(weight=57, height=1.73)