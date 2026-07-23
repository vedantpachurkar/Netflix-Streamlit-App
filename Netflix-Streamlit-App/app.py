import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\HP\\Code\\netflix_titles.csv")

st.title("🎬 Netflix Dataset Explorer")

st.write("### Dataset Preview")
st.dataframe(df.head())

st.write("### Dataset Shape")
st.write(df.shape)

st.write("### Content Type Distribution")
st.bar_chart(df["type"].value_counts())

country = st.selectbox(
    "Select Country",
    ["All"] + sorted(df["country"].dropna().unique().tolist())
)

if country != "All":
    filtered = df[df["country"] == country]
    st.write(filtered)