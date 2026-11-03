# print(available_balance)

avail_bal = 5000
while avail_bal >= 0:
  amt = int(input("Enter amt ; "))
  if amt > avail_bal:
    print("Insufficient balance")
    continue
  avail_bal -= amt
  if amt == 0:
    break

print(avail_bal)  

a = int(input("Enter number : "))
while a >= 1:
  print(a)
  a -= 1

print("Hapieee bday wishes to you") 

a = int(input("Enter number : "))
i = 1
while i <= 10:
  print(a, "x", i, "=", a*i)
  i += 1

print("Multiplication table completed")

i = 1
while i <= 10:
  print(i)
  i += 1

secret_number = 29

while True:
  guessing_number = int(input("Enter number : "))
  if guessing_number != secret_number:
    print("Try again")
    continue
  else:
    print("Congratulations.....")
    break
print("while end")

secret_number = 55
guessing_number = int(input("Enter number : "))

while guessing_number != secret_number:
  print("bad luck! try again.")
  guessing_number = int(input("Enter number : "))

print("congrats")

secret_number = 29
attempts = 1
while attempts <= 5:
  guessing_number = int(input("Enter number : "))
  attempts += 1
  if guessing_number != secret_number:
    print("Try again")
    continue
  else:
    print("Congratulations!")
    break

secret_number = 29
attempts = 1

while attempts <= 5:
    guessing_number = int(input("Enter number: "))

    if guessing_number == secret_number:
        print("Congratulations!")
        break

    print("Try again")
    attempts += 1

else:
    print("You ran out of attempts!")
    print("The secret number was:", secret_number)

sum = 0
i = 0
while i <= 10:
  
  sum += i
  i += 1
print(sum)
