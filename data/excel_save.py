######################################################################
# help function to copy datafrem onto spreadsheet
# initial date: 24/11/2016
######################################################################
import pandas as pd
from openpyxl import load_workbook
from os import path

def save_excel(df, file_name, ws_name):
    '''
    Save data from a dataframe onto excel, in a specific sheet, without
    deleting the others' information
    input:
    - df: pandas dataframe
    - file_name: str
    - ws_name: str
    '''
    book = load_workbook(file_name)
    writer = pd.ExcelWriter(file_name, engine="openpyxl")
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    df.to_excel(writer, sheet_name=ws_name, index=True)
    writer.save()
