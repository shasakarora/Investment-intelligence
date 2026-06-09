import pandas as pd
import streamlit as st
import plotly.express as px

allocations = pd.read_csv("../outputs/portfolio_allocations.csv")


def show_portfolio_construction():

    st.header("Portfolio Construction")
    # Selection bar
    profile = st.selectbox("Select Portfolio Type", allocations["Profile"].unique())
    filtered_alloc = allocations[allocations["Profile"] == profile]

    c1, c2, c3 = st.columns(3)

    portfolio_return = (
        filtered_alloc["Allocation_%"] * filtered_alloc["Predicted_Return"]
    ).sum() / 100
    portfolio_sharpe = (
        filtered_alloc["Allocation_%"] * filtered_alloc["Sharpe"]
    ).sum() / 100
    portfolio_volatility = (
        filtered_alloc["Allocation_%"] * filtered_alloc["Volatility"]
    ).sum() / 100

    c1.metric("Expected Return", f"{portfolio_return*100:.2f}%")

    c2.metric("Portfolio Sharpe", f"{portfolio_sharpe:.2f}")

    c3.metric("Portfolio Volatility", f"{portfolio_volatility*100:.2f}%")

    st.divider()

    # Pie Chart
    fig_pie = px.pie(
        filtered_alloc,
        names="Stock",
        values="Allocation_%",
        hole=0.4,
        title=f"{profile} Portfolio Allocation",
    )
    fig_pie.update_layout(height=450, width=450, title_x=0.36)
    st.plotly_chart(fig_pie, use_container_width=True)

    # Plot of predicted returns of stocks belonging to same portfolio
    returns_df = filtered_alloc.copy()
    returns_df["Predicted_Return_%"] = returns_df["Predicted_Return"] * 100

    fig_returns = px.bar(
        returns_df.sort_values("Predicted_Return_%", ascending=False),
        x="Stock",
        y="Predicted_Return_%",
        color="Predicted_Return_%",
        color_continuous_scale="Blues",
        text_auto=".2f",
        title=f"{profile} Portfolio Expected Returns (%)",
    )

    fig_returns.update_layout(
        height=550,
        title_x=0.36,
        xaxis_tickangle=35,
        yaxis_title="Predicted Return (%)",
    )

    fig_returns.update_traces(texttemplate="%{y:.2f}%")

    fig_returns.add_hline(y=0, line_dash="dash", line_color="white")

    st.plotly_chart(fig_returns, use_container_width=True)

    st.divider()

    display_df = filtered_alloc.copy()

    display_df["Predicted Return (%)"] = display_df["Predicted_Return"] * 100
    display_df = display_df.drop(columns=["Predicted_Return"])
    st.subheader("Portfolio Constituents")
    st.dataframe(display_df, use_container_width=True)
