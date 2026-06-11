import pandas as pd
import streamlit as st
import plotly.express as px

risk_df = pd.read_csv("outputs/risk_metrics.csv")

predictions_df = pd.read_csv("data/predicted_portfolio_signals.csv")

stock_predictions = (
    predictions_df.groupby("Name")["Predicted_Return"].mean().reset_index()
)

stock_predictions.rename(columns={"Name": "Stock"}, inplace=True)


def show_stock_explorer():

    st.header("Stock Explorer")

    stock = st.selectbox("Choose Stock", sorted(risk_df["Stock"].unique()))
    stock_row = risk_df[risk_df["Stock"] == stock].iloc[0]

    pred_row = stock_predictions[stock_predictions["Stock"] == stock]
    predicted_return = pred_row["Predicted_Return"].iloc[0]

    if len(pred_row) > 0:
        predicted_return = pred_row["Predicted_Return"].mean()
    else:
        predicted_return = 0

    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Predicted Daily Return", f"{predicted_return*100:.3f}%")
    c2.metric("Sharpe Ratio", round(stock_row["Sharpe"], 2))
    c3.metric("Volatility", round(stock_row["Volatility"], 3))

    st.divider()

    # Reasoning
    reasons = []

    if stock_row["Sharpe"] > 0.5:
        reasons.append("Strong risk-adjusted returns because of high sharpe ratio")
    if stock_row["Volatility"] < 0.35:
        reasons.append(
            "Relatively low volatility so this stock follows low change in trends"
        )
    if predicted_return > 0:
        reasons.append("Positive returns are expected so BUY is recommmended")
    if predicted_return < 0:
        reasons.append("Negative returns are predicted so SELL is recommmended")
    if stock_row["Max_Drawdown"] > -0.6:
        reasons.append("Selected stock has controlled historical drawdown")
    if len(reasons) == 0:
        reasons.append("Higher-risk investment profile")

    st.info(" | ".join(reasons))
    st.divider()

    # Price vs time graph of selected stock
    st.subheader("Historical Price Trend")
    try:
        price_df = pd.read_csv(f"data/dataset/{stock}.csv")
        if "Date" in price_df.columns:
            fig_price = px.line(
                price_df, x="Date", y="Close", title=f"{stock} Historical Closing Price"
            )
        else:
            fig_price = px.line(
                price_df, y="Close", title=f"{stock} Historical Closing Price"
            )
        fig_price.update_layout(title_x=0.5, height=500)

        st.plotly_chart(fig_price, use_container_width=True)

    except Exception as e:

        st.warning(f"Could not load historical data for {stock}")

        st.divider()

    # Risk metrics of selected stock
    metrics_df = pd.DataFrame(
        {
            "Metric": [
                "Annual Return",
                "Volatility",
                "Sharpe Ratio",
                "Sortino Ratio",
                "Value at Risk (95%)",
                "Conditional value at risk (95%)",
                "Max Drawdown",
            ],
            "Value": [
                stock_row["Annual_Return"],
                stock_row["Volatility"],
                stock_row["Sharpe"],
                stock_row["Sortino"],
                stock_row["VaR_95"],
                stock_row["CVaR_95"],
                stock_row["Max_Drawdown"],
            ],
        }
    )
    st.subheader("Risk Metrics")

    for _, row in metrics_df.iterrows():
        c1, c2 = st.columns([2, 1])

        c1.write(row["Metric"])

        if row["Metric"] == "Annual Return":
            c2.write(f"{row['Value']*100:.2f}%")
        else:
            c2.write(f"{row['Value']:.4f}")