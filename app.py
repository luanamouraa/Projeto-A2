import streamlit as st
import pandas as pd

df = pd.read_excel('Reviews_iphone.xlsx')
st.write(df)

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["positivo", "neutro", "negativo"])

st.bar_chart(chart_data)
