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
    df = pd.read_sql('SELECT * FROM students where(grade=12)', engine)
    if not df.empty:
        df.to_excel('grade_12.xlsx', index=False)
    
    df = pd.read_sql('SELECT * FROM students where(grade=11)', engine)
    if not df.empty:
        df.to_excel('grade_11nature.xlsx', index=False)
    
    df = pd.read_sql('SELECT * FROM students where(grade=10)', engine)
    if not df.empty:
        df.to_excel('grade_10.xlsx', index=False)
    
    df = pd.read_sql('SELECT * FROM students where(grade=9)', engine)
    if not df.empty:
        df.to_excel('grade_9.xlsx', index=False)
save_to_excel()