import sqlite3
import pandas as pd

# 读取Excel文件
excel_file_path = 'book_review_2.0.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(excel_file_path)

# 连接到SQLite数据库
con = sqlite3.connect("/mnt/mock-db/tutorial.db")

# 将数据写入数据库
df.to_sql('reviews', con, if_exists='replace', index=False)

print("Data inserted into the database successfully.")