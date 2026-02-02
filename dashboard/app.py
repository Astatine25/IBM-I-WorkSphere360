import streamlit as st
import pandas as pd

st.title("WorkSphere360 – AI Workforce Dashboard")

df = pd.read_csv("final_ai_output.csv")

st.metric("High Burnout Risk Employees", df[df.burnout_risk > 0.7].shape[0])
st.bar_chart(df.groupby("department")["burnout_risk"].mean())
st.dataframe(df)
