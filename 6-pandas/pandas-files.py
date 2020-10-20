import pandas as pd
import sqlite3

# df = pd.read_csv('sample.csv') # sample.csv dosyasını pandas üzerinden okuduk.
# df = pd.read_json('sample.json',encoding='utf-8') # JSON dosyası
df = pd.read_excel('datasets/stok.xlsx') # EXCEL dosyası

# connection = sqlite3.connect('sample.db') # SQL dosyası
# df = pd.read_sql_query("SELECT * FROM students",connection)

print(df["lucastokkodu"].head(100))