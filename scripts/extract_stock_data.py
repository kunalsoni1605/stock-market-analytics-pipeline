"""
Stock Market Data Extraction Script
Extracts historical stock data from Yahoo Finance
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os
from config import STOCK_SYMBOLS, LOOKBACK_DAYS, RAW_DATA_PATH

def create_directories():
    """Create necessary directories if they don't exist"""
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    print(f"✅ Data directory created/verified: {RAW_DATA_PATH}")

def extract_stock_data(symbol, start_date, end_date):
    """
    Extract historical stock data for a single symbol
    
    Args:
        symbol (str): Stock ticker symbol (e.g., 'AAPL')
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
    
    Returns:
        DataFrame: Stock price data with OHLCV columns
    """
    try:
        print(f"📊 Extracting data for {symbol}...", end=' ')
        
        # Create Ticker object
        stock = yf.Ticker(symbol)
        
        # Download historical data
        df = stock.history(start=start_date, end=end_date)
        
        if df.empty:
            print(f"❌ No data found")
            return None
        
        # Reset index to make Date a column
        df = df.reset_index()
        
        # Add symbol column
        df['Symbol'] = symbol
        
        # Rename columns to match our schema
        df = df.rename(columns={
            'Date': 'date',
            'Open': 'open_price',
            'High': 'high_price',
            'Low': 'low_price',
            'Close': 'close_price',
            'Volume': 'volume'
        })
        
        # Select only the columns we need
        df = df[['date', 'Symbol', 'open_price', 'high_price', 
                 'low_price', 'close_price', 'volume']]
        
        print(f"✅ {len(df)} records extracted")
        return df
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def extract_company_info(symbol):
    """
    Extract company information for a stock symbol
    
    Args:
        symbol (str): Stock ticker symbol
    
    Returns:
        dict: Company information
    """
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        
        company_data = {
            'symbol': symbol,
            'company_name': info.get('longName', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'country': info.get('country', 'N/A'),
            'website': info.get('website', 'N/A')
        }
        
        return company_data
        
    except Exception as e:
        print(f"⚠️  Could not extract company info for {symbol}: {str(e)}")
        return None

def main():
    """Main execution function"""
    
    print("=" * 60)
    print("🚀 STOCK MARKET DATA EXTRACTION STARTING")
    print("=" * 60)
    
    # Create directories
    create_directories()
    
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=LOOKBACK_DAYS)
    
    print(f"\n📅 Date Range: {start_date.date()} to {end_date.date()}")
    print(f"📈 Stocks to extract: {len(STOCK_SYMBOLS)}")
    print(f"📊 Symbols: {', '.join(STOCK_SYMBOLS)}\n")
    
    # Store all dataframes
    all_stock_data = []
    company_info_list = []
    
    # Extract data for each stock
    for i, symbol in enumerate(STOCK_SYMBOLS, 1):
        print(f"[{i}/{len(STOCK_SYMBOLS)}] ", end='')
        
        # Extract price data
        df = extract_stock_data(symbol, start_date, end_date)
        if df is not None:
            all_stock_data.append(df)
        
        # Extract company info
        company_info = extract_company_info(symbol)
        if company_info is not None:
            company_info_list.append(company_info)
    
    # Combine all stock data
    if all_stock_data:
        print("\n" + "=" * 60)
        print("💾 SAVING DATA TO CSV FILES")
        print("=" * 60)
        
        # Combine all stock price data
        combined_df = pd.concat(all_stock_data, ignore_index=True)
        
        # Save to CSV
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        price_filename = f'{RAW_DATA_PATH}stock_prices_{timestamp}.csv'
        combined_df.to_csv(price_filename, index=False)
        print(f"✅ Stock prices saved: {price_filename}")
        print(f"   Total records: {len(combined_df):,}")
        
        # Save company info
        if company_info_list:
            company_df = pd.DataFrame(company_info_list)
            company_filename = f'{RAW_DATA_PATH}company_info_{timestamp}.csv'
            company_df.to_csv(company_filename, index=False)
            print(f"✅ Company info saved: {company_filename}")
            print(f"   Total companies: {len(company_df)}")
        
        # Display sample data
        print("\n" + "=" * 60)
        print("📊 SAMPLE DATA (First 5 rows)")
        print("=" * 60)
        print(combined_df.head())
        
        print("\n" + "=" * 60)
        print("✅ DATA EXTRACTION COMPLETE!")
        print("=" * 60)
        print(f"📁 Check your data folder: {RAW_DATA_PATH}")
        
    else:
        print("\n❌ No data was extracted. Please check your internet connection.")

if __name__ == "__main__":
    main()