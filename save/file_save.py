"""save file to excel"""
import numpy as np
import pandas as pd

def save_to_excel(data):
    """save data to excel"""
    file_name = 'data.xlsx'
    df = pd.DataFrame(data, columns=['First Name', 'MIddle Name', 'Last Name', 'Grade', 'Gender'])
    df.to_excel(file_name, index=False)
