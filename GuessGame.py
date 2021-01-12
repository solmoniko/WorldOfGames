def play(game_difficulty):
 import random
 print(game_difficulty)
 secret_number = random.randint(1,int(game_difficulty))
 get_guess_from_user = input('guess a number: ')
 print(get_guess_from_user)
 if  int(secret_number) == int(get_guess_from_user) :
    print('Right!,Well done!')
    return
 else :
   print('No .. Maybe next time')
   quit()
