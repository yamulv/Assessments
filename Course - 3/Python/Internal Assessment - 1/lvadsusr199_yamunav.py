# -*- coding: utf-8 -*-
"""LVADSUSR199_YamunaV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tiQ3hwb-eVexUyCz6AZqVBTGyQjVx7l9

Lab 1
"""

# Question 1
length = eval(input("Enter length in meters: "))
width = eval(input("Enter width in meters: "))
area = length * width
print("Area: ", area)
if area<=100:
  print("small")
elif area >100 and area<=1000:
  print("medium")
else:
  print("large")

# Question 2
weight = eval(input("Enter weight in kg: "))
height = eval(input("Enter height in meters: "))
bmi = weight/(height * height)
print("BMI: ",bmi)
print("Based on your BMI, follow the suggestions below:")
print("BMI is less ---> malnutrition ---> please add vegetables and proteins")
print("BMI is normal ---> Good --->  please follow your diet")
print("BMI is exceeding normal  ---> obese ---> Cutdown calories")

# Question 3
student_dict = {1:{"Maths": 95, "English": 97}, 2:{"Maths": 89, "English": 90}}
print(student_dict)
#add
student_dict[3]={"Maths":54, "English":67}
print(student_dict)
#update
student_dict[2]={"Maths":100}
print(student_dict)
#retrive
print("Student 1 report: " , student_dict[1])

"""Lab 2"""

# Question 4
age = int(input("Enter age: "))
print("Age: ", age)
print("Recommended Movie and TV Shows")
if age<=15:
  print("Recommended for Kids")
elif age>15 and age<=20:
  print("Recommended for Teens")
elif age>20 and age<=50:
  print("Recommended for Adults")
else:
  print("Recommended for Seniors")

# Question 5
subscriber_id = [1,2,3,4,5,6,7,8,9,10]
even_sub_id =[]
for i in range(len(subscriber_id)):
  if (i+1)% 2 == 0:
    even_sub_id.append(subscriber_id[i])
print("List of even subscriber id : ",even_sub_id)

# Question 6
access = {"abc": 123, "def":456}
while True:
  user_name = input("Enter username: ")
  password = eval(input("Enter Password: "))
  if access[user_name] == password:
    print("Login success")
    break

"""Lab 3"""

# Question 7
feedback_score = [2,5,9,8,9,6]
avg_feedback_score = sum(feedback_score)/len(feedback_score)
print("avg_feedback_score: ", avg_feedback_score)
if avg_feedback_score<5:
  print("Needs Improvement")
elif avg_feedback_score>=5 and avg_feedback_score<=8:
  print("Good")
else:
  print("Excellent")

# Question 8
print("Comment quality")

content = "To count vowels to access comment quality"
content.lower()
vowels_count = content.count("a")+content.count("e")+content.count("i")+content.count("o")+content.count("u")
print(vowels_count)

# Question 9
import datetime
if True:
  print("Upcoming event, deadline at ", datetime.datetime.now())

"""Lab 4"""

# Question 10
try:
  loan = eval(input("Enter loan amount: "))
  no_of_months = eval(input("Enter number of months: "))
  loan_interest_per_month = (loan * 0.12)/(no_of_months)
  print(loan_interest_per_month)
except:
  print("Some error has occured")
  print("Please enter valid details")

# Question 11
try:
  name = input("Enter name :")
  age = int(input("Enter age: "))
  print(name," ",age)
except:
  print("Name error")

# Question 12
try:
  division = 100/0
  print(division)
except:
  print("Division by zero error")

"""Lab 5"""

# Question 13
#f = open("logfile.txt","x")
f = open("logfile.txt","w")
f.write("Server uptime is 2 hours")
f.close()

x = open("logfile.txt","r")
print(x.read())
x.close()

# Question 14
x = open("logfile.txt","r")
print(x.read())
x.close()

# Question 15

y = open("logfile.txt","a")
y.write("\nCompany news, Stock performance, Industry news")
y.close()

z = open("logfile.txt","r")
print(z.read())
z.close()