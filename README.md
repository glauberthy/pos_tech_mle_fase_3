
# Tech Challenge: Predição de Satisfação de Passageiros ✈️

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-green?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red?style=for-the-badge&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5.0-orange?style=for-the-badge&logo=scikit-learn)

## 🚀 [Acesse a Demonstração Interativa Aqui!](URL_DO_SEU_DASHBOARD_NO_HF_SPACE)

Este projeto é uma solução completa de Machine Learning, desenvolvida para o Tech Challenge da Pós-Graduação, que aborda o ciclo de vida de um produto de dados de ponta a ponta: desde a coleta e armazenamento de dados via API até o treino de um modelo preditivo e sua implantação numa aplicação interativa.

## 🎥 Apresentação em Vídeo do Projeto

Assista ao vídeo de demonstração que preparamos para avaliação do **Tech Challenge da Pós Tech em Machine Learning Engineering**.  
Clique na imagem abaixo para abrir no YouTube:

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
                               │   (SQLite)    │
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

Uma companhia aérea deseja entender os principais fatores que influenciam a satisfação dos seus clientes para melhorar os seus serviços. Além de entender, a empresa quer uma ferramenta que possa prever a satisfação de um passageiro com base no seu perfil e nas características do voo, permitindo uma tomada de decisão proativa.

---

## 🛠️ Tecnologias Utilizadas

| Área                  | Ferramentas                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| **Backend** | Python, FastAPI, Pydantic, Uvicorn                                                                      |
| **Frontend** | Streamlit                                                                                               |
| **Ciência de Dados** | Pandas, Scikit-learn, Matplotlib, Seaborn, XGBoost, Jupyter Notebook                                    |
| **Banco de Dados** | SQLite                                                                                                  |
| **Qualidade & Testes**| Pytest                                                                                                  |
| **Deploy** | Docker, Hugging Face Spaces                                                                             |

---

## 📊 Resultados do Modelo

O modelo final escolhido foi um `RandomForestClassifier`, que demonstrou um excelente equilíbrio entre performance e tempo de treino.

* **Acurácia Final:** **96%** (validada num conjunto de teste com mais de 25.000 amostras).
* **Métricas Principais:** O modelo é particularmente eficaz em identificar corretamente tanto os clientes satisfeitos quanto os insatisfeitos, com F1-Scores de 0.96 e 0.97, respetivamente.

![Matriz de Confusão do Modelo Final](URL_PARA_A_IMAGEM_DA_MATRIZ_DE_CONFUSAO_AQUI)

---

## 🚀 Como Executar o Projeto Localmente

**Pré-requisitos:** Python 3.12+

**1. Clone o Repositório**
```bash
git clone <URL_DO_SEU_REPOSITORIO_AQUI>
cd nome-do-repositorio
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
* **Otimização de Hiperparâmetros:** Utilizar técnicas como GridSearchCV ou RandomizedSearchCV para encontrar a combinação ótima de parâmetros para o modelo, o que poderia levar a um pequeno ganho de acurácia.
