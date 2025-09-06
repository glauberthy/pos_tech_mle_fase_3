## **Cronograma Detalhado: Fase 3 - Modelo em Produção (Dashboard Interativo)**

**Duração Estimada:** 4 dias
**Ferramentas Principais:** Python, Streamlit, Pandas, Joblib, Git, GitHub.

---

**Dia 19 - Quinta-feira (02/10/2025): Estrutura do Dashboard e Carregamento do Modelo**
* **Objetivo do dia:** Montar o esqueleto da aplicação web e garantir que nosso modelo treinado possa ser carregado com sucesso.
* **Bloco 1 (1h):** **Setup do Ambiente e Aplicação Básica.**
    * **Atividade:** Instalar o Streamlit: `pip install streamlit`.
    * **Atividade:** Criar o arquivo `dashboard.py`.
    * **Atividade:** Escrever a estrutura inicial da aplicação com título e texto (`st.title`, `st.header`, `st.write`) e executá-la com `streamlit run dashboard.py` para validar a instalação.
* **Bloco 2 e 3 (2h):** **Carregamento do Modelo e Início da UI.**
    * **Atividade:** Escrever uma função para carregar seu arquivo `pipeline.joblib`. **Dica de especialista:** Use o decorador `@st.cache_resource` nesta função para que o modelo seja carregado na memória apenas uma vez, tornando a aplicação muito mais rápida.
    * **Atividade:** Criar uma barra lateral (`st.sidebar`) para organizar os inputs do usuário. Começar a adicionar os primeiros widgets (ex: `st.selectbox` para `Customer Type` e `Class`).

**Dia 20 - Sexta-feira (03/10/2025): Interface do Usuário e Coleta de Dados**
* **Objetivo do dia:** Finalizar a interface de entrada de dados e garantir que a aplicação consiga capturar todas as informações do usuário.
* **Bloco 1 e 2 (2h):** **Finalização do Formulário de Input.**
    * **Atividade:** Adicionar todos os widgets restantes na barra lateral para cada uma das features que seu modelo precisa para fazer uma previsão (ex: `st.slider` para `Age`, `st.number_input` para `Flight Distance`, etc.).
    * **Atividade:** Organizar os widgets com subtítulos (`st.subheader`) para uma melhor experiência do usuário.
* **Bloco 3 (1h):** **Coleta e Estruturação dos Inputs.**
    * **Atividade:** Adicionar um botão de ação (`st.button('Prever Satisfação')`).
    * **Atividade:** Escrever a lógica que, ao clicar no botão, coleta os valores de todos os widgets e os organiza em um DataFrame do Pandas de uma única linha. **Atenção:** Os nomes das colunas deste DataFrame devem ser *exatamente* os mesmos que o modelo espera.

---

#### **Fim de Semana (04/10 e 05/10):**
* Este é um período crucial. Recomendo fortemente usar algumas horas aqui para garantir que a interface esteja 100% funcional ou para adiantar a lógica de previsão. O prazo está apertado.

---

**Dia 21 - Segunda-feira (06/10/2025): Lógica de Previsão e Apresentação do Resultado**
* **Objetivo do dia:** Implementar a chamada ao modelo e exibir a previsão de forma clara e intuitiva para o usuário.
* **Bloco 1 e 2 (2h):** **Implementação da Lógica de Previsão.**
    * **Atividade:** Dentro da lógica do botão, passar o DataFrame de input para o método `pipeline.predict()` para obter a previsão ("satisfied" ou "neutral or dissatisfied").
    * **Atividade:** (Opcional, mas recomendado) Usar também o método `pipeline.predict_proba()` para obter a probabilidade da previsão, o que adiciona um nível de confiança ao resultado.
* **Bloco 3 (1h):** **Exibição Dinâmica do Resultado.**
    * **Atividade:** Exibir o resultado na tela principal.
    * **Sugestão:** Se a previsão for "satisfied", mostre uma mensagem de sucesso com `st.success()`. Se for "neutral or dissatisfied", use `st.warning()`.
    * **Atividade:** Use `st.metric()` ou `st.progress()` para mostrar a probabilidade da previsão de forma visual e profissional.

**Dia 22 - Terça-feira (07/10/2025): RETA FINAL - PREPARAÇÃO PARA ENTREGA**
* **Objetivo do dia:** Focar exclusivamente em revisar, finalizar e empacotar o projeto para a submissão. **Não desenvolva código novo hoje.**
* **Bloco 1 (1h):** **Revisão Geral e Testes Finais.**
    * **Atividade:** Execute todos os componentes do seu projeto uma última vez: a API, o notebook de treinamento e, principalmente, o dashboard. Garanta que tudo funciona como esperado.
* **Bloco 2 (1h):** **Documentação Final (README.md).**
    * **Atividade:** Atualize o `README.md` no GitHub com a seção final, explicando como executar o dashboard (`streamlit run dashboard.py`). Garanta que todas as instruções, do início ao fim, estejam claras.
* **Bloco 3 (1h):** **Storytelling e Empacotamento.**
    * **Atividade:** Grave um vídeo curto (usando Loom, OBS Studio, etc.) demonstrando o projeto. Siga o roteiro do *storytelling*: apresente o problema de negócio, mostre o dashboard funcionando, e explique brevemente os resultados do modelo.
    * **Atividade:** Crie o arquivo `.txt` final contendo o link para o seu repositório no GitHub e o link para o vídeo no YouTube (ou outra plataforma).
    * **Atividade:** **Submeta o projeto.**

