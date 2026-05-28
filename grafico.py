import streamlit as st
import pandas as pd

df = pd.read_excel('exportacao_geral.xlsx')
st.title('Exportação por Estado (UF)')

st.bar_chart(
  df,
  x='UF do Produto'
  y =['2021 - Valor US$ FOB', '2022 - Valor US$ FOB']
)
