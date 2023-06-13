import streamlit as st
import pandas as pd

df = pd.read_excel('Reviews_iphone.xlsx')
st.write(df)
