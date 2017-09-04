######################################################################
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
    row = [ind]
    row.extend(df.loc[ind, :].values)
    if (row[-1] < 0):
        row[-1] = str((row[-1]))
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
    with doc.create(pl.Tabular('l|c c|c c|c c|c c c', col_space='0.15cm', pos=['h'])) as table:
        if doc.__dict__['default_filepath'].split('/')[-1] == "NTN-B":
            header_row0 = ['Expiry', 'Yield', "Daily Ch.",  'BE',
            'Ch. BE', 'FRA', 'FRA BE', "Duration", "BRL", "Carry"]
            header_row1 = ['', '', '(%)', '',
                          '', '', '(Daily)', "(Macaulay)", "PV01", "(bps)"]
        else:
            header_row0 = ['Expiry', 'Yield', 'Daily Ch.', 'Spread',
                          'Daily Ch.', '%DI', 'Daily Ch.', "Duration", "BRL", "DI"]
            header_row1 = ['', '', '(%)', '',
                           'Daily', '', '(%)', "(Macaulay)", "PV01", "Conts."]
        table.add_hline()
        table.add_row(header_row0, mapper=[bold], color=color)
        table.add_row(header_row1, mapper=[bold], color=color)
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
    for dc in ["NTN-F", "NTN-B", "LTN"]:
        df = pd.read_excel("./data/indicators_input.xlsx", sheetname=dc,
                           header=0, index_col=0, usecols=[0, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        df.index = df.index.map(lambda x: x.strftime(format="%b-%y"))
        df['Macaulay Duration'] = df['Macaulay Duration'].map(lambda x: x.strftime(format="%b-%d-%y"))
        df.iloc[:,0] = df.iloc[:,0].map(lambda x: np.round(x, 4))
        df.iloc[:,1] = df.iloc[:,1].map(lambda x: np.round(x, 2))
        df.iloc[:,2] = df.iloc[:,2].map(lambda x: np.round(x, 2))
        df.iloc[:,3] = df.iloc[:,3].map(lambda x: np.round(x, 2))
        df.iloc[:,7] = df.iloc[:,7].map(lambda x: int(np.round(x,0)))
        if dc == "NTN-B":
            df.iloc[:,4] = df.iloc[:,4].map(lambda x: np.round(x, 2))
            df.iloc[:,5] = df.iloc[:,5].map(lambda x: np.round(x, 2))
            df.iloc[:,8] = df.iloc[:,8].map(lambda x: np.round(x, 2))
        else:
            df.iloc[:,4] = df.iloc[:,4].map(lambda x: np.round(x*100, 2))
            df.iloc[:,5] = df.iloc[:,5].map(lambda x: np.round(x*100, 2))
            df.iloc[:,8] = df.iloc[:,8].map(lambda x: int(np.round(x, 0)))
        doc = gen_doc(dc)

        gen_table(df, doc)
        doc.generate_tex()

    print("Bonds is done!")
