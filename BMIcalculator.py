#BMI Calculator 2.0


# Assign appropriate variables.
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# Combine variables into code to obtain appropriate calculations.
bmi = round(weight / height ** 2)
bmi_as_int = int(bmi)

# Using "if / elif / else" conditions you can establish ranges and messages to elaborate results. 
if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight. ")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you are underweight. ")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you have a normal weight. ")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you need self control. ")
else:
  print(f"Your bmi is {bmi}, you need clinical help ")
# Using the code above you are able to calculate your BMI percentage.

