"""save as excel"""
import pandas as pd
from sqlalchemy import create_engine

def save_to_excel():
    """save to ecxel"""
    user = 'school'
    paswd = 'school_pwd'
    host = 'localhost'
    db = 'school_db'
    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(user,
                                                paswd,
                                                host,
                                                db))
    
    df = pd.read_sql('SELECT * FROM students', engine)

    df.to_excel('students.xlsx', index=False)

