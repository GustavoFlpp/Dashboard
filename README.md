# Dashboard de Vendas do Supermercado
Este projeto é um dashboard de vendas para um supermercado. 

Linguagem e Bibliotecas<br>
Ele usa Python, Streamlit e Plotly para visualizar dados de vendas.

Estrutura do Projeto<br>
O arquivo principal deste projeto é dashboards.py. Este arquivo lê os dados de vendas, filtra-os com base no mês selecionado e, em seguida, cria várias visualizações dos dados.

Aqui está o que cada visualização mostra:<br>

* Faturamento por dia: Este é um gráfico de barras que mostra as vendas totais para cada dia, dividido por cidade.
* Faturamento por tipo de produto: Este é um gráfico de barras horizontais que mostra as vendas totais para cada linha de produto, dividido por cidade.
* Faturamento por filial: Este é um gráfico de barras que mostra as vendas totais para cada filial.
* Faturamento por tipo de pagamento: Este é um gráfico de pizza que mostra as vendas totais para cada tipo de pagamento.
* Avaliação: Este é um gráfico de barras que mostra a avaliação média para cada cidade.

Como Executar<br>
Para executar este projeto, você precisará ter Python instalado em sua máquina. <br>
Você também precisará instalar os pacotes Python necessários. Você pode fazer isso executando o seguinte comando no seu terminal:

pip install streamlit plotly pandas

Uma vez que os pacotes necessários estão instalados, você pode executar o projeto com o seguinte comando:

streamlit run seu_arquivo.py

Isso iniciará o servidor Streamlit e abrirá o painel no seu navegador web.

Dados<br>
Os dados para este projeto estão armazenados em um DataFrame df. O DataFrame é esperado ter as seguintes colunas: 'Month', 'Date', 'Total', 'City', 'Product line', 'Payment', 'Rating'. Por favor, certifique-se de que sua fonte de dados tem essas colunas para que o painel funcione corretamente.

Referência do Tutorial
Este painel foi criado seguindo o tutorial disponível neste [Link](https://youtu.be/P6E_Kts9pxE?si=6ZU2ilvVCR-Af_mW)

