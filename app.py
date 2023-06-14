import streamlit as st
import pandas as pd

st.title('Projeto A2 Programação')
st.header('Raspagem de comentários do Iphone 11 no site da Amazon')
st.caption('Luana Rodrigues de Melo Moura')

df = pd.read_excel('Reviews_iphone.xlsx')
st.write(df)



import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('Gráficos')
st.altair_chart(grafico_interativo_interacoes(df, marca_sidebar, ano_sidebar), use_container_width=True)

