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


import pandas as pd
import matplotlib.pyplot as plt
     

df = pd.read_excel('Reviews_iphone11.xlsx')
texto = ''
for linha in df['text']:
    print(linha)
    texto += linha + ' '
     

print(df[['text']])
     

from wordcloud import WordCloud
     

wordcloud = WordCloud()
wordcloud.generate_from_text(texto)

stopwords = []
arqstop = open('stopwords.txt')

for linha in arqstop:
    stopwords.append(linha.replace('\n', '').replace(' ' , ''))
    stopwords += ['linha', 'in', 'and', 'the', 'n', 'pp', 'of', 'op']

linha = "exemplo"
lista = linha.split(' ')
nova_lista = []
nova_linha = ''

for palavra in lista:
     if len(palavra) > 3:
        nova_lista.append(palavra)
        nova_linha = ' '
        nova_linha += palavra + ' '
wordcloud = WordCloud(stopwords=stopwords)

wordcloud.generate_from_text(texto)
plt.figure(figsize = (15, 10))
plt.imshow( wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.show() 
st.set_option('deprecation.showPyplotGlobalUse', False) 
st.pyplot()
