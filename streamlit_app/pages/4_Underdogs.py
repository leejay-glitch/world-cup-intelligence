import streamlit as st
import random
from utils import team_strength

st.title("🚨 Underdog Watch")

teams = list(team_strength.keys())

for _ in range(10):
    t1, t2 = random.sample(teams, 2)

    diff = abs(team_strength[t1] - team_strength[t2])

    if diff < 3:
        st.warning(f"{t1} vs {t2} → High upset risk ⚠️")