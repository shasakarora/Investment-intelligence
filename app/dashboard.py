import streamlit as st
import pandas as pd
import plotly.express as px

from tab1 import show_risk_analysis
from tab2 import show_portfolio_construction
from tab3 import show_stock_explorer

st.set_page_config(
    page_title="Investment Intelligence Platform", page_icon="📈", layout="wide"
)

st.title("📈 Investment Intelligence Platform")

st.markdown("""
AI-Powered Portfolio Construction, Risk Assessment and Investment Recommendation System
""")

tab1, tab2, tab3 = st.tabs(
    ["📊 Risk Analysis", "📈 Portfolio Construction", "🔍 Stock Explorer"]
)

# TAB 1 (Risk Analysis)
with tab1:
    show_risk_analysis()

# TAB 2 (Portfolio Construction)
with tab2:
    show_portfolio_construction()

# TAB 3 (Stock explorer)
with tab3:
    show_stock_explorer()
