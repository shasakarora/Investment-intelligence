# Investment Intelligence Platform
This is an AI-powered investment intelligence platform for portfolio construction, risk analysis and stock recommendation using machine learning and financial risk metrics.

## Features
- Risk analysis of NIFTY-50 stocks
- Portfolio construction for different investors (Conservative, Balanced and Agressive stratergies)
- Sharpe Ratio, Sortino Ratio, VaR, CVaR and Maximum Drawdown analysis for each stock
- Interactive streamlit dashboard
- Visualization of historical stock data

## Project Structure
```
Investment-intelligence/
|
|- app/
|   |-- dashboard.py
|   |-- tab1.py
|   |-- tab2.py
|   |-- tab3.py
|
|-- data/
|   |-- dataset/
|
|-- outputs/
|-- notebooks/
|   |-- model1.ipynb
|
|-- portfolio/
|   |-- portfolio_construction.ipynb
|
|-- risk_assessment/
|   |-- risk_analysis.ipynb
|   |-- risk_indexes.py
|
|-- data_analysis.ipynb
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Installation
Follow the given steps in order to run the project.
1. Clone the repository : Run the following commands.
    - git clone https://github.com/shasakarora/Investment-intelligence
    - cd Investment-intelligence
2. Create a virtual environment and activate it on your system :
    - python -m venv env
    - (Windows) env\Scripts\activate
      (Mac) source env/bin/activate
3. Run pip install -r requirements.txt to install necessary libraries.
4. Download the dataset :
    - https://www.kaggle.com/datasets/rohanrao/nifty50-stock-market-data/data (Dataset link)
    - csv files of each stock's historical data should be in "data/dataset/"
5. Run data_analysis.ipynb using command jupyter notebook data_analysis.ipynb
This notebook performs exploratory data analysis and preprocessing of the stock dataset.
6. Train the prediction model :
Run "jupyter notebook notebooks/model1.ipynb".This notebook trains the machine learning model and generates "data/predicted_portfolio_signals.csv" containing predicted stock returns.
7. Perform risk analysis of stocks :
Run "jupyter notebook risk_assessment/risk_analysis.ipynb".This notebook generates "outputs/risk_metrics.csv" containing Annual return, Volatility, Sharpe ratio, Sortino ratio, Value at risk (VaR), Conditional value at risk (CVaR), Maximum drawdown for each stock.
8. Portfolio construction :
Run "jupyter notebook portfolio/portfolio_construction.ipynb".This notebook generates "outputs/portfolio_allocations.csv" containing portfolio weights for Conservative, Balanced and Aggressive investor profiles.
9. Launch dashboard :
Run "streamlit run app/dashboard.py" to launch the dashboard on localhost.The dashboard has 3 tabs, namely Risk Analysis, Portfolio Construction and Stock Explorer with interactive visualizations and portfolio recommendations.

## Dashboard Preview :
 Tab 1 (Risk Analysis)
<img width="1918" height="1002" alt="image" src="https://github.com/user-attachments/assets/6220f3ae-b98a-4471-bf71-125894ba4b31" />
<img width="1881" height="807" alt="image" src="https://github.com/user-attachments/assets/6e9419e3-0c5a-489c-84d9-3c28f76f980f" />
<img width="1800" height="695" alt="image" src="https://github.com/user-attachments/assets/7ddeb757-fc61-44f1-b503-a88be07cdfa0" />
 Tab 2 (Portfolio Construction)
<img width="1918" height="965" alt="image" src="https://github.com/user-attachments/assets/038ebbb7-c690-45c5-8e20-c4d5becd91d0" />
<img width="1918" height="820" alt="image" src="https://github.com/user-attachments/assets/77c0d6db-ef0e-43df-a825-1a5bc9afa267" />
<img width="1860" height="741" alt="image" src="https://github.com/user-attachments/assets/a8f15644-fd64-4307-9132-8248bf11e669" />
 Tab 3 (Stock explorer)
<img width="1918" height="880" alt="image" src="https://github.com/user-attachments/assets/90472b57-4ba4-43ba-a306-6b7be41bbbdb" />
<img width="1912" height="766" alt="image" src="https://github.com/user-attachments/assets/38c4f6fa-9c87-4b2a-a745-728731c4afa8" />
<img width="1858" height="578" alt="image" src="https://github.com/user-attachments/assets/a61c345c-ac18-469f-b034-578d9b091f30" />
