# 📊 Time Series Intelligence & Forecasting System

Sistema completo de Inteligência em Séries Temporais para análise, detecção de anomalias e previsão de vendas com modelos estatísticos e técnicas de Machine Learning.

Este projeto simula um ambiente real de Data Science aplicado a problemas de negócio, com foco em análise temporal, forecasting e avaliação de modelos.

---

# 🎯 Objetivo

Construir um pipeline completo de análise de séries temporais capaz de:

- Entender padrões de vendas ao longo do tempo
- Detectar tendências e sazonalidade
- Identificar anomalias em dados reais
- Construir modelos de previsão
- Comparar abordagens estatísticas e baseline simples
- Avaliar performance com métricas reais (MAE e RMSE)

---

# 📁 Estrutura do Projeto
data/
├── raw/ # Dados brutos (train, stores, oil, holidays)
├── processed/ # Dados tratados

notebooks/
└── time_series_project.ipynb

src/
├── data/
├── features/
├── models/
├── visualization/
└── utils/

models/
reports/
configs/


---

# 📊 Dataset Utilizado

O projeto utiliza dados de vendas contendo:

- Histórico de vendas diárias
- Informações de lojas
- Fatores externos (feriados, petróleo)
- Dados auxiliares de contexto

---

# 🧹 Pipeline do Projeto

## 1. Pré-processamento
- Leitura dos dados com Pandas
- Tratamento de valores nulos
- Conversão para série temporal

## 2. Análise Exploratória (EDA)
- Visualização da série temporal
- Distribuição de vendas
- Identificação de padrões gerais

## 3. Suavização da Série
- Média móvel (rolling mean)
- Identificação de tendência

## 4. Decomposição da Série Temporal
- Tendência (Trend)
- Sazonalidade (Seasonality)
- Resíduos (Noise)

## 5. Análise Estatística
- Autocorrelação (ACF)
- Autocorrelação parcial (PACF)

## 6. Detecção de Anomalias
- Baseada em resíduos da decomposição
- Identificação de valores fora do padrão estatístico

## 7. Modelagem de Forecasting
- Baseline: Média móvel
- Modelo avançado: Holt-Winters (Exponential Smoothing)

---

# 📈 Resultados dos Modelos

## 🔵 Média Móvel (Baseline)
- MAE: 108,311
- RMSE: 138,001

## 🟣 Holt-Winters
- MAE: 55,617
- RMSE: 94,051

---

# 🧠 Conclusão Técnica

O modelo Holt-Winters apresentou desempenho superior ao baseline de média móvel, reduzindo significativamente MAE e RMSE, indicando melhor capacidade de capturar tendência e sazonalidade da série temporal.

Isso demonstra que modelos estatísticos com componentes de tendência e sazonalidade são mais adequados para previsão de séries temporais reais do que abordagens simplificadas.

---

# 📊 Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Scikit-learn
- Jupyter Notebook

---

# 🚀 Aprendizados do Projeto

- Manipulação de séries temporais reais
- Engenharia de features temporais
- Análise estatística de dados sequenciais
- Decomposição de séries temporais
- Detecção de anomalias baseada em resíduos
- Construção e avaliação de modelos de forecasting
- Comparação entre abordagens simples e estatísticas

---

# 📌 Próximos Passos (Roadmap Evolutivo)

- Modelos ARIMA/SARIMA
- Prophet (Meta)
- Machine Learning para forecasting
- Redes neurais (LSTM)
- Pipeline automatizado de previsão
- Deploy do modelo

---

# 📎 Autor

Projeto desenvolvido como parte de portfólio de Data Science com foco em aplicações reais de séries temporais e engenharia de Machine Learning.