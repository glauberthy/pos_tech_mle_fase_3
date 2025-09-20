### Validação e Métricas:

 - Testar Cross-Validation + GridSearch + Curva de Aprendizado
    - Implementar StratifiedKFold com cross_val_score.
    - Aplicar GridSearchCV para RF e XGB, buscando hiperparâmetros básicos.
    - Gerar curva de aprendizado (learning_curve do sklearn) e interpretar comportamento de treino vs teste.

- Estudar em detalhes 2 métricas
    - Precisão (Precision) e Recall → interpretar fórmulas, casos de uso, trade-off.
    - Criar exemplos práticos de cálculo manual e com classification_report.

- Definir as Métricas do Projeto:
    - Métricas Finais: Defina e justifique quais métricas (como acurácia, F1-score, ROC-AUC) são as mais importantes para o nosso projeto.
    - Guia Rápido: Crie um pequeno guia explicando quando e por que usar cada métrica.

- Detectar Overfitting e Underfitting
    - Comparar métricas em treino vs teste.
    - Usar curva de aprendizado como evidência.
    - Redigir resumo dos riscos de generalização.

### Modelos e Escolha dos Algoritmos

- Comparar Modelos:
    - Revisão Teórica: Estude as diferenças entre o Random Forest (RF) e o XGBoost (XGB), focando em como eles funcionam (Bagging vs. Boosting).
    - Documentação: Anote as vantagens e desvantagens de cada técnica para o nosso caso.

- Extrair Informações dos Modelos:
    - Feature Importance: Use feature_importances_ no modelo Random Forest.
    - Explainability (SHAP): Use plot_importance e os valores SHAP (SHAP values) no modelo XGBoost para entender quais variáveis são mais importantes.
    - Relatórios: Gere gráficos e escreva um resumo das suas descobertas.

- Tradução para Marketing
    - Selecionar top-5 variáveis mais influentes.
    - Relacionar com decisões de negócio (ex.: satisfação aumenta quando bagagem tem nota ≥ 4).
    - Recomendações: Escreva um pequeno relatório de fácil entendimento para o time de marketing. Explique a relação das variáveis com a satisfação do cliente (ex: "Clientes dão nota mais alta quando o processo de bagagem é eficiente").

### Serialização e Produção

- Estudar Serialização: Joblib vs Pickle
    - Testar joblib.dump vs pickle.dump em modelo simples.
    - Comparar performance e tamanho dos arquivos.
    - Justificar escolha de joblib para o projeto.

- Serialização + Versionamento do Pipeline
    - Criar pipeline completo (pré-processador + modelo).
    - Salvar em models/pipeline_rf_v1.joblib.
    - Carregar e validar predict em novos dados.
    - Criar convenção de nomes (v1, v2) e metadados (metadata_rf_v1.json com dataset, data, métricas).
    - Propor fluxo de versionamento (manual ou MLflow).

### Exploração de Dados e Formulário

- Heatmap de Correlações (ydata + seaborn)
    - Gerar relatório automático com ydata-profiling.
    - Produzir heatmap e destacar variáveis correlacionadas.

- Analisar Variáveis Escala 0–5
    - Listar todas as variáveis do dataset com essa escala.
    - Definir quando 0 = ausência de serviço.
    - Documentar decisão para o pipeline.

- Analisar Variável Baggage Handling (1 a 5)
    - Explorar distribuição e estatísticas.
    - Relacionar com satisfação geral dos clientes.

- Benchmark no Kaggle
    - Analisar 2–3 notebooks relevantes.
    - Destacar técnicas e métricas usadas.

- Integração ao Formulário de Demonstração
    - Selecionar variáveis mais influentes (baseado em SHAP/feature importance).
    - Propor layout do formulário destacando campos mais relevantes.