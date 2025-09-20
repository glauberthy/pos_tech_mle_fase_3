 Relatório de Classificação Final (test.csv)
 ```csv
                         precision    recall  f1-score   support

neutral / dissatisfied       0.96      0.98      0.97     14573
              satisfied       0.97      0.94      0.96     11403

               accuracy                           0.96     25976
              macro avg       0.96      0.96      0.96     25976
           weighted avg       0.96      0.96      0.96     25976
```

Este relatório mostra o quão bem (segundo a IA) o seu modelo de machine learning está performando na tarefa de classificar a satisfação dos clientes, com base nos dados de teste (`test.csv`).

Aqui está uma explicação de cada métrica:

### **Métricas por Classe**

As classes que o seu modelo está tentando prever são:
* `neutral or dissatisfied` (neutro ou insatisfeito)
* `satisfied` (satisfeito)

Para cada uma dessas classes, temos:

* **Precision (Precisão):** Das vezes que o modelo previu uma classe, quantas vezes ele acertou?
    * **`neutral or dissatisfied`: 0.96** -> Quando o modelo disse que um cliente estava "neutro ou insatisfeito", ele estava correto em 96% das vezes.
    * **`satisfied`: 0.97** -> Quando o modelo disse que um cliente estava "satisfeito", ele estava correto em 97% das vezes.

* **Recall (Revocação ou Sensibilidade):** De todas as instâncias reais de uma classe, quantas o modelo conseguiu encontrar?
    * **`neutral or dissatisfied`: 0.98** -> O modelo identificou corretamente 98% de todos os clientes que estavam *realmente* "neutros ou insatisfeitos".
    * **`satisfied`: 0.94** -> O modelo identificou corretamente 94% de todos os clientes que estavam *realmente* "satisfeitos".

* **F1-Score:** É uma média harmônica entre `precision` e `recall`. É uma ótima métrica para ter uma visão geral do desempenho para uma classe específica, especialmente se houver um desequilíbrio entre as classes. Varia de 0 a 1, onde 1 é o melhor resultado.
    * Ambas as classes têm um F1-Score excelente (0.97 e 0.96), indicando um bom equilíbrio entre precisão e recall.

* **Support:** É o número real de ocorrências de cada classe no conjunto de dados de teste.
    * Havia **14.573** clientes "neutros ou insatisfeitos" e **11.403** clientes "satisfeitos".

### **Métricas Gerais**

* **Accuracy (Acurácia):** De todas as previsões feitas, qual a porcentagem de acertos?
    * **0.96** -> O modelo acertou 96% de todas as previsões, o que é um resultado excelente.

* **Macro Avg (Média Macro):** Calcula a média das métricas (precision, recall, f1-score) para todas as classes, tratando todas as classes com o mesmo peso.

* **Weighted Avg (Média Ponderada):** Calcula a média das métricas, mas ponderada pelo número de instâncias (`support`) em cada classe. É mais útil quando as classes são desbalanceadas.

### **Conclusão (segundo a IA)**

Seu modelo tem um **desempenho excelente**. Ele não só tem uma alta acurácia geral (96%), mas também é muito bom em prever ambas as classes, com altos valores de precisão e recall. Isso significa que o modelo é confiável tanto para identificar clientes satisfeitos quanto para identificar os insatisfeitos.