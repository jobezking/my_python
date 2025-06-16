import random

# Set the secret_number variable here (between 1 and 10)
# Initialize the guess variable here with a value of 0

secret_number = 9
guess = 0

roll = 0
while roll != 6:
    roll = random.randint(1, 6) 
    print("You rolled a", roll)

total = 0
for number in range(1, 101): 
    total += number
    print("The sum is:", total)

numbers = [1, 2, 3, 4, 5]
index = 0

for i in range(1, 11):
    for j in range(1, 11):
        print(i, j, end="\t") # Print on the same line with a tab sep 
    print() # Move to the next line after each row

while index < len(numbers):
    if numbers[index] % 2 == 0:
        print(numbers[index])
    index += 1

while guess != secret_number:  # Add the while loop condition here
	guess = random.randint(1, 10)
	print(f"Guessing: {guess}")

print(f"I guessed the right number! It was {secret_number}")

for i in range(1, 11):
  print(i)

valid_input = False
while not valid_input:
  user_input = input("Please enter a number greater than 0: ")
  if user_input > 0:
    valid_input = True
  else:
    print("Invalid input. Please try again.")

player_score = 80

if player_score > 100:
  print("Congratulations! You scored over 100 points.")
else:
  print("Keep trying to beat your high score!")

for i in range(1,11): # This loop prints 1 through 10, not through 11
    print(i)

number = 1
while number <= 10:
    print(number) 
    number = number + 1