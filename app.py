from flask import Flask, request, render_template, redirect, flash, session, jsonify
from boggle import Boggle
from flask_debugtoolbar import DebugToolbarExtension

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

app.config["SECRET_KEY"] = "secretkey"


boggle_game = Boggle()


@app.route("/start")
def start_boggle():
    ###create boggle board
    board_create = Boggle()
    created_board = board_create.make_board()
    ###Get make board method from boggle.py
    session["created_board"] = created_board
    ##get the session for our created board
    return render_template("start.html", board = created_board)


# @app.route("/check_word", methods=["POST"])
# def check_word():
#     data = request.get_json()
#     print(data)
#     guessed_word = data.get("word")
#     print(guessed_word)
#     ##AttributeError: 'NoneType' object has no attribute 'get'
#     if guessed_word in boggle_game.words:
#         result = "ok"
#     else:
#         result = "not-a-word"
#     return jsonify({"result": result})

valid_words = set()
with open('words.txt', 'r') as file:
    for line in file:
        valid_words.add(line.strip().lower())


@app.route("/check_word", methods=["POST"])
def check_word():
    data = request.get_json()
    if data and "word" in data:
        print(data)
        guessed_word = data["word"].lower()  # Convert guessed word to lowercase for case-insensitive matching
        if guessed_word in boggle_game.words:
            result = "ok"
        else:
            result = "not-a-word"
        return jsonify({"result": result})
    else:
        return jsonify({"result": "invalid-data"})
    

if __name__ == "__main__":
    app.run(debug=True)  # or app.run() for production