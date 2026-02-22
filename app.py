import streamlit as st
import pandas as pd
import plotly.express as px

tab1, tab2 = st.tabs(["League Overview", "Player Relationships"])

with tab1: 
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
  
  num_players = filtered_df.shape[0]
  st.write(f"This chart shows the total number of tackles per player. For the {selected_position} position, there are {num_players} represented."
           f" We can see the trends of how many tackles each player commits as a {selected_position}.")
  
  average_tackles = df.groupby('position')['tackles'].mean()
  selected_avg = average_tackles[selected_position]
  max_avg = average_tackles.max()
  
  st.write(f"On average, {selected_position} makes {selected_avg} tackles per season. Defenders have the max number of average tackles ({max_avg})"
           f", but are very similar to midfielders.")

with tab2:
  
  # Scatter plot of player tackles vs. interceptions
  scatter = px.scatter(
    filtered_df, x = "tackles", y = "interceptions", size = "minutes_played", color = "position", hover_name = "player_name", 
    title = "Tackles vs. Interceptions per Player",
    labels = {"tackles": "Total Tackles", "interceptions": "Total Interceptions"},
    trendline = "ols",
    height = 500
  )
  
  st.plotly_chart(scatter, use_container_width = True)
  
  corr = filtered_df["tackles"].corr(filtered_df["interceptions"])
  st.write(f"Correlation between tackles and interceptions: {corr:.2f}")
  
  st.write("For all positions except goalkeepers, there is a strong positive correlation (r>.7) between the number of tackles and interceptions. This"
           "suggests that players who engage in more tackles also tend to generate more interceptions, highlighting defensive effectiveness.")
  
  # Heatmap of fouls and cards by position
  foul_metrics = ['fouls_committed', 'yellow_cards', 'red_cards']
  position_avg = df.groupby('position')[foul_metrics].mean()
  
  heatmap = px.imshow(
      position_avg,
      labels=dict(x="Metric", y="Position", color="Average Count"),
      x=foul_metrics,
      y=position_avg.index,
      color_continuous_scale='Reds',
      title="Average Fouls and Cards by Position"
  )
  
  st.plotly_chart(heatmap, use_container_width=True)
  
  st.write("This heatmap shows the average fouls, yellow cards, and red cards by position. "
           "It highlights which positions tend to commit more fouls or receive more cards. The heatmap shows that, on average, "
          f"forwards commit the most fouls, defenders receive the most yellow cards, and goalkeepers receive the most red cards.")
  
  # Box for tackles per 90 minutes
  df["tackles_per_90"] = df["tackles"] / (df["minutes_played"] / 90)
  df_box = df[df["minutes_played"] > 0]
  
  box = px.box(
      df, x="position", y="tackles_per_90", color="position", points="all",
      title="Distribution of Tackles per 90 Minutes by Position",
      labels={"position": "Position", "tackles_per_90": "Tackles per 90 Minutes"},
      height=500
  )
  
  st.plotly_chart(box, use_container_width = True)
  
  st.write(f"This box plot shows the tackles per 90 minutes for each position. It normalizes defensive performance by playing time,"
           f" highlighting what players are more effective regardless of playing time. Defenders and midfielders tend to have the highest tackles per 90 minutes,"
           f" with medians of .9467801 and 1.243094, respectively. A few individual players stand out, with much larger values, indicating"
           f" exceptional defensive activity.")
