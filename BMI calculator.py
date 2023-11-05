# Define a function to calculate BMI
def bmi_calculator(weight, height):
    # Convert weight from kg to pounds
    weight = weight * 2.205
    # Convert height from meters to inches
    height = height * 39.37
    # Calculate BMI using the formula: BMI = weight / height^2 * 703
    bmi = weight / (height ** 2) * 703
    # Return the BMI value
    return bmi

# Ask the user to input their weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Call the function and print the result
bmi = bmi_calculator(weight, height)
print("Your BMI is", bmi)
