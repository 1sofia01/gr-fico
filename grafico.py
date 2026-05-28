import streamlit as st
import pandas as pd

df = pd.read_csv('TOTAIS_ANUAL.csv')

st.title('Exportações e Importações Anuais do Brasil')
st.caption('Valores em US$ FOB Milhões — Fonte: Secretaria de Comércio Exterior / MDIC')

col_exp = 'Exportações (US$ FOB Milhões)'
col_imp = 'Importações (US$ FOB Milhões)'

import altair as alt

chart_data = df[['Ano', col_exp, col_imp]].melt('Ano', var_name='Tipo', value_name='Valor (US$ FOB Milhões)')

chart = alt.Chart(chart_data).mark_line(point=True, strokeWidth=2.5).encode(
    x=alt.X('Ano:O', title='Ano'),
    y=alt.Y('Valor (US$ FOB Milhões):Q', title='US$ FOB Milhões'),
    color=alt.Color('Tipo:N', scale=alt.Scale(
        domain=[col_exp, col_imp],
        range=['#45AC42', '#F40000']
    ), legend=alt.Legend(title='Legenda')),
    tooltip=['Ano', 'Tipo', alt.Tooltip('Valor (US$ FOB Milhões):Q', format=',.0f')]
).properties(
    height=450
).interactive()

st.altair_chart(chart, use_container_width=True)
