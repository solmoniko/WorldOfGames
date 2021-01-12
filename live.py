from Score import add_score

def welcome(name):
    score = open('Scores.txt', "w") #new game so score=0
    score.write("0")
    name = input('enter your name:')
    print('Hello,'+ name +' welcome to World of Games (WOG)')
    print('here you can find many cool games')

def load_game():
    print('\n' * 2)
    print('please choose a game to play:')
    print('1.Memory Game - a sequence of numbers will appear for 1 sercond and you have to guess it back')
    print('2.Guess Games - guess a number and see if you chose like the computer')
    print('3.Currency Roulette - try and guess the value of a random amount of USD in ILS')
    game_number =input('Game Number:')

    while game_number >'3' or game_number <'0':
        game_number =input('Please choose game number Game Number 1 to 3: ')

    game_difficulty = input('please choose game difficulty:')
    while game_difficulty >'5' or game_difficulty <'0':
      game_difficulty = input('Please choose difficulty between 1 to 5: ')



    if game_number =="1":
     from MemoryGame import play
     play(game_difficulty)
     add_score(game_difficulty)
     load_game()

    if game_number =="2":
     from GuessGame import play
     play(game_difficulty)
     add_score(game_difficulty)
     load_game()

    if game_number =="3":
     from CurrencyRouletteGame import play
     play(game_difficulty)
     add_score(game_difficulty)
     load_game()



