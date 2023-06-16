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
grafico = alt.Chart(contagem_sentimento).mark_bar().encode(x='sentiment' , y='contagem')
st.altair_chart(grafico) 


from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='sentiment',
    y='contagem'
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)




