import json
from models.player import Player

FILE_PATH = "data/leaderboard.json"


class LeaderboardManager:
    def load(self):
        try:
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
                return [Player(**item) for item in data]
        except FileNotFoundError:
            return []

    def save(self, players):
        with open(FILE_PATH, "w") as f:
            json.dump([p.to_dict() for p in players], f, indent=4)

    def add_player(self, player):
        players = self.load()
        players.append(player)

        players.sort(key=lambda x: x.time)

        players = players[:10]

        self.save(players)

    def show(self):
        players = self.load()

        print("\n🏆 Leaderboard:")
        for i, p in enumerate(players, 1):
            print(f"{i}. {p.name} - {p.time}s ({p.difficulty})")