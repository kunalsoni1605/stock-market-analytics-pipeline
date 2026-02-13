"""
Configuration settings for stock market data extraction
"""

# List of stocks to track (start with popular tech stocks)
STOCK_SYMBOLS = [
    'AAPL',   # Apple
    'MSFT',   # Microsoft
    'GOOGL',  # Google
    'AMZN',   # Amazon
    'TSLA',   # Tesla
    'META',   # Meta (Facebook)
    'NVDA',   # Nvidia
    'JPM',    # JP Morgan
    'V',      # Visa
    'JNJ',    # Johnson & Johnson
    'WMT',    # Walmart
    'PG',     # Procter & Gamble
    'DIS',    # Disney
    'NFLX',   # Netflix
    'COST'    # Costco
]

# Date range for historical data
LOOKBACK_DAYS = 365  # Get 1 year of historical data

# Output settings
RAW_DATA_PATH = './data/raw/'
PROCESSED_DATA_PATH = './data/processed/'