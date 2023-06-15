import streamlit as st
import pandas as pd

st.title('Projeto A2 Programação')
st.header('Raspagem de comentários do Iphone 11 no site da Amazon')
st.caption('Luana Rodrigues de Melo Moura')

df = pd.read_excel('Reviews_iphone11.xlsx')
st.write(df)

import altair as alt

st.header('Gráfico de análise de sentimento dos comentários')

contagem_sentimento = df.value_counts('sentiment').reset_index(name = 'contagem')
grafico = alt.Chart(contagem_sentimento).mark_bar().encode(x='sentimento' , y='contagem', color='sentimento)
st.altair_chart(grafico)




