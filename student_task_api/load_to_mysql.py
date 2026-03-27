import pandas as pd
from sqlalchemy import create_engine
from file_load import file_load   # your function

DATABASE_URL = "mysql+pymysql://root:atul1234@localhost/student_db"

engine = create_engine(DATABASE_URL)

df = file_load()
df.rename(columns={"student_id": "id"}, inplace=True)

df.to_sql("students", con=engine, if_exists="replace", index=False)

print("✅ Data inserted into MySQL")