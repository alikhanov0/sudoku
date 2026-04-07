from flask import Flask, render_template, request
from services.generator import Generator
from solver.backtracking_solver import BacktrackingSolver
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

generator = Generator()
solver = BacktrackingSolver()


@app.route("/", methods=["GET", "POST"])
def index():
    difficulty = "easy"

    if request.method == "POST":
        difficulty = request.form.get("difficulty", "easy")

    board = generator.generate(difficulty)

    return render_template("index.html", board=board.grid, difficulty=difficulty)


@app.route("/solve", methods=["POST"])
def solve():
    grid = []

    for i in range(9):
        row = []
        for j in range(9):
            val = request.form.get(f"cell-{i}-{j}")
            row.append(int(val) if val else 0)
        grid.append(row)

    from models.board import Board
    board = Board(grid)

    solver.solve(board)

    return render_template("index.html", board=board.grid, difficulty="custom")


if __name__ == "__main__":
    app.run(debug=True)