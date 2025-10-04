---
title: Demo Satisfacao Passageiros
emoji: ✈️
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# Tech Challenge: Predição de Satisfação de Passageiros ✈️

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red?style=for-the-badge&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5.0-orange?style=for-the-badge&logo=scikit-learn)

## 🚀 [Acesse a Demonstração Interativa Aqui!](https://huggingface.co/spaces/glauberthy/analise-satisfacao-passageiros)

Este projeto é uma solução completa de Machine Learning, desenvolvida para o Tech Challenge da Pós-Graduação, que aborda o ciclo de vida de um produto de dados de ponta a ponta: desde a coleta e armazenamento de dados via API até o treino de um modelo preditivo e sua implantação em uma aplicação interativa para o usuário final.

## 🎥 Apresentação em Vídeo do Projeto

Assista à apresentação completa do projeto, onde detalhamos o problema de negócio, a arquitetura da solução, a análise de dados e a demonstração da aplicação em funcionamento. Este vídeo cumpre o requisito de **storytelling e vídeo explicativo** do desafio.

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank">
  <img src="https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg" alt="Apresentação do Projeto - Tech Challenge Pós Tech MLE" width="400"/>
</a>


## 🏛️ Arquitetura da Solução

O projeto foi desenhado com uma arquitetura desacoplada, separando a interface do utilizador (frontend) da lógica de negócio e do modelo (backend), o que é uma prática padrão em sistemas de produção.

```
┌──────────────────┐      ┌─────────────────────────┐      ┌────────────────────┐
│                  │      │                         │      │                    │
│   Dashboard      │      │     API (FastAPI)       │      │   Modelo de ML     │
│   (Streamlit)    ├─────►│                         ├─────►│   (.joblib)        │
│                  │      │ 1. Recebe dados         │      │                    │
└──────────────────┘      │ 2. Serve a predição     │      └────────────────────┘
                          │ 3. Salva no banco       │
                          └────────────┬────────────┘
                                       │
                                       ▼
                               ┌───────────────┐
                               │               │
                               │Banco de Dados │
                               │               │
                               │               │
                               └───────────────┘
```

### 📁 Estrutura do Projeto

A estrutura de arquivos foi organizada para separar claramente as responsabilidades de cada componente do sistema.

```
.
├── 📂 api/                   # Módulos do backend (API FastAPI)
│   ├── 📄 database.py        # Lógica de interação com o banco de dados
│   ├── 📄 main.py            # Endpoints da API (roteamento)
│   └── 📄 models.py          # Modelos de dados Pydantic
│
├── 📂 data/                   # Conjuntos de dados originais
│   ├── 📄 test.csv
│   └── 📄 train.csv
│
├── 📂 models/                 # Artefactos do modelo treinado
│   └── 📦 modelo_satisfacao_passageiros_v1.joblib
│
├── 📂 notebooks/              # Análise exploratória e treino do modelo
│   └── 📓 analise_exploratoria.ipynb
│
├── 📂 tests/                  # Testes automatizados da API
│   └── 📄 test_api.py
│
├── 🖥️ app.py                  # Arquivo principal da aplicação Streamlit (Frontend)
├── 🗃️ passageiros.db         # Banco de dados SQLite
├── ⚙️ pytest.ini             # Arquivo de configuração do Pytest
├── 📋 README.md               # Documentação do projeto
└── 📦 requirements.txt      # Lista de dependências Python
```

---

## 🎯 Problema de Negócio

Uma companhia aérea busca transformar sua abordagem de reativa para proativa na gestão da satisfação do cliente. O objetivo é parar de apenas analisar o passado e começar a **prever o futuro**, identificando os passageiros com alta probabilidade de insatisfação **antes** que ela ocorra. Para isso, é necessário não apenas um modelo preditivo acurado, mas também um entendimento claro de **quais fatores** mais impactam a experiência do cliente para guiar ações estratégicas e otimizar investimentos em serviços.

---

## 🛠️ Tecnologias Utilizadas

| Área                  | Ferramentas                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| **Backend** | Python, FastAPI, Pydantic, Uvicorn                                                                      |
| **Frontend** | Streamlit                                                                                               |
| **Ciência de Dados** | Pandas, Scikit-learn, Matplotlib, Seaborn, XGBoost, SHAP, Jupyter Notebook                                    |
| **Banco de Dados** | SQLite                                                                                                  |
| **Qualidade & Testes**| Pytest                                                                                                  |
| **Deploy** | Docker, Hugging Face Spaces                                                                             |

---

## 📊 Performance e Insights do Modelo

