import streamlit as st
import pandas as pd
from utils import team_strength, simulate_match

st.title("⚔️ Match Predictor")

teams = list(team_strength.keys())

team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams)

if st.button("Predict Match"):
    winner, g1, g2 = simulate_match(team1, team2)

    st.subheader(f"Result: {team1} {g1} - {g2} {team2}")
    st.success(f"Winner: {winner}")