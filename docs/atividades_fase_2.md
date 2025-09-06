## **Cronograma Detalhado: Fase 2 - Construção do Modelo de Machine Learning**

**Duração Estimada:** 10 dias (incluindo buffer)
**Ferramentas Principais:** Python, Jupyter Notebook, Pandas, Matplotlib, Seaborn, Scikit-learn, Git, GitHub.

---

#### **Semana 1: Análise e Preparação dos Dados**

**Dia 9 - Quinta-feira (18/09/2025): Carregamento e Exploração Inicial (EDA)**
* **Objetivo do dia:** Fazer o primeiro contato com os dados, entendendo sua estrutura, qualidade e principais características.
* **Bloco 1 (1h):** **Configuração do Ambiente de Análise.**
    * **Atividade:** Instalar as bibliotecas de análise: `pip install notebook pandas matplotlib seaborn scikit-learn`.
    * **Atividade:** Iniciar um novo Jupyter Notebook no diretório `/notebooks` do projeto. Carregar o arquivo `train.csv` em um DataFrame do Pandas.
* **Bloco 2 e 3 (2h):** **Inspeção Inicial do DataFrame.**
    * **Atividade:** Realizar a "sondagem" inicial dos dados.
    * **Comandos:** `df.info()` (para ver tipos e nulos), `df.describe()` (para estatísticas de colunas numéricas), `df.isnull().sum()` (para quantificar dados faltantes), `df.columns` (para listar colunas).
    * **Atividade:** Documentar as primeiras descobertas em células de Markdown no notebook (ex: "Identificamos 310 valores nulos na coluna 'Arrival Delay in Minutes'").

**Dia 10 - Sexta-feira (19/09/2025): Análise Exploratória Visual - Parte 1**
* **Objetivo do dia:** Transformar números em gráficos para entender a distribuição dos dados e o perfil dos passageiros.
* **Bloco 1 (1.5h):** **Análise Univariada Numérica.**
    * **Atividade:** Criar histogramas para entender a distribuição das principais variáveis numéricas, como `Age` e `Flight Distance`.
    * **Ferramentas:** Matplotlib/Seaborn (`sns.histplot`, `sns.boxplot`).
* **Bloco 2 (1.5h):** **Análise Univariada Categórica.**
    * **Atividade:** Criar gráficos de barras para visualizar a contagem das variáveis categóricas, como `Gender`, `Customer Type`, `Class` e, mais importante, a variável alvo `satisfaction`.
    * **Ferramentas:** Seaborn (`sns.countplot`).

**Dia 11 - Segunda-feira (22/09/2025): Análise Exploratória Visual - Parte 2**
* **Objetivo do dia:** Aprofundar a análise, buscando relações entre as variáveis e a satisfação do cliente.
* **Bloco 1 e 2 (2h):** **Análise Bivariada.**
    * **Atividade:** Investigar como as características dos passageiros influenciam na satisfação. Criar gráficos de barras agrupados.
    * **Perguntas a responder com gráficos:** Passageiros da `Business class` estão mais satisfeitos? O `Type of Travel` (negócios vs. pessoal) impacta a satisfação?
    * **Ferramentas:** Seaborn (`sns.countplot` com o parâmetro `hue='satisfaction'`).
* **Bloco 3 (1h):** **Análise de Correlação.**
    * **Atividade:** Criar um heatmap de correlação entre todas as variáveis numéricas para identificar se existem relações lineares fortes entre elas.
    * **Ferramentas:** Pandas (`df.corr()`) e Seaborn (`sns.heatmap`).

**Dia 12 - Terça-feira (23/09/2025): Pré-processamento de Dados - Parte 1**
* **Objetivo do dia:** Limpar e preparar o terreno para a construção do modelo.
* **Bloco 1 (1h):** **Tratamento de Dados Faltantes.**
    * **Atividade:** Definir uma estratégia para a coluna `Arrival Delay in Minutes`. Com base na análise, decidir se é melhor preencher com a média, a mediana, ou outro valor. Implementar a decisão.
    * **Ferramentas:** Pandas (`df.fillna()`).
* **Bloco 2 (2h):** **Seleção de Features e Separação.**
    * **Atividade:** Remover colunas que não serão usadas no modelo (ex: `Unnamed: 0`, `id`).
    * **Atividade:** Separar o DataFrame em duas variáveis: `X` (contendo todas as colunas de características) e `y` (contendo apenas a coluna alvo, `satisfaction`).

**Dia 13 - Quarta-feira (24/09/2025): Pré-processamento de Dados - Parte 2**
* **Objetivo do dia:** Transformar os dados para um formato que o algoritmo de Machine Learning consiga entender.
* **Bloco 1, 2 e 3 (3h):** **Construção de um Pipeline de Pré-processamento.**
    * **Atividade:** Usar o `ColumnTransformer` do Scikit-learn para aplicar transformações diferentes em colunas diferentes.
    * **Passos:**
        1.  Identificar as colunas numéricas e categóricas.
        2.  Aplicar `StandardScaler` nas colunas numéricas (para padronizar a escala).
        3.  Aplicar `OneHotEncoder` nas colunas categóricas (para transformá-las em números).
    * **Ferramentas:** Scikit-learn (`ColumnTransformer`, `StandardScaler`, `OneHotEncoder`).

