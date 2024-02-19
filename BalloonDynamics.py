import random

class BalloonDynamics:
    def __init__(self):
        self.spawn_rate = 2.0  # Initial spawn rate (balloons per second)
        self.speed = 2.5  # Initial speed of balloons
        self.difficulty_level = 1  # Initial difficulty level
        self.time_elapsed = 0.0

    def update_spawn_rate(self, score):
        # Update spawn rate dynamically based on game conditions
        # Higher score leads to faster spawn rate
        self.spawn_rate = 2.0 + score * 0.1  # Example: Increase spawn rate by 0.1 for every point scored

    def update_speed(self):
        # Update speed dynamically based on game conditions
        # Speed increases gradually over time
        self.speed += 0.05  # Example: Increase speed by 0.05 units per second

    def update_difficulty(self):
        # Update difficulty level based on time elapsed
        if self.time_elapsed > 30 and self.difficulty_level == 1:
            self.difficulty_level = 2
            print("Difficulty level increased to 2!")
        elif self.time_elapsed > 60 and self.difficulty_level == 2:
            self.difficulty_level = 3
            print("Difficulty level increased to 3!")
        # Add more conditions as needed for higher difficulty levels

    def update(self, score, delta_time):
        self.time_elapsed += delta_time
        self.update_spawn_rate(score)
        self.update_speed()
        self.update_difficulty()

    def get_spawn_rate(self):
        return self.spawn_rate

    def get_speed(self):
        return self.speed

    def get_difficulty_level(self):
        return self.difficulty_level
