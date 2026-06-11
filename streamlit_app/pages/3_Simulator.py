import streamlit as st
import random
from utils import simulate_match, team_strength

st.title("🎲 World Cup Simulator")

teams = list(team_strength.keys())

def simulate():
    t1, t2 = random.sample(teams, 2)
    winner, g1, g2 = simulate_match(t1, t2)
    return f"{t1} {g1}-{g2} {t2} → {winner}"

if st.button("Run Simulation"):
    for i in range(10):
        st.write(simulate())