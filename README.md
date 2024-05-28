# :chart_with_upwards_trend: 🛍️ Dashboard de Vendas do Supermercado
Este repositório contém a implementação de um dashboard de vendas de um supermercado. Seu desenvolvimento é para fins didáticos, exemplificando os recursos exigidos pelo Desafio Python do [Projeto Desenvolve](http://projetodesenvolve.com.br).

### Instruções de uso
Este projeto foi desenvolvido usando a versão 3.11.6 do Python. Para execução do script, além da instalação do Python, se certifique que as dependências (em `requirements.txt`) foram devidamente instaladas. <br>
O dashboard pode ser executado através do seguinte comando no terminal:
```
streamlit run dashboards.py
```
A execução iniciará o servidor local do Streamlit e abrirá o dashboard no seu navegador padrão.

### Estrutura do Projeto
| Arquivo   | Descrição |
| :-------- | :------- |
| `dashboards.py`  | Este é o arquivo principal do projeto. Ele contém as funcionalidades do dashboard, entre elas a manipulação de dados com Pandas, criação das visualizações com Plotly, e manipulação de widgets do Streamlit.    |
| `style.css` | A estilização de elementos com CSS. Note que o nome das classes está associada aos nomes de widgets do Streamlit |
| `supermarket_sales.csv`   | Base de dados utilizada no projeto. Maiores detalhes a seguir.   |

### Dados
O arquivo `supermarket_sales.csv` é uma base de dados de vendas de um supermercado, onde cada linha é uma venda realizada. Descreveremos a seguir apenas as colunas relevantes para o nosso painel.
* City: Cidade da filial onde a venda foi realizada.
* Customer type: Tipo do consumidor. Pode assumir dois valores, membro ou não-membro.
* Product line: Tipo do produto. Assume apenas um dentre seis valores: *food and beverages, fashion accessories, home and lifestyle, sports and travel, health and beauty, electronic accessories*
* Total: Valor total da venda, em dólares.
* Date: Data de realização da venda.
* Payment: Modo de pagamento. Pode assumir um entre três valores: *cash, credit card, ewallet*.
* Rating: Avaliação do cliente sobre o atendimento.

### O Projeto Desenvolve
Caso deseje saber mais sobre o Projeto Desenvolve e nossos desafios de programação: <br>
🌐 [Visite nosso site](https://projetodesenvolve.com.br) <br>
:camera: [Conheça o Instagram do Projeto](https://www.instagram.com/projetodesenvolve_br) <br> 

<img src="https://framerusercontent.com/images/flF0huFcLPipFj1TQGVszGKH3Wg.png" height=200>


### Referências
Este painel foi criado seguindo o tutorial do Asimov Academy: [É o fim do Power BI? Criando Dashboard com Python em 15 minutos](https://youtu.be/P6E_Kts9pxE?si=6ZU2ilvVCR-Af_mW)

