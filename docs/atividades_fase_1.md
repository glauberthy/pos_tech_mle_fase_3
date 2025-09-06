## **Cronograma Detalhado: Fase 1 - Coleta e Armazenamento de Dados via API**

**Duração Estimada:** 8 dias (incluindo buffer)
**Ferramentas Principais:** Python, FastAPI, Pydantic, Uvicorn, SQLite, Git, GitHub.

---

#### **Semana 1: Construção e Integração**

**Dia 1 - Segunda-feira (08/09/2025): Setup do Ambiente e Estrutura do Projeto**
* **Objetivo do dia:** Preparar todo o alicerce para o desenvolvimento, garantindo um ambiente de trabalho limpo e versionado.
* **Bloco 1 (1h):** **Configuração do Ambiente Virtual e Dependências.**
    * **Atividade:** Criar um ambiente virtual (`venv`) para isolar as dependências do projeto.
    * **Comandos:** `python -m venv venv`, `source venv/bin/activate` (ou `venv\Scripts\activate` no Windows).
    * **Ferramentas:** Python, venv.
    * **Atividade:** Instalar as bibliotecas iniciais: FastAPI e Uvicorn (servidor para a API).
    * **Comandos:** `pip install fastapi "uvicorn[standard]"`
* **Bloco 2 (1h):** **Estruturação de Diretórios e Controle de Versão.**
    * **Atividade:** Criar a estrutura de pastas do projeto (ex: `/api`, `/notebooks`, `/data`).
    * **Atividade:** Iniciar o repositório Git, criar um arquivo `.gitignore` (para ignorar arquivos como `__pycache__` e `venv`) e fazer o primeiro commit.
    * **Ferramentas:** Git.
* **Bloco 3 (1h):** **Criação do "Hello World" da API.**
    * **Atividade:** Criar o arquivo `main.py` dentro da pasta `/api` com um endpoint raiz (`@app.get("/")`) que retorna uma mensagem simples.
    * **Objetivo:** Validar que a instalação do FastAPI e Uvicorn foi bem-sucedida e que o servidor está rodando.
    * **Ferramentas:** FastAPI, Uvicorn.

**Dia 2 - Terça-feira (09/09/2025): Modelagem dos Dados de Entrada**
* **Objetivo do dia:** Definir um contrato claro para os dados que a API irá receber, garantindo a qualidade e o formato das informações.
* **Bloco 1 (1h):** **Análise do Schema dos Dados.**
    * **Atividade:** Abrir o arquivo `train.csv` e mapear todas as colunas e seus tipos de dados (texto, inteiro, decimal).
    * **Atenção:** Notar que a coluna `Class` é uma palavra-chave reservada em Python. Decidir renomeá-la para `flight_class` no nosso modelo de dados.
* **Bloco 2 e 3 (2h):** **Implementação do Modelo Pydantic.**
    * **Atividade:** Dentro de `main.py`, criar uma classe `Passageiro(BaseModel)` usando a biblioteca Pydantic. Adicionar todos os campos mapeados no bloco anterior como atributos da classe, com seus respectivos tipos (ex: `age: int`, `gender: str`).
    * **Ferramentas:** Pydantic (parte do FastAPI).

**Dia 3 - Quarta-feira (10/09/2025): Desenvolvimento do Endpoint de Coleta**
* **Objetivo do dia:** Criar o "portão de entrada" que receberá os dados dos passageiros.
* **Bloco 1 e 2 (2h):** **Desenvolvimento do Endpoint POST.**
    * **Atividade:** Criar um novo endpoint `@app.post("/adicionar_passageiro")` que recebe um objeto do tipo `Passageiro` (a classe Pydantic que você criou).
    * **Atividade:** Inicialmente, a função deste endpoint irá apenas imprimir os dados recebidos no console para fins de teste.
* **Bloco 3 (1h):** **Teste de Validação Automática.**
    * **Atividade:** Iniciar o servidor Uvicorn e acessar a documentação automática (`/docs`). Usar a interface do Swagger UI para enviar um JSON de teste para o seu novo endpoint e verificar se os dados são impressos corretamente no terminal.
    * **Ferramentas:** FastAPI Docs (Swagger UI).

**Dia 4 - Quinta-feira (11/09/2025): Configuração do Banco de Dados**
* **Objetivo do dia:** Preparar o local onde os dados coletados serão armazenados de forma persistente.
* **Bloco 1 (1h):** **Desenho da Tabela SQL.**
    * **Atividade:** Escrever a instrução `CREATE TABLE` em SQL para a tabela `passageiros`. As colunas devem corresponder exatamente aos campos do modelo Pydantic.
    * **Ferramentas:** SQL.
* **Bloco 2 e 3 (2h):** **Criação de um Script de Inicialização do Banco.**
    * **Atividade:** Dentro do `main.py` (ou em um arquivo separado), criar uma função `init_db()` que se conecta a um banco de dados SQLite e executa o comando `CREATE TABLE` que você desenhou.
    * **Objetivo:** Garantir que a tabela exista antes que a API tente inserir dados nela.
    * **Ferramentas:** Python (biblioteca `sqlite3`).

**Dia 5 - Sexta-feira (12/09/2025): Integração Final da API com o Banco de Dados**
* **Objetivo do dia:** Conectar as duas pontas: fazer com que os dados que chegam na API sejam efetivamente salvos no banco de dados.
* **Bloco 1, 2 e 3 (3h):** **Implementação da Lógica de Inserção.**
    * **Atividade:** Modificar o endpoint `@app.post("/adicionar_passageiro")`.
    * **Passos:**
        1.  Remover a linha `print()`.
        2.  Adicionar o código para conectar-se ao banco de dados SQLite.
        3.  Escrever a instrução `INSERT INTO passageiros ...` usando os dados recebidos do objeto `passageiro`.
        4.  Implementar `try...except` para tratamento de erros durante a inserção.
        5.  Confirmar (`commit`) a transação e fechar a conexão.
        6.  Retornar uma mensagem de sucesso em JSON.
