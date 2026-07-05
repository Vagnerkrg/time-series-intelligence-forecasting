<h1 align="center"> 
  🚀 Time Series Intelligence System
</h1>

<h3 align="center">
  “Sistema de Machine Learning em nível empresarial para previsão de demanda e inteligência em séries temporais.”
</h3>

<p align="center">
  <img src="https://media.giphy.com/media/juua9i2c2fA0AIp2iq/giphy.gif" width="120"/>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Forecasting%20System-orange?style=for-the-badge)
![Time Series](https://img.shields.io/badge/Time%20Series-Advanced-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production%20Pipeline-green?style=for-the-badge)
![Stage](https://img.shields.io/badge/Stage-Modeling%20%26%20Evaluation-black?style=for-the-badge)

</p>

<p align="center">
  <i>“Construindo inteligência em nível de produção para previsão, detecção de anomalias e insights de negócio.”</i>
</p>

## 🧠 Visão Geral

Sistema completo de análise e previsão de séries temporais aplicado a um cenário de demanda real.

O objetivo é transformar dados históricos em previsões confiáveis, simulando um ambiente real de Data Science aplicado a negócios.

---

## 🎯 Objetivo do Projeto

- Analisar comportamento histórico de demanda
- Criar baseline de previsão
- Implementar modelos estatísticos e de Machine Learning para forecasting
- Avaliar performance com métricas reais (MAE e RMSE)
- Comparar diferentes abordagens de modelagem
- Disponibilizar um sistema interativo em produção

---

## 📊 Pipeline do Projeto

### 🔵 1. Entendimento dos Dados
- Leitura com Pandas
- Tratamento de valores nulos
- Conversão de datas (série temporal)
- Ordenação cronológica dos dados

---

### 🟡 2. Engenharia de Série Temporal
- Criação da série temporal estruturada (ds / y)
- Garantia de consistência temporal
- Preparação para modelos estatísticos

---

### 🟠 3. Análise Exploratória
- Visualização da série histórica
- Identificação de tendência
- Avaliação de comportamento temporal
- Análise de estabilidade da série

---

### 🔴 4. Modelagem de Forecasting

#### 📌 Baseline
- Média móvel como referência simples

#### 📌 Modelos Estatísticos
- Holt-Winters (Exponential Smoothing)
  - Captura tendência e sazonalidade
- Prophet (Meta AI)
  - Modelagem robusta de tendência e sazonalidade

---

## 📊 Visualização do Modelo em Produção

Abaixo está a visualização gerada diretamente pelo sistema de previsão, comparando valores reais vs previsões dos modelos:

<p align="center">

<img src="./imagens/forecast.png" width="900"/>

</p>

### 🔍 Interpretação

- Linha azul: valores reais da série temporal  
- Linha laranja: previsão do modelo  
- O gráfico demonstra a capacidade do sistema de capturar padrões de tendência e sazonalidade  
- Resultado gerado pelo sistema em produção (Streamlit App)

---

## 📈 Comparação de Modelos

| Modelo         | MAE  | RMSE |
|----------------|------|------|
| Holt-Winters   | 2.34 | 2.86 |
| Prophet        | 2.53 | 3.08 |

---

## 📉 Análise de Performance

- Holt-Winters apresentou melhor desempenho neste dataset
- Prophet demonstrou maior complexidade, porém menor precisão neste cenário específico
- A série apresenta comportamento estável e forte padrão sazonal
- Modelos simples foram suficientes para boa generalização

---

## 💡 Insights de Negócio

- A demanda possui comportamento relativamente estável
- Há padrão sazonal bem definido
- Modelos estatísticos simples são altamente eficazes neste cenário
- Complexidade adicional nem sempre melhora performance

---

## 🚀 Sistema em Produção

A aplicação está disponível em produção via Streamlit Cloud:

👉 https://time-series-intelligence-forecasting.streamlit.app/

### ⚙️ Funcionalidades do Sistema

- Upload de arquivo CSV contendo série temporal
- Seleção de modelo de forecasting (Holt-Winters / Prophet)
- Geração automática de previsões
- Visualização comparativa (Real vs Previsão)
- Cálculo de métricas de performance (MAE e RMSE)

### 📌 Requisitos de Entrada

O sistema requer um dataset estruturado com as colunas:

- `ds` → variável temporal (datetime)
- `y` → variável alvo (numérica)

Os dados devem estar previamente tratados e ordenados cronologicamente.

### 📊 Saída do Sistema

- Gráfico interativo de previsão
- Métricas de avaliação do modelo
- Comparação entre abordagens estatísticas

## 🧠 Conclusão

O sistema demonstrou que modelos estatísticos clássicos como Holt-Winters podem superar modelos mais complexos como Prophet dependendo da estrutura dos dados.

Isso reforça a importância da análise exploratória e entendimento do comportamento da série antes da escolha do modelo.

---

## 🧭 Próximos Passos

Este projeto encerra sua versão atual como sistema de forecasting com modelos estatísticos (Holt-Winters e Prophet), consolidando os principais conceitos de séries temporais aplicados em um cenário de portfólio.

Como evolução conceitual futura, os próximos estudos incluem aprofundamento em técnicas mais avançadas de modelagem e escalabilidade de sistemas de previsão.

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels
- Prophet
- Scikit-learn
- Streamlit

---

## 📌 Status do Projeto

✔ Pipeline de dados concluído  
✔ Modelagem estatística implementada  
✔ Comparação de modelos realizada  
✔ Métricas de avaliação aplicadas  
✔ Sistema em produção (Streamlit Cloud)  

✔ Versão 1 concluída com deploy funcional em produção

---

## 🧠 Nota

Este projeto faz parte de um portfólio de Data Science com foco em problemas reais de previsão de demanda, engenharia de machine learning e sistemas em produção.