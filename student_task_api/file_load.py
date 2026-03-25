import pandas as pd
import numpy as np

def file_load():
    try:
        data=pd.read_csv(r"C:\Users\atuls\OneDrive\Desktop\fastApi-100\student_task_api\students_complete.csv")
        df=pd.DataFrame(data)   
        df['gpa'].fillna(df['gpa'].mean(), inplace=True)
        return df  
    except Exception as e:
        print(e)
        return pd.DataFrame()
