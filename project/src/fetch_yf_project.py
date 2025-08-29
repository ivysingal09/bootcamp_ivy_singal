import os, sys
import yfinance as yf
import pandas as pd

ticker = sys.argv[1] if len(sys.argv) > 1 else "VNQ"
start = sys.argv[2] if len(sys.argv) > 2 else "2022-01-01"
end   = sys.argv[3] if len(sys.argv) > 3 else "2023-12-31"

data_dir = os.getenv("DATA_DIR", "project/data")
raw_dir = os.path.join(data_dir, "raw")
os.makedirs(raw_dir, exist_ok=True)

df = yf.download(ticker, start=start, end=end)
df.reset_index(inplace=True)
out = os.path.join(raw_dir, f"{ticker}_raw_project.csv")
df.to_csv(out, index=False)
print(out)
