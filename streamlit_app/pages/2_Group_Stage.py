import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import team_strength

st.title("🌍 Group Stage Overview")

teams = list(team_strength.keys())[:12]

scores = [team_strength[t] for t in teams]

fig, ax = plt.subplots()
ax.bar(teams, scores)
plt.xticks(rotation=45)

st.pyplot(fig)