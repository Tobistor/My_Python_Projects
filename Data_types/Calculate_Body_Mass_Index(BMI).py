# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
conv_weight = float(weight)
conv_height = float(height)

bmi = conv_weight / (conv_height*conv_height)
print(int(bmi))