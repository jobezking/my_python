new_list = []
coin_flips = [True, False, True, True, False] #booleans
student_record = ["Aashvi", 24, "Computer Science", 3.8, True] #mixed values, though dictionaries should be used
print(student_record)

grocery_list = ["milk", "hummus", "bread", "cheese", "apples"]
print(grocery_list[0])
print(len(grocery_list))
print(grocery_list[len(grocery_list) - 1])
#more readable
last_element = len(grocery_list) - 1
print(grocery_list[last_element])
#access and print item 0 through item 2 of list (slicing): 
print(grocery_list[0:2])

#Scenario: You have a list of scores for students on an examination, and you'd like to calculate the average. 
# #You will need to calculate the total of the exam scores and then divide by the number of elements:
# 1. Start with a variable to store the total score
# 2. Loop through each score in the list (list comprehension)
# 3. Add the current score to the total score
# 4. Calculate the average score
# 5. Print the average score

exam_scores = [85, 90, 78, 92, 88]
total_score = 0
for score in exam_scores:
   total_score = total_score + score
   average_score = total_score / len(exam_scores)
print("The average score is:", average_score)

fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]

fruit_length = len(fruits)
print(fruit_length)

fruits.append("date")

students = ["Alice", "Bob", "Charlie"]
for i in range(0,len(students)):
    print("Hello,", students[i])

for student in students:
    print("Hello,", student)