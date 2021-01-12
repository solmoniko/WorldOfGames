def add_score(game_difficulty):

 o= open('Scores.txt',"r")
 old_score = o.read()
 print("Old Score:  "+old_score)

 POINTS_OF_WINNING = (int(game_difficulty) * 3) + 5

 new_points = int(old_score)+int(POINTS_OF_WINNING)

 score = open('Scores.txt',"w")
 write_text =str(new_points)
 print("New Score:  " +write_text)
 score.write(write_text)


