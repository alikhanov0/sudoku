from solver.backtracking_solver import BacktrackingSolver
from services.leaderboard_manager import LeaderboardManager
from models.player import Player
import time
from services.generator import Generator


def main():
    start_time = time.time()

    generator = Generator()
    difficulty = "medium"
    board = generator.generate(difficulty)
    solver = BacktrackingSolver()

    print("Before:")
    board.print_board()

    if solver.solve(board):
        print("\nSolved:")
        board.print_board()

        end_time = time.time()
        elapsed = int(end_time - start_time)

        try:
            name = input("Enter your name: ")
        except Exception:
            name = "Unknown"

        player = Player(name, elapsed, difficulty)

        lb = LeaderboardManager()
        lb.add_player(player)
        lb.show()

    else:
        print("No solution found")


if __name__ == "__main__":
    main()