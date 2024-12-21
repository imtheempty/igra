from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Глобальные переменные для отслеживания состояния игры
game_data = {
    "total_winnings": 0,
    "lucky_numbers": [],
    "message": "",
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "start":
            # Генерация "счастливых чисел"
            game_data["lucky_numbers"] = sorted([random.randint(1, 6) for _ in range(3)])
            game_data["message"] = "New lucky numbers generated! Place your bets."
        elif action == "bet":
            try:
                bet_count = int(request.form.get("bet_count"))
                numbers = [int(request.form.get(f"number_{i + 1}")) for i in range(bet_count)]
                wagers = [int(request.form.get(f"wager_{i + 1}")) for i in range(bet_count)]

                winnings = 0
                for num, wager in zip(numbers, wagers):
                    count = game_data["lucky_numbers"].count(num)
                    if count > 0:
                        winnings += count * wager
                        game_data["message"] += f"You WIN {count} times on {num}! "
                    else:
                        winnings -= wager
                        game_data["message"] += f"You LOSE on {num}. "

                game_data["total_winnings"] += winnings
            except (ValueError, KeyError):
                game_data["message"] = "Invalid input. Please try again."
        elif action == "stop":
            return redirect(url_for("stop"))

    return render_template("index.html", game_data=game_data)


@app.route("/stop")
def stop():
    return render_template("stop.html", total_winnings=game_data["total_winnings"])


if __name__ == "__main__":
    app.run(debug=True)