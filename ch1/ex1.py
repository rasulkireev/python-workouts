from random import randint

def guessing_game():
  random_number = randint(0, 100)

  while True:
    user_guess = int(input("Guess the number. Enter your guess and press enter..."))
    if user_guess > random_number:
      print("Too High. Try again.")
      continue
    elif user_guess < random_number:
      print("Too Low. Try again.")
      continue
    else:
      print("Just Right")
      break

if __name__ == '__main__':
  guessing_game()