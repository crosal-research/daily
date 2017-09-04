# script to draw table for open interest
# initial date:
######################################################################
import pylatex as pl
from pylatex.utils import bold, dumps_list
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# help function
def _fill_row(ind, df):
    '''
    return a list where, in the first, cell
    goes ind (particular index of df) and
    in the remaider goes the values of that row
    inputs:
    -----
    ind: str
    - df: DataFrame
    - returns:
    -------
    -list
    '''
    row = []
    row.extend(df.loc[ind, :].values)
    return row


def gen_table(df, doc):
    '''
    add a table to a doc.
    inputs:
    ------
    - df: DataFrame
    - doc: str (latex document)
    returns:
    - side effect
    '''
    color = 'white'
    with doc.create(pl.Tabular('l | c c c c c', col_space='0.15cm', pos=['h'])) as table:
        header_row0 = ["Time", "Country", "Indicator", "Period", "Forecast", "Impact"]
        table.add_hline()
        table.add_row(header_row0, mapper=[bold], color=color)
        table.add_hline()
    for ind in df.index:
        color = 'white' if color == 'lightgray' else 'lightgray'
        row = _fill_row(ind, df)
        table.add_row(row, color=color)
    table.add_hline()


def gen_doc(file_output):
    '''
    function to return a latex document with a table for Brazilian bonds
    input:
    -----
    - file_output: str
    returnt:
    str - latex output.
    '''
    doc = pl.Document('./latex/{}'.format(file_output), font_size='normalsize',
                      documentclass='standalone',
                      document_options=['article', 'crop=false'])
    return doc


# main
if __name__ =='__main__':
    dc = "agenda"
    df = pd.read_excel("./data/indicators_input.xlsx", sheetname=dc,
                       header=0, usecols=[0, 1, 2, 3, 4, 5])
    doc = gen_doc(dc)
    gen_table(df, doc)
    doc.generate_tex()
    print ("Agenda is done!!")
