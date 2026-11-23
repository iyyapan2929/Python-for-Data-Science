# Print numbers from 1 to 10

<<<<<<< HEAD
# for x in range(10, 1):
#   print(x)
=======
for x in range(1, 11):
  print(x)
>>>>>>> 8cbda93dc04557f94b9fadb4583f9158f08e25e0

# Print numbers from 10 to 1 in reverse order

# for x in range(10, 0, -1):
#     print(x)  

# Print all odd numbers between 1 and 50

# for x in range(1, 50, 2):
#   print(x)

# print all even numbers between 1 and 50

# for x in range(2, 50, 2):
#   print(x)

# Print the multiplication table of a number entered by the user

# a = int(input("enter number : "))
# for i in range(1, 11):
#   print(a, "x", i, "=", a*i)

# Calculate the sum of numbers from 1 to 100.

# total = 0

# for i in range(1, 101):
#     total += i

# print(total)

# calculate the sum of all even numbers between 1 and 100

# total = 0

# for i in range(2, 101, 2):
#   total += i
# print(total)

# Factorial number

# number = int(input("enter number : "))
# factorial = 1
# for i in range(1, number + 1):
#   factorial  *= i

# print(factorial)

# Fibonacci number

# a = 0
# b = 1
# for i in range(0, 10):
#   c = a + b
#   a = b
#   b = c

#   print(c)

# Multiplication tables

# a = int(input("Enter number : "))
# for i in range(1, 11):
#   print(a, "x", i, "=", a*i)

# Count down 

# for i in range(10, 0, -1):
#   print(i)
  
# print("Happy Birthday")

# Sum of 1 to 10


# total = 0

# array = [2, 3, 4, 9, 33, 45, 66, -3, -5]
# print(sum(array))

# for i in range(len(array)): # for i in range(0, 9):
#     total += array[i]
    
# print(total)


# sum = 0
# for num in array:
#   sum += num
# print(sum)

# array = [2, 3, 4, 9, 33, 45, 66]
# x = 33

<<<<<<< HEAD
# for num in array:
#   if x == num:
#     print(array.index(x))
# else:
#   print("invalid")
  
import random

CHOICES = ["rock", "paper", "scissors"]

# Each key beats its value
WINS_AGAINST = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_user_choice():
    """Ask the player for a valid choice."""
    while True:
        choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").strip().lower()
        if choice == "q":
            return None
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please try again.")


def get_winner(user, computer):
    """Return 'user', 'computer', or 'tie'."""
    if user == computer:
        return "tie"
    if WINS_AGAINST[user] == computer:
        return "user"
    return "computer"


def play():
    user_score = 0
    computer_score = 0
    ties = 0

    print("=== Rock, Paper, Scissors ===\n")

    while True:
        user = get_user_choice()
        if user is None:
            break

        computer = random.choice(CHOICES)
        print(f"\nYou chose:      {user}")
        print(f"Computer chose: {computer}")

        result = get_winner(user, computer)
        if result == "tie":
            ties += 1
            print("It's a tie!")
        elif result == "user":
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print(f"Score -> You: {user_score} | Computer: {computer_score} | Ties: {ties}\n")

    print("\n=== Final Score ===")
    print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    if user_score > computer_score:
        print("You won the game!")
    elif computer_score > user_score:
        print("The computer won the game!")
    else:
        print("The game ended in a draw.")


if __name__ == "__main__":
    play()  
  
=======
for num in array:
  if x == num:
    print(array.index(x))
else:
  print("invalid")
  
>>>>>>> 8cbda93dc04557f94b9fadb4583f9158f08e25e0
