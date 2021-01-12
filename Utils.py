import os

Error_Code = "ERROR - The file Scores.txt is missing"


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')
