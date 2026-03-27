class Player:
    def __init__(self, name, time, difficulty):
        self.name = name
        self.time = time
        self.difficulty = difficulty

    def to_dict(self):
        return {
            "name": self.name,
            "time": self.time,
            "difficulty": self.difficulty
        }