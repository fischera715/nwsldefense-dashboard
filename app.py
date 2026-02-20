import streamlit as st
import pandas as pd
import plotly.express as px

st.title("NWSL Defensive Stats")

st.markdown( """**Analytical Objective**
This dashboard analyzes defensive performance for players in the National Womens Soccer Legue (NWSL), focussing on tackles, interceptions, 
and other defensive metrics to identify key contributors or trends""")

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

# Bar plot to visualize players with the most tackles
bar = px.bar(
  filtered_df, x = "player_name", y = "tackles", color = "tackles", title = "Total Tackles per Player", 
  labels = {"player_name": "Player Name", "tackles": "Total Tackles"},
  height = 500
  )

st.plotly_chart(bar, use_container_width = True)

# Scatter plot of player tackles vs. interceptions
scatter = px.scatter(
  filtered_df, x = "tackles", y = "interceptions", size = "minutes_played", color = "position", hover_name = "player_name", 
  title = "Tackles vs. Interceptions per Player",
  labels = {"tackles": "Total Tackles", "interceptions": "Total Interceptions"},
  height = 500
)

st.plotly_chart(scatter, use_container_width = True)

corr = filtered_df["tackles"].corr(filtered_df["interceptions"])
st.write(f"Correlation between tackles and interceptions:" {corr.2f})





