
from flask import Flask
import Utils


HOST = '192.168.1.10'
PORT = int('3031')


app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        score = open('Scores.txt', "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">"""+ Utils.Error_Code +  """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""

app.run(host=HOST,threaded=True, port=PORT)