import pandas as pd

def load_transactions(path="/Users/crew/Documents/RS-Mini/data/transaction.csv"):
    return pd.read_csv(path)

df = load_transactions()
print(df)
