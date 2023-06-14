import streamlit as st
import pandas as pd

st.title('Projeto A2 Programação')
st.header('Raspagem de comentários do Iphone 11 no site da Amazon')
st.caption('Luana Rodrigues de Melo Moura')

df = pd.read_excel('Reviews_iphone11.xlsx')
st.write(df)

import altair as alt

st.header('Gráficos')
st.altair_chart(grafico_interativo_interacoes(df, sentiment, title), use_container_width=True)

