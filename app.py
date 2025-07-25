from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

Rock = "r"
Paper = "p"
Scissors = "s"

emojies = {Rock: "🪨", Scissors: "✂️", Paper: "📃"}
choices = tuple(emojies.keys())

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie!"
    elif (
        (user_choice == Rock and computer_choice == Scissors) or
        (user_choice == Scissors and computer_choice == Paper) or
        (user_choice == Paper and computer_choice == Rock)
    ):
        return "You Win 🏆!"
    else:
        return "You Lose 😢!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play', methods=["POST"])
def play():
    user_choice = request.json["choice"]
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    return jsonify({
        "user_choice": emojies[user_choice],
        "computer_choice": emojies[computer_choice],
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
