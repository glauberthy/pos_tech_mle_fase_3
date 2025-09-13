# Tech Challenge: Predição de Satisfação de Passageiros Aéreos

Este projeto é uma solução completa de Machine Learning desenvolvida como parte do Tech Challenge da Pós-Graduação. O objetivo é criar um sistema que coleta dados de passageiros, treina um modelo de ML para prever a satisfação e disponibiliza essas previsões através de um dashboard interativo.

## Fase 1: API de Coleta de Dados

Nesta fase, foi construída uma API robusta com FastAPI para coletar e armazenar os dados dos passageiros. A API inclui validação de dados em tempo real e testes automatizados para garantir a qualidade e a integridade dos dados.

### 🛠️ Tecnologias Utilizadas na Fase 1

* **Python 3.12+**
* **FastAPI:** Para a construção da API.
* **Pydantic:** Para validação e modelagem dos dados.
* **Uvicorn:** Como servidor para a API.
* **SQLite:** Para o armazenamento dos dados.
* **Pytest:** Para os testes automatizados (de integração).

---

## Fase 2: Construção do Modelo de Machine Learning

Nesta fase, foi realizado todo o ciclo de vida de um modelo de classificação, desde a análise exploratória dos dados até o treino e a validação final. O objetivo foi construir um modelo capaz de prever a satisfação de um passageiro com alta acurácia.

### 🛠️ Tecnologias Utilizadas na Fase 2

* **Jupyter Notebook:** Para a análise interativa e experimentação.
* **Pandas:** Para manipulação e pré-processamento dos dados.
* **Matplotlib & Seaborn:** Para a visualização de dados.
* **Scikit-learn:** Para a construção do pipeline de pré-processamento e treino do modelo (`RandomForestClassifier`).
* **Joblib:** Para salvar o objeto do modelo treinado.

### 📊 Resultados

O modelo final (`RandomForestClassifier`) alcançou uma **acurácia de 96%** no conjunto de teste dedicado (`test.csv`), demonstrando excelente capacidade de generalização.

---

## 🚀 Como Executar o Projeto

**1. Clone o Repositório**

```bash
git clone <URL_DO_SEU_REPOSITORIO_AQUI>
cd nome-do-repositorio
```

**2. Crie e Ative o Ambiente Virtual**

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as Dependências**

```bash
pip install -r requirements.txt
```

**4. Execute a API (Fase 1)**

O banco de dados `passageiros.db` e a tabela serão criados automaticamente na primeira inicialização.

```bash
uvicorn api.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`. A documentação interativa para testes está em `http://127.0.0.1:8000/docs`.

**5. Execute os Testes Automatizados da API**

Para verificar a integridade da API, execute os testes:

```bash
pytest
```

**6. Explore a Análise e o Treinamento do Modelo (Fase 2)**

Para ver o processo de análise de dados e treinamento do modelo, inicie o Jupyter Notebook:

```bash
jupyter notebook
```

Em seguida, navegue até a pasta `/notebooks` e abra o ficheiro `analise_exploratoria.ipynb`.

## Storytelling
```text
"É uma excelente oportunidade para, no seu vídeo de storytelling, você mencionar esta decisão: "Para este projeto, o artefacto do modelo foi incluído diretamente no repositório para simplificar a avaliação, mas numa implementação de produção, a melhor prática seria utilizar uma ferramenta como o Git LFS para gerir ficheiros binários grandes."
```