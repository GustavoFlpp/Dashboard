import streamlit as st
import pandas as pd
import plotly.express as px


# Define a configuração da página como "wide"
st.set_page_config(layout="wide")

# Abre o arquivo "styles.css" em modo de leitura e o associa à variável 'f'
with open("styles.css") as f:
    # Lê o conteúdo do arquivo CSS e o armazena em uma string
    css_content = f.read()
    # Utiliza o componente de markdown do Streamlit para inserir o conteúdo CSS diretamente no aplicativo da web
    # O conteúdo é inserido entre tags <style> para aplicação correta do CSS
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)


# Lê o arquivo CSV e cria um DataFrame
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# Converte a coluna "Date" para o formato datetime
df["Date"] = pd.to_datetime(df["Date"])

# Ordena o DataFrame por data
df = df.sort_values("Date")

# Cria uma nova coluna "Month" com base no ano e mês da data
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Permite ao usuário selecionar um mês na barra lateral
month = st.sidebar.selectbox("Mês", df["Month"].unique())

# Exibe o nome "Gustavo Felippe Barbosa" na barra lateral
st.sidebar.markdown("Gustavo Felippe Barbosa")

# Filtra o DataFrame baseado no mês selecionado
df_filtered = df[df["Month"] == month]

# Cria duas colunas na interface do Streamlit
col1, col2 = st.columns(2)
# Cria três colunas na interface do Streamlit
col3, col4, col5 = st.columns(3)

# Cria um gráfico de barras do faturamento por dia, dividido por cidade
fig_date = px.bar(df_filtered, x="Date", y="Total",color="City", title="Daily billing")
# Exibe o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)

# Cria um gráfico de barras do faturamento por tipo de produto, dividido por cidade
fig_prod = px.bar(df_filtered, x="Date", y="Product line",color="City", title="Billing by product type", orientation="h")
# Exibe o gráfico na segunda coluna
col2.plotly_chart(fig_prod, use_container_width=True)

# Agrupa o DataFrame filtrado por cidade e soma o total de vendas
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
# Cria um gráfico de barras do faturamento por filial
fig_city = px.bar(city_total, x="City", y="Total",color="City", title="Billing by branch")
# Exibe o gráfico na terceira coluna
col3.plotly_chart(fig_city, use_container_width=True)

# Cria um gráfico de pizza do faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Billing by payment")
# Exibe o gráfico na quarta coluna
col4.plotly_chart(fig_kind, use_container_width=True)

# Agrupa o DataFrame filtrado por cidade e calcula a média das avaliações
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
# Cria um gráfico de barras da avaliação por cidade
fig_rating = px.bar(df_filtered, x="City", y="Rating", color="City", title="Evaluation")
# Exibe o gráfico na quinta coluna
col5.plotly_chart(fig_rating, use_container_width=True)