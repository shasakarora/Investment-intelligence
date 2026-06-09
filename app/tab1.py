import pandas as pd
import streamlit as st
import plotly.express as px

risk_df = pd.read_csv("../outputs/risk_metrics.csv")


def show_risk_analysis():

    st.header("Risk Analysis")
    col1, col2 = st.columns(2)
    # Top sharpe ratio stocks
    with col1:

        top_sharpe = risk_df.sort_values("Sharpe", ascending=False).head(10)

        fig_sharpe = px.bar(
            top_sharpe,
            x="Stock",
            y="Sharpe",
            color="Sharpe",
            color_continuous_scale="Teal",
            text_auto=".2f",
            title="Top 10 Stocks by Sharpe Ratio",
        )

        fig_sharpe.update_layout(xaxis_tickangle=30, title_x=0.36, height=500)
        fig_sharpe.update_traces(textposition="outside")
        st.plotly_chart(fig_sharpe, use_container_width=True)

    # Low voltality stocks
    with col2:

        low_vol = risk_df.sort_values("Volatility").head(10)

        fig_vol = px.bar(
            low_vol,
            x="Stock",
            y="Volatility",
            color="Volatility",
            color_continuous_scale="Pinkyl",
            text_auto=".3f",
            title="Top 10 Lowest Volatility Stocks",
        )

        fig_vol.update_layout(xaxis_tickangle=30, title_x=0.36, height=500)
        fig_vol.update_traces(textposition="outside")
        st.plotly_chart(fig_vol, use_container_width=True)

    st.divider()

    # Risk vs Return scatter graph
    st.subheader("Risk vs Return Landscape")

    fig_scatter = px.scatter(
        risk_df,
        x="Volatility",
        y="Annual_Return",
        color="Sharpe",
        hover_name="Stock",
        color_continuous_scale="Viridis",
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

    st.divider()
    # Detailed risk analysis

    display_risk_df = risk_df.copy()

    display_risk_df.columns = [
        "Stock",
        "Annual Return",
        "Volatility",
        "Sharpe Ratio",
        "Sortino Ratio",
        "Value at Risk (95%)",
        "Conditional Value at Risk (95%)",
        "Maximum Drawdown",
    ]
    display_risk_df["Annual Return"] = (display_risk_df["Annual Return"] * 100).round(2)
    display_risk_df["Volatility"] = (display_risk_df["Volatility"] * 100).round(2)
    display_risk_df["Value at Risk (95%)"] = (
        display_risk_df["Value at Risk (95%)"] * 100
    ).round(2)
    display_risk_df["Conditional Value at Risk (95%)"] = (
        display_risk_df["Conditional Value at Risk (95%)"] * 100
    ).round(2)
    display_risk_df["Maximum Drawdown"] = (
        display_risk_df["Maximum Drawdown"] * 100
    ).round(2)
    display_risk_df.index = range(1, len(display_risk_df) + 1)
    st.subheader("Complete Risk Metrics")

    st.dataframe(display_risk_df, use_container_width=True)
