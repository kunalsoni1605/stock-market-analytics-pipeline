# Stock Market Analytics Pipeline

**Data Engineering Portfolio Project**

Author: Kunal Radhanpara  
Email: kunalsoni01616@gmail.com  
LinkedIn: [linkedin.com/in/kunalradhanpara](https://linkedin.com/in/kunalradhanpara)

---

## Project Overview

End-to-end stock market analytics pipeline demonstrating ETL, technical analysis, and business intelligence skills using Python, Databricks, and Power BI.

**Key Highlights:**
- ✅ Automated data extraction from Yahoo Finance API (15 stocks, 1 year history)
- ✅ Processed 3,500+ records in Databricks with PySpark
- ✅ Calculated 5 technical indicators (SMA, EMA, RSI, MACD, Bollinger Bands)
- ✅ Interactive Power BI dashboard with 15+ visualizations
- ✅ Real-time filtering and cross-page interactions

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Data Extraction** | Python 3.13, yfinance API |
| **Data Processing** | Databricks Community Edition, PySpark |
| **Storage** | Delta Lake Tables |
| **Visualization** | Power BI Desktop |
| **Version Control** | Git, GitHub |

---

## Project Architecture
```
Data Source (Yahoo Finance)
          ↓
Python Extraction Script
          ↓
Raw CSV Files (local)
          ↓
Databricks Upload
          ↓
PySpark Transformations
          ↓
Delta Lake Tables
          ↓
Power BI Dashboard
```

---

## Dataset

**Stocks Analyzed:** AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM, V, JNJ, WMT, PG, DIS, NFLX, COST

**Time Period:** 365 days (1 year historical data)

**Total Records:** ~3,500 data points

**Features:**
- Date, Symbol, Open, High, Low, Close, Volume
- SMA 20, SMA 50, EMA 12
- RSI (14-period)
- MACD, MACD Signal, MACD Histogram
- Bollinger Bands (Upper, Middle, Lower)

---

## Pipeline Workflow

### 1. Data Extraction (Python)
```bash
cd E:\Python\stock-market-analytics\scripts
python extract_stock_data.py
```

**Output:** CSV files in `data/raw/`

### 2. Data Processing (Databricks)

**Notebooks:**
1. `01_data_upload_and_exploration.py` - Data quality checks
2. `02_technical_indicators.py` - Calculate indicators using PySpark Window functions

**Output:** Delta table `workspace.processed_data.stock_prices_with_indicators`

### 3. Visualization (Power BI)

**Dashboard Pages:**
1. Executive Summary - KPIs, trends, volume
2. Technical Analysis - Moving averages, RSI, MACD, Bollinger Bands
3. Stock Comparison - Rankings, performance metrics

---

## Key Features

### Technical Indicators Calculated

**Moving Averages:**
- Simple Moving Average (20-day, 50-day)
- Exponential Moving Average (12-day)

**Momentum:**
- RSI (Relative Strength Index) - Overbought/oversold signals

**Trend:**
- MACD (Moving Average Convergence Divergence)
- MACD Signal Line, Histogram

**Volatility:**
- Bollinger Bands (20-day, 2 standard deviations)

### Power BI Dashboard

**Page 1: Executive Summary**
- Total stocks, latest date, average price
- Multi-line price trend chart
- Trading volume comparison
- Interactive stock filter

**Page 2: Technical Analysis**
- Price vs moving averages
- RSI gauge with buy/sell zones
- MACD indicator with histogram
- Bollinger Bands volatility chart

**Page 3: Stock Comparison**
- Matrix with all indicators
- Stock rankings by price
- Performance summary with data bars

---

## How to Run

### Prerequisites
```bash
Python 3.13
pip install yfinance pandas numpy python-dotenv
```

### Extract Data
```bash
cd scripts
python extract_stock_data.py
```

### Process in Databricks
1. Upload CSV to Databricks workspace
2. Run notebook `01_data_upload_and_exploration.py`
3. Run notebook `02_technical_indicators.py`

### View Dashboard
1. Open `powerbi/Stock_Market_Dashboard.pbix` in Power BI Desktop
2. Explore the 3 interactive pages

---

## Files Structure
```
stock-market-analytics/
├── data/
│   ├── raw/              # CSV files (gitignored)
│   └── processed/        # Exported data
├── scripts/
│   ├── config.py         # Stock symbols, API settings
│   ├── extract_stock_data.py
│   └── view_data.py
├── notebooks/
│   ├── 01_data_upload_and_exploration.py
│   ├── 02_technical_indicators.py
│   └── WEEK2_SUMMARY.md
├── powerbi/
│   ├── Stock_Market_Dashboard.pbix
│   └── Stock_Market_Dashboard.pdf
├── images/               # Dashboard screenshots
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Results & Insights

✅ Successfully extracted and processed 3,500+ stock records  
✅ Implemented 5 technical indicators using PySpark Window functions  
✅ Created interactive dashboard with 15+ visualizations  
✅ Enabled real-time filtering across all pages  

**Technical Skills Demonstrated:**
- Python API integration
- ETL pipeline design
- PySpark transformations
- Delta Lake table management
- Power BI DAX measures
- Data visualization best practices

---

## Future Enhancements

- [ ] Automate daily data refresh with Apache Airflow
- [ ] Add predictive models (LSTM for price forecasting)
- [ ] Deploy dashboard to Power BI Service
- [ ] Add more technical indicators (Fibonacci, Stochastic)
- [ ] Integrate with cloud storage (Azure Data Lake)

---

## Contact

**Kunal Radhanpara**  
📧 kunalsoni01616@gmail.com  
💼 [LinkedIn](https://linkedin.com/in/kunalradhanpara)  
🐙 [GitHub](https://github.com/kunalsoni1605)

**Portfolio:** [github.com/kunalsoni1605/stock-market-analytics-pipeline](https://github.com/kunalsoni1605/stock-market-analytics-pipeline)

---

## License

This project is for portfolio and educational purposes.

Stock data provided by Yahoo Finance API.
