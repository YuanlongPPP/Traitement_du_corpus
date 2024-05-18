import sqlite3
import pandas as pd

excel_file_path = 'book_review_2.0.xlsx' 
df = pd.read_excel(excel_file_path)
con = sqlite3.connect("/mnt/mock-db/tutorial.db")
df.to_sql('reviews', con, if_exists='replace', index=False)
print("Data inserted into the database successfully.")