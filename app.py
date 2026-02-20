import streamlit as st
import pandas as pd

st.title("NWSL Defensive Stats")

# Load CSV
df = pd.read_csv("2023_nwsl_full.csv")

st.write("Here are the first 5 rows of the data:")
st.dataframe(df.head())
