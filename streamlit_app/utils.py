import numpy as np
import random
import pandas as pd
import os

# Get the directory where utils.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Build an absolute path to the data folder
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "matches.csv")

# Load data safely
df = pd.read_csv(DATA_PATH)


df.head()

teams = list(set(df["team1"]).union(set(df["team2"])))

# reuse your learned strengths idea
team_strength = {}

for team in teams:
    r1 = df[df["team1"] == team]["team1_rank"].mean()
    r2 = df[df["team2"] == team]["team2_rank"].mean()

    if np.isnan(r1): r1 = 20
    if np.isnan(r2): r2 = 20

    team_strength[team] = (r1 + r2) / 2


def expected_goals(rank):
    return max(0.3, 3.5 - (rank / 10))


def simulate_goals(r1, r2):
    return np.random.poisson(expected_goals(r1)), np.random.poisson(expected_goals(r2))


def simulate_match(team1, team2):
    r1 = team_strength.get(team1, 20)
    r2 = team_strength.get(team2, 20)

    g1, g2 = simulate_goals(r1, r2)

    if g1 > g2:
        return team1, g1, g2
    elif g2 > g1:
        return team2, g1, g2
    else:
        return random.choice([team1, team2]), g1, g2