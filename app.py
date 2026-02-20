import streamlit as st
import pandas as pd

st.title("NWSL Defensive Stats")

# Load CSV
df = pd.read_csv("nwsldefense2023.csv")

st.write("Here are the first 5 rows of the data:")
st.dataframe(df.head())
