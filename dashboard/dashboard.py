import streamlit as st
import pandas as pd

st.set_page_config("WorkSphere360 Dashboard")

st.title("WorkSphere360 AI Dashboard")

df = pd.DataFrame({
    "Employee": ["A", "B"],
    "Burnout Risk": [0.8, 0.3]
})

st.dataframe(df)

st.bar_chart(df.set_index("Employee"))
