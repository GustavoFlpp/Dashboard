import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Define a configuração da página como "wide"
st.set_page_config(
    page_title="Supermercado",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Abre o arquivo "styles.css" em modo de leitura e o associa à variável 'f'
with open("styles.css") as f:
    # Utiliza o componente de markdown do Streamlit para inserir o conteúdo CSS diretamente no aplicativo da web
    # O conteúdo é inserido entre tags <style> para aplicação correta do CSS
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

## Lê o arquivo CSV e cria um DataFrame
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

## Ajustes na base de dados
df["Date"] = pd.to_datetime(df["Date"]) # Converte a coluna "Date" para o formato datetime
df = df.sort_values("Date") # Ordena o DataFrame por data
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month)) # Coluna "Month" com base no ano e mês da data

## Elementos na sidebar
# Cria e aplica filtros de interatividade
with st.sidebar:
    st.title('Supermercado 🛍️')

    selected_month = st.selectbox("Mês", df["Month"].unique()) # Permite ao usuário selecionar um mês na barra lateral
    df_filtered = df[df["Month"] == selected_month]

    unique_products = df["Product line"].unique()
    selected_products = st.multiselect('Tipo de produto', unique_products, default=unique_products[:2])
    df_filtered = df_filtered[df_filtered["Product line"].isin(selected_products)]

    selected_membros = st.toggle('Apenas clientes membros', value=False)
    df_filtered = df_filtered if not selected_membros else df_filtered[df_filtered["Customer type"] == 'Member']

    st.markdown("Autor: Gustavo Felippe Barbosa") # Exibe o nome "Gustavo Felippe Barbosa" na barra lateral


### Primeira linha: métricas numéricas
cols1= st.columns(3)
cols1[0].metric('Faturamento total', f'${df_filtered["Total"].sum():.2f}')
cols1[1].metric('Número de vendas', len(df_filtered))
cols1[2].metric('Avaliação média',  f'{df_filtered["Rating"].mean():.1f}')

### Segunda linha: primeiro grupo de plots - faturamento por filial
st.markdown('''#### Faturamento por filial''')
cols2 = st.columns((2, 3), gap='medium')
with cols2[0]:
    city_total = df_filtered.groupby(["City", 'Customer type'])[["Total"]].sum().reset_index()
    fig_city = px.bar(city_total, x="City", y="Total",color="City", facet_col='Customer type', 
                      color_discrete_sequence=['#265C4B', '#589A8D','#8FC1B5'])
    fig_city.update_layout(yaxis_title=None, showlegend=False)
    fig_city.update_xaxes(categoryorder='array', categoryarray=sorted(df_filtered["City"].unique()))
    st.plotly_chart(fig_city, use_container_width=True)

with cols2[1]:
    fig_perday = px.area(df_filtered, x='Date', y='Total', color='City', facet_row='City', 
                         category_orders={"City": sorted(df_filtered["City"].unique())}, 
                         color_discrete_sequence=['#388A70', '#69B8A8','#A5DEBB'])
    fig_perday.for_each_annotation(lambda a: a.update(text=''))
    fig_perday.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.01,xanchor='left'), legend_title=None)
    st.plotly_chart(fig_perday, use_container_width=True)

### Terceira linha: segundo grupo de plots - faturamento por produto, tipo de pagamento, avaliações
st.markdown('''#### Métricas secundárias''')
cols3 = st.columns((2, 1, 2))

with cols3[0]:
    # Cria um gráfico de barras do faturamento por tipo de produto, dividido por cidade
    products_total = df_filtered.groupby(['Product line', 'City'])['Total'].sum().reset_index()
    fig_prod = px.bar(products_total, x="Total", y='Product line', color="City", 
                      title="Faturamento por tipo de produto", orientation="h", 
                      color_discrete_sequence=['#265C4B', '#589A8D','#8FC1B5'])  # Cores em formato hexadecimal
    fig_prod.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor='left'), 
                           legend_title=None, yaxis_title=None)
    st.plotly_chart(fig_prod, use_container_width=True)


with cols3[1]:
    # Cria um gráfico de pizza do faturamento por tipo de pagamento
    fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Tipos de pagamento",
                      color_discrete_sequence=['#503A5E', '#323050', '#21445B'])
    fig_kind.update_traces(textposition='inside', textinfo='percent+label')
    fig_kind.update_layout(showlegend=False)
    # Exibe o gráfico na quarta coluna
    st.plotly_chart(fig_kind, use_container_width=True)

with cols3[2]:
    fig_hist = px.histogram(df_filtered, x="Rating",  color="City", marginal="box", title='Avaliações',
                            category_orders={'City': sorted(df_filtered["City"].unique())}, color_discrete_sequence=['#265C4B', '#589A8D','#8FC1B5'])
    fig_hist.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.01,xanchor='left'), legend_title=None)
    # fig_hist.update_layout(showlegend=False)
    st.plotly_chart(fig_hist, use_container_width=True)