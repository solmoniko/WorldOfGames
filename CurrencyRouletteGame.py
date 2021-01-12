def play(game_difficulty):
 from random import randint
 difficulty =int(game_difficulty)
 money = randint(1, 100)
 currency = 3.6*money
 money_interval = [currency - (5 - difficulty), currency + (5 - difficulty)]

 user_guess = input("Guess the approximately is the currency of " + str(money) + " from USD to ILS? ")
 money_up = money_interval[1]
 money_down = money_interval[0]

 if int(money_down) <= int(user_guess) <= int(money_up) :
  print('Right!,Well done!')
 else:
  print('Wrong,maybe next time .. good bye')
  quit()