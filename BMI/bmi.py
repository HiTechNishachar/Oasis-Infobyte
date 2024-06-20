# Simple BMI Calculator

# Get user input for weight and height
weight = input("Enter your weight in kilograms: ")
height = input("Enter your height in meters: ")

# Convert the input strings to float
weight = float(weight)
height = float(height)

# Calculate BMI
bmi = weight / (height ** 2)

# Determine the BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

# Print the results
print("Your BMI is:", round(bmi, 2))
print("BMI Category:", category)