O modelo final escolhido foi um `RandomForestClassifier` otimizado com GridSearchCV, que demonstrou um desempenho excelente e robusto.

* **Acurácia Geral:** **96%**.
* **Score ROC-AUC:** **0.97**, o que indica uma capacidade quase perfeita de discriminar entre clientes satisfeitos e insatisfeitos. Esta métrica valida a alta performance do modelo de forma independente do leve desbalanceamento de classes.

![Matriz de Confusão do Modelo Final](./docs/imagens/Visualizando_a_Matriz_de_Confusao_Final_(test.csv).png)
''
### Principais Fatores de Satisfação (Insights de XAI)

A análise de explicabilidade (XAI) revelou os principais drivers por trás das previsões do modelo:

* **Experiência Digital Lidera:** `online_boarding` e `inflight_wifi_service` são os fatores de maior impacto na satisfação do cliente.
* **Perfil do Passageiro é Decisivo:** O tipo de viagem (`Business Travel` vs. `Personal Travel`), a fidelidade do cliente (`Loyal Customer`) e a classe do voo são preditores-chave.
* **Serviços a Bordo Têm Impacto Moderado:** Conforto do assento (`seat_comfort`) e entretenimento a bordo (`inflight_entertainment`) são importantes, mas com um peso menor que os fatores digitais e o perfil do passageiro.
* **Baixa Relevância:** Idade, atrasos no voo e localização do portão de embarque mostraram ter pouco impacto nas previsões do modelo.

---
 **Para uma análise técnica aprofundada** sobre a importância das variáveis, impacto com SHAP e dependência parcial, **[consulte o Relatório Completo de Explicabilidade (XAI) aqui](./docs/ANALISE_DO_MODELO.md)**.
---

## 🚀 Como Executar o Projeto Localmente

**Pré-requisitos:** Python 3.12+

**1. Clone o Repositório**
```bash
git clone https://github.com/glauberthy/pos_tech_mle_fase_3
cd pos_tech_mle_fase_3
```

**2. Crie e Ative o Ambiente Virtual e Instale as Dependências**
```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
venv\Scripts\activate
# Ative o ambiente (macOS/Linux)
source venv/bin/activate

# Instale as bibliotecas
pip install -r requirements.txt
```

**3. Execute a API (Backend)**
*Num primeiro terminal, execute:*
```bash
uvicorn api.main:app --reload
```
A API estará disponível em `http://127.0.0.1:8000`.

**4. Execute o Dashboard (Frontend)**
*Num segundo terminal, execute:*
```bash
streamlit run app.py
```
A aplicação abrirá no seu navegador em `http://127.0.0.1:8501`.

---

## 🤔 Decisões de Design e Trade-offs

* **Escolha do Banco de Dados (SQLite vs. PostgreSQL/MySQL):** Para este projeto, foi utilizado o SQLite devido à sua simplicidade e portabilidade. Por ser um banco de dados baseado em arquivo, ele não exige a configuração de um servidor e está perfeitamente adequado para o desenvolvimento, prototipagem e para o escopo deste desafio. Numa aplicação de produção real, com múltiplos usuários e um volume maior de dados, a escolha ideal seria um sistema de banco de dados como **PostgreSQL** ou **MySQL**, provavelmente containerizado com **Docker** para garantir um ambiente de deploy consistente e escalável.

* **Armazenamento do Modelo (Git vs. Git LFS):** Para este projeto, o artefacto do modelo (`.joblib`) foi incluído diretamente no repositório para simplificar a avaliação. Numa implementação de produção, a melhor prática seria utilizar uma ferramenta como **Git LFS (Large File Storage)** para gerir arquivos binários grandes, evitando sobrecarregar o repositório Git.

* **Escolha do Modelo (RandomForest vs. XGBoost):** Foram testados os modelos `RandomForestClassifier` e `XGBoost`. Como ambos apresentaram uma performance quase idêntica (96% de acurácia), optou-se pelo RandomForest devido à sua simplicidade e robustez, que já atendiam plenamente aos requisitos do problema.

---

## 🔮 Próximos Passos

* **Pipeline de Retreino:** Implementar um pipeline automatizado que retreine o modelo periodicamente com os novos dados coletados pela API.
* **Monitoramento:** Criar um segundo dashboard para monitorizar a performance do modelo em produção e detetar "data drift".
* **Testes A/B:**  Implementar as recomendações de ação (ex: melhorias direcionadas ao Wi-Fi) e medir o impacto real na satisfação do cliente através de testes A/B para validar as hipóteses geradas pelo modelo.
