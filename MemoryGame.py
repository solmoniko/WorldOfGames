import random
from Utils import screen_cleaner

def play(game_difficulty):

 randomlist = random.sample(range(1,101),int(game_difficulty))
 print(randomlist)
 from time import sleep
 sleep(0.9)
 screen_cleaner()
 startgame(game_difficulty,randomlist)


def startgame(game_difficulty,randomlist):
 for i in range(0,int(game_difficulty)):
  print('enter number at index '+str(i+1))
  get_list_from_user =int(input())
  if get_list_from_user != randomlist[i]:
   print('no,maybe next time .. good bye')
   quit()

  else:
   print('right!')
 print('\n' * 2)
 print("well done !")





