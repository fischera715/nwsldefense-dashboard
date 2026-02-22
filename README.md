# NWSL Defensive Stats 

## Overview
This interactive dashboard analyzes defensive performance for players in the National Women's Soccer League (NWSL). The analysis focuses on tackles, interceptions,
fouls, and other defensive metrics. The goal is to identify key contributors and trends, allowing users to explore how different positions perform 
defensively. 

This was built with **Streamlit** and uses **Plotly** for visualizations.

## Analytical Objective
The purpose of this dashboard is to provide insights into defensive performance across the league by
  1. Comparing defensive metrics across different positions (defender, midfielder, forward, goalkeeper)
  2. Normalizing performance metrics by playing time (per 90 minutes)
  3. Highlighting individual players who contribute most to defensive actions

## Data Source
The data used in this dashboard comes from Kaggle: 

- **2023 NWSL Women’s Soccer League Player Stats**
- Source: [Kaggle dataset by Bree Nguyen](https://www.kaggle.com/datasets/bree/nguyen/2023-nwsl-womens-soccer-player-stats)  
- Format: CSV file

This dataset contains player-level statistics such as games played, minutes played, interceptions, tackles, fouls, and other metrics.

## Data Collection
The data is static and downloaded directly as a CSV file from Kaggle. 
For future sessions, to update dashboard:
  1. Download the latest CSV for the desired season from Kaggle.
  2. Replace the exsting CSV in the repository with the updated file.
  3. Restart the Streamlit app to refresh the visualization.

## Dashboard Features
The dashboard includes 4 main visualizations:
  1. **Bar Plot** - Total tackles per player for the selected position
  2. **Scatter Plot** - Tackles vs. interceptions per player for the selected position. Point size represents minutes played. Regression trendline included.
  3. **Heatmap** - Average fouls and cards by position.
  4. **Box Plots** - Tackles per 90 minutes across positions.

Additional Features: 
- Sidebar filters for **position** and **minimum games played**
- Text analysis describing trends and correlations based on user selection.

## Deployment
- The dashboard is deployed on **[Streamlit Community Cloud](https://share.streamlit.io/)**.
- Public URL: https://nwsldefense-dashboard-8z9tpopbaqzc6k2d9tnqbj.streamlit.app/

## Dependencies
- Python 3.x
- Streamlit
- Pandas
- Plotly
- Statsmodels

Install dependencies via 'requirements.txt'

```bash
pip install -r requirements.txt


