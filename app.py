import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

st.set_page_config(page_title="Forecast System", layout="wide")

st.title("📊 Time Series Forecasting System")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    df["ds"] = pd.to_datetime(df["ds"])
    df["y"] = pd.to_numeric(df["y"], errors="coerce")

    df = df.dropna()
    df = df.sort_values("ds").reset_index(drop=True)

    st.subheader("Dataset Preview")
    st.write(df.head())

    split_idx = int(len(df) * 0.8)

    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]

    model_type = st.selectbox("Select Model", ["Holt-Winters", "Prophet"])

    pred = None

    if model_type == "Holt-Winters":

        model = ExponentialSmoothing(
            train["y"].astype(float),
            trend="add",
            seasonal=None
        ).fit()

        pred = model.forecast(len(test))

    else:

        prophet_train = train[["ds", "y"]].copy()

        model = Prophet()
        model.fit(prophet_train)

        future = model.make_future_dataframe(periods=len(test), freq="D")
        forecast = model.predict(future)

        pred = forecast["yhat"].iloc[-len(test):].values

    # =========================
    # METRICS
    # =========================

    mae = mean_absolute_error(test["y"], pred)
    rmse = np.sqrt(mean_squared_error(test["y"], pred))

    col1, col2, col3 = st.columns(3)

    col1.metric("Model", model_type)
    col2.metric("MAE", f"{mae:.2f}")
    col3.metric("RMSE", f"{rmse:.2f}")

    st.divider()

    # =========================
    # PLOT
    # =========================

    st.subheader("Forecast Result")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(test["ds"], test["y"], label="Real")
    ax.plot(test["ds"], pred, label="Forecast")

    ax.set_title("Forecast vs Real")
    ax.legend()
    ax.grid()

    st.pyplot(fig)

    st.divider()

    # =========================
    # INSIGHT FINAL
    # =========================

    st.subheader("Insight")

    if mae < rmse:
        st.write("Modelo apresenta boa estabilidade geral nos erros.")
    else:
        st.write("Modelo pode ser melhorado com ajuste de parâmetros ou features externas.")

    st.success("Forecast gerado com sucesso 🚀 Projeto pronto para portfólio")