---

#### **Semana 2: Modelagem, Avaliação e Encerramento**

**Dia 14 - Quinta-feira (25/09/2025): Treinamento do Modelo**
* **Objetivo do dia:** Dividir os dados e treinar nosso primeiro modelo preditivo.
* **Bloco 1 (1h):** **Divisão em Treino e Teste.**
    * **Atividade:** Dividir `X` e `y` em conjuntos de treino e teste (ex: 80% para treino, 20% para teste) para que possamos avaliar o modelo de forma justa.
    * **Ferramentas:** Scikit-learn (`train_test_split`).
* **Bloco 2 e 3 (2h):** **Treinamento do Modelo.**
    * **Atividade:** Integrar o `ColumnTransformer` e um algoritmo de ML em um `Pipeline` completo.
    * **Atividade:** Escolher um modelo robusto como `RandomForestClassifier` e treiná-lo com os dados de treino (`pipeline.fit(X_train, y_train)`).
    * **Ferramentas:** Scikit-learn (`Pipeline`, `RandomForestClassifier`).

**Dia 15 - Sexta-feira (26/09/2025): Avaliação de Performance**
* **Objetivo do dia:** Medir o quão bom nosso modelo é em fazer previsões em dados que ele nunca viu.
* **Bloco 1 e 2 (2h):** **Métricas de Classificação.**
    * **Atividade:** Usar o modelo treinado para fazer previsões no conjunto de teste (`pipeline.predict(X_test)`).
    * **Atividade:** Calcular as principais métricas de avaliação: Acurácia, Precisão, Recall e F1-Score. Gerar um `classification_report`.
* **Bloco 3 (1h):** **Análise da Matriz de Confusão.**
    * **Atividade:** Gerar e visualizar uma matriz de confusão para entender os tipos de erros que o modelo está cometendo.
    * **Ferramentas:** Scikit-learn (`classification_report`, `confusion_matrix`, `ConfusionMatrixDisplay`).

**Dia 16 - Segunda-feira (29/09/2025): Salvando o Modelo para Produção**
* **Objetivo do dia:** "Empacotar" nosso modelo treinado para que ele possa ser usado na aplicação final.
* **Bloco 1 e 2 (2h):** **Persistência do Pipeline.**
    * **Atividade:** Salvar o objeto `pipeline` inteiro (que contém tanto o pré-processamento quanto o modelo treinado) em um arquivo.
    * **Ferramentas:** Biblioteca `joblib` (`joblib.dump`).
* **Bloco 3 (1h):** **Teste de Carregamento.**
    * **Atividade:** Em uma nova célula (ou script), carregar o modelo salvo (`joblib.load`) e fazer uma previsão em um único exemplo para garantir que o processo de salvamento/carregamento funcionou.

**Dia 17 - Terça-feira (30/09/2025): Documentação e Versionamento**
* **Objetivo do dia:** Limpar e documentar todo o processo de análise e modelagem para o GitHub.
* **Bloco 1 e 2 (2h):** **Limpeza e Comentários no Notebook.**
    * **Atividade:** Revisar todo o Jupyter Notebook, remover códigos de teste desnecessários, e adicionar explicações claras em células de Markdown para cada etapa da análise. Contar a "história" dos dados.
* **Bloco 3 (1h):** **Commit no GitHub.**
    * **Atividade:** Atualizar o `README.md` com uma nova seção descrevendo a Fase 2.
    * **Atividade:** Fazer o commit do notebook finalizado (`.ipynb`), do modelo salvo (`.joblib`) e do `requirements.txt` atualizado para o repositório.

**Dia 18 - Quarta-feira (01/10/2025): Buffer e Refinamento**
* **Objetivo do dia:** Dia de segurança para refinar o modelo ou a análise.
* **Bloco 1, 2 e 3 (3h):** **Atividades Flexíveis.**
    * **Opção 1 (Refinamento):** Tentar um algoritmo diferente (ex: `XGBoost`) para ver se consegue uma performance melhor.
    * **Opção 2 (Ajuste de Hiperparâmetros):** Pesquisar e aplicar técnicas como `GridSearchCV` para encontrar os melhores parâmetros para o seu modelo.
    * **Opção 3 (Revisão):** Revisar todo o trabalho da fase, garantindo que a documentação está clara e o código é legível.

---

Com o término desta fase, você terá o coração do seu projeto pronto: um modelo de Machine Learning treinado, avaliado e salvo, pronto para ser colocado em produção.


---

Ok, vamos para a reta final. A inteligência do projeto está construída; agora, precisamos dar vida a ela e prepará-la para a apresentação.

Com a data de entrega final (07/10) se aproximando, o cronograma para esta próxima fase será intenso e focado em entregar um resultado funcional e polido. A partir de agora, também planejaremos as atividades de documentação e apresentação em paralelo.

---
