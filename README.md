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
* **Pytest:** Para os testes automatizados (unitários e de integração).

### 🚀 Como Executar a Fase 1

**1. Clone o Repositório**
```bash
git clone <URL_DO_SEU_REPOSITORIO_AQUI>
cd tech_challenge
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

**4. Execute a API**
O banco de dados `passageiros.db` e a tabela serão criados automaticamente na primeira inicialização.
```bash
uvicorn api.main:app --reload
```
A API estará disponível em `http://127.0.0.1:8000`. A documentação interativa para testes está em `http://127.0.0.1:8000/docs`.

**5. Execute os Testes Automatizados**
Para verificar a integridade da API, execute os testes:
```bash
pytest
```