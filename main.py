import pandas as pd

class DeveloperAchievementsCalculator:
    """
    Gamified Developer Profile Achievements Engine
    Inspects commit count metrics and unlocks special achievements.
    """
    def __init__(self):
        self.badge_rules = {
            "First Step": 1,
            "10x Committer": 10,
            "Code Warrior": 50,
            "Open Source Titan": 100
        }

    def evaluate_profile(self, commits_count):
        unlocked = []
        for badge, threshold in self.badge_rules.items():
            if commits_count >= threshold:
                unlocked.append(badge)
        return unlocked

if __name__ == "__main__":
    calc = DeveloperAchievementsCalculator()
    print("Unlocked Achievements (Count: 65 Commits):")
    print(calc.evaluate_profile(65))
