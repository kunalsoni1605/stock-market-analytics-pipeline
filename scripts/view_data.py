"""
Quick script to view the extracted data
"""

import pandas as pd
import glob
import os

# Find the most recent stock prices file
files = glob.glob('../data/raw/stock_prices_*.csv')
if not files:
    print("❌ No data files found!")
    exit()

latest_file = max(files, key=os.path.getctime)
print(f"📁 Loading: {latest_file}\n")

# Load data
df = pd.read_csv(latest_file)

# Show summary
print("=" * 70)
print("📊 DATA SUMMARY")
print("=" * 70)
print(f"Total records: {len(df):,}")
print(f"Number of stocks: {df['Symbol'].nunique()}")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
print(f"\nStocks: {', '.join(sorted(df['Symbol'].unique()))}")

# Show records per stock
print("\n" + "=" * 70)
print("📈 RECORDS PER STOCK")
print("=" * 70)
records_per_stock = df.groupby('Symbol').size().sort_values(ascending=False)
print(records_per_stock)

# Show latest prices
print("\n" + "=" * 70)
print("💰 LATEST CLOSING PRICES")
print("=" * 70)
latest_date = df['date'].max()
latest_prices = df[df['date'] == latest_date][['Symbol', 'close_price']].sort_values('Symbol')
print(latest_prices.to_string(index=False))

# Show sample data
print("\n" + "=" * 70)
print("🔍 SAMPLE DATA (First 10 rows)")
print("=" * 70)
print(df.head(10).to_string(index=False))

print("\n✅ Data looks good! Ready for Databricks!")