# Stock Market Analytics Pipeline

Real-time stock market ETL pipeline using Python, Databricks, and Power BI.

## Overview

This project extracts stock market data from Yahoo Finance API, processes it using Databricks, and visualizes insights through Power BI dashboards.

## Tech Stack

- **Python 3.13** - Data extraction
- **Pandas** - Data manipulation  
- **Databricks** - ETL processing
- **Power BI** - Visualization
- **Yahoo Finance API** - Data source

## Features

✅ **Week 1 - Complete**
- Automated data extraction for 15+ stocks
- Historical price data (1 year)
- Data validation and quality checks

🚧 **Week 2 - In Progress**
- Databricks ETL pipeline
- Technical indicators (SMA, RSI, MACD)

📅 **Week 3-4 - Planned**
- Power BI dashboard
- Interactive visualizations

## Getting Started

### Prerequisites
- Python 3.10+
- Databricks Community Edition
- Power BI Desktop

### Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/stock-market-analytics-pipeline.git
cd stock-market-analytics-pipeline
```

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run extraction
```bash
cd scripts
python extract_stock_data.py
```

## Project Structure
```
stock-market-analytics-pipeline/
├── data/
│   ├── raw/              # Raw CSV files
│   └── processed/        # Processed data
├── scripts/
│   ├── config.py         # Configuration
│   ├── extract_stock_data.py  # Main script
│   └── view_data.py      # Validation
├── notebooks/            # Databricks notebooks
├── .gitignore
├── requirements.txt
└── README.md
```

## Stocks Tracked

AAPL, MSFT, GOOGL, AMZN, TSLA, META, NVDA, JPM, V, JNJ, WMT, PG, DIS, NFLX, COST

## Author

**Kunal Radhanpara**  
Data Engineering Student | NAIT  
📧 kunalsoni01616@gmail.com  
💼 [LinkedIn](https://linkedin.com/in/kunalradhanpara)  
📍 Edmonton, AB, Canada

## License

MIT License - Educational/Portfolio Project

**Last Updated:** February 2025