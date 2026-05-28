import streamlit as st
import pandas as pd

df = pd.read_excel('exportacao_geral.xlsx')
st.bar_chart(df)
