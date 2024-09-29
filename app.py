import pandas as pd
import plotly.express as px
import streamlit as st

# Adicionando um cabeçalho ao aplicativo
st.header("Dashboard de Anúncios de Vendas de Carros")

# Lendo os dados do arquivo CSV
car_data = pd.read_csv("vehicles.csv")

# Criar uma caixa de seleção para o histograma
build_histogram = st.checkbox('Criar um histograma')

# Se a caixa de seleção do histograma for marcada
if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    # Criar um histograma usando Plotly Express
    fig_hist = px.histogram(car_data, x="odometer")
    # Exibir o histograma no Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# Criar uma caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# Se a caixa de seleção do gráfico de dispersão for marcada
if build_scatter:
    st.write('Criando um gráfico de dispersão para odômetro e preço')
    # Criar um gráfico de dispersão usando Plotly Express
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Exibir o gráfico de dispersão no Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
