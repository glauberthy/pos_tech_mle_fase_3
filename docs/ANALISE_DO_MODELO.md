# Relatório de Explicabilidade (XAI) — Classificação de Satisfação de Passageiros
_Gerado em 2025-10-04 16:36_

Resumo das análises **MDI**, **Permutation Importance**, **SHAP (summary, dependence e local)** e **PDP/ICE** realizadas neste notebook.

## Resumo Executivo

- **Experiência digital** lidera: **online_boarding** e **inflight_wifi_service**.
- **Perfil do passageiro** é decisivo: **Business Travel**, **Loyal Customer** e **Classe Business** aumentam satisfação; **Personal Travel**, **Disloyal Customer** e **Classe Economy** reduzem.
- **Serviços de bordo** (conforto, entretenimento, check-in) têm impacto positivo moderado.
- **Baixa relevância**: idade, atrasos e portão de embarque.

## MDI — Mean Decrease in Impurity

Indicador interno do RF (sanity check) agregado por variável original (somando dummies do OHE).

### Top variáveis por MDI (agregado)

| orig                   |   importance |
|:-----------------------|-------------:|
| online_boarding        |    0.15531   |
| inflight_wifi_service  |    0.13724   |
| class                  |    0.120497  |
| type_of_travel         |    0.110474  |
| inflight_entertainment |    0.0593454 |
| customer_type          |    0.0518917 |
| seat_comfort           |    0.0410733 |
| ease_of_online_booking |    0.0393233 |
| leg_room_service       |    0.0328006 |
| flight_distance        |    0.0296853 |

## Permutation Importance

Impacto **real** na performance ao embaralhar uma variável nos **dados de teste**.

Métrica utilizada: **métrica escolhida**.

### Top variáveis por queda média na métrica (importance_mean)

| feature               |   importance_mean |   importance_std |
|:----------------------|------------------:|-----------------:|
| type_of_travel        |         0.184284  |      0.0020149   |
| inflight_wifi_service |         0.123363  |      0.00174848  |
| customer_type         |         0.0815505 |      0.00047396  |
| online_boarding       |         0.0335499 |      0.000940711 |
| checkin_service       |         0.029065  |      0.000667824 |
| baggage_handling      |         0.0267023 |      0.00106877  |
| seat_comfort          |         0.0238102 |      0.000535765 |
| inflight_service      |         0.0218421 |      0.00112163  |
| cleanliness           |         0.0182426 |      0.000563014 |
| class_                |         0.0174631 |      0.00073436  |

### Interpretação destacada
- **type_of_travel** e **inflight_wifi_service** sustentam a acurácia; são drivers fundamentais.
- **food_and_drink** e **arrival_delay_in_minutes** tiveram impacto desprezível.

## SHAP — Summary & Dependence

- Valores SHAP **positivos** → puxam para **satisfied**; **negativos** → **neutral/unsatisfied**.
- **Wifi** e **Online boarding**: notas altas aumentam satisfação; notas baixas reduzem.
- **Type of travel**: *Business* ↑; *Personal* ↓. **Class**: *Business* ↑; *Eco* ↓. **Customer type**: *Loyal* ↑; *Disloyal* ↓.
- **Dependence (online_boarding)**: relação **monotônica crescente**; efeito **mais forte** em *Business Travel*.

## SHAP Local — Waterfall

- Casos corretos explicados por notas baixas em wifi/boarding; falso negativo mostrou supervalorização de problemas digitais.

## PDP/ICE

- **PDP** (tendência média) e **ICE** (variação individual) confirmam efeitos crescentes para boarding e wifi.
- **PDP 2D (boarding × wifi)**: efeito conjunto positivo quando ambos estão altos.

## Limitações e Boas Práticas

- **MDI** é triagem interna (não prova impacto).
- **Permutation** depende da métrica e pode ser afetada por **colinearidade** (considere grupos correlacionados).
- **SHAP** deve ser lido com a **métrica de negócio** e dados recentes (monitorar drift).

## Recomendações de Ação

1) Priorizar melhorias em **online boarding** e **inflight wifi**.
2) Customizar ofertas por **tipo de viagem** e **fidelidade**.
3) Monitorar KPIs de conforto/check-in (impacto moderado, porém consistente).
4) Despriorizar fatores de baixo impacto (idade, atrasos, gate) neste contexto.

