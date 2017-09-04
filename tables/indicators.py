#####################################################################
# Script to generate latex table "indicadores" for bgc daily
# start: 07/01/2017
######################################################################
import pylatex as pl
from pylatex.utils import bold
import pandas as pd



_index = {
    'CDS 5Y': 'pts',
    'DAX': "%",
    'T-10': "pts",
    'S&P Fut': "%",
    'OIL': "%",
    'EUR': "%",
    'MXN': "%",
    'Iron Ore': "%",
    'Soya': "%",
    'VIX': "%"}

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
    hr = [ind]
    hr.extend(df.loc[ind, :].values)
    if ind in ['DAX', "S&F Fut", 'Iron Ore']:
        hr[-2] = round(hr[-2],1)
        hr[-1] = round(hr[-1],1)
    elif ind in ['EUR', 'MXN']:
        hr[-2] = round(hr[-2],2)
        hr[-1] = round(hr[-1],1)
    else:
        hr[-2] = round(hr[-2],1)
        hr[-1] = round(hr[-1],1)
    if (hr[-1] < 0):
        hr[-1] = pl.TextColor('red', str(hr[-1]) + _index[ind])
    else:
        hr[-1] = str(hr[-1]) + _index[ind]
    return hr


def gen_table(df):
    '''
    add a table to a doc.
    inputs:
    ------
    - df: DataFrame
    returns:
    - side effect
    '''
    with doc.create(pl.Tabular('l  r  r  ', col_space='0.15cm', row_height=1.2)) as table:
        header_row = ["Index", "", "+/-"]
        table.add_hline()
        table.add_row(header_row, mapper=[bold])
        table.add_hline()
    for ind in df.index:
        table.add_row(_fill_row(ind, df))
    table.add_hline()


# main
if __name__ =='__main__':
    df = pd.read_excel("./data/indicators_input.xlsx", sheetname="indicators",
                       index_col=0, parse_cols="A:C")
    doc = pl.Document('./latex/indicators', font_size='scriptsize',
                      documentclass='standalone',
                      document_options=['article', 'crop=false'])
    gen_table(df)
    doc.generate_tex()
    print("Table of indicators is Done!")
