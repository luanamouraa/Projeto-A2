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

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["positivo", "neutro", "negativo"])

st.bar_chart(chart_data)
