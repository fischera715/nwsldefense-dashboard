import streamlit as st
import pandas as pd

st.title("NWSL Defensive Stats")

# Load CSV
df = pd.read_csv("2023_nwsl_full.csv")

st.write("Here are the first 5 rows of the data:")
st.dataframe(df.head())

position = df['position'].unique()
selected_position = st.sidebar.selectbox("Select Position", options=position)

min_games = st.sidebar.slider("Minimum Games Played", min_value=0, max_value=int(df['games_played'].max()), value=0)

# Filtering the data
filtered_df = df[(df['position'] == selected_position) & (df['games_played'] >= min_games)]

st.write(f"Showing {len(filtered_df)} players for {selected_position} with at least {min_games} games:")
st.dataframe(filtered_df)
