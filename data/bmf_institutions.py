from excel_save import save_excel
from datetime import datetime, date
import requests
import pandas as pd
import workdays as wk
import time

_url = "http://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-tipo-de-participante-enUS.asp"

def _fetch_bmf(dat):
    data = {"dData1": dat}
    resp = requests.post(_url, data=data,
                         proxies = {'http': 'spoflpxy0001:8080'}).content
    df = pd.read_html(resp, match="1-DAY INTERBANK DEPOSIT FUTURES",
                      index_col=0)[0].dropna(axis='columns', how='all')
    df.columns = ["long", "long(%)", "short", "short(%)"]
    df.name = 'institutions'
    return df


def consolidate(dat_end):
    '''
    fetch data from bmf site and generates ouput table
    inputs:
    ------
    - dat: initial date
    - dat1: final date
    output:
    -----
    pandas dataframe
    '''
    dat = datetime.strptime(dat_end, "%m/%d/%Y")
    df = _fetch_bmf(wk.workday(dat,-1).strftime('%m/%d/%Y'))
    df1 = _fetch_bmf(dat_end)
    col = ["long", "long(%)", "ch(long)", "short", "short(%)", "ch(short)",
           "Net Position", "Net Change"]
    dfinal = pd.DataFrame(index=df.index, columns = col)
    dfinal["long"] = df1['long']
    dfinal["long(%)"] = df1['long(%)']
    dfinal["ch(long)"] = df1['long'] - df['long']
    dfinal["short"] = df1['short']
    dfinal["short(%)"] = df1['short(%)']
    dfinal["ch(short)"] = df1['short'] - df['short']
    dfinal["Net Change"] = dfinal["ch(long)"] - dfinal["ch(short)"]
    dfinal["Net Position"] = dfinal["long"] - dfinal["short"]
    return dfinal[dfinal.index != "Nonresident investors - RES.2689"]



if __name__ =='__main__':
    dat = date.today()
    while True:
        try:
            ds = consolidate(dat.strftime("%m/%d/%Y"))
        except:
            print("Date {} not yet available".format(dat))
            dat = wk.workday(dat,-1)
            time.sleep(0.5)
        else:
            save_excel(ds,"./data/indicators_input.xlsx", "OpenInterest")
            break
    #print("DI by institutions saved for date {}".format(dat.strftime("%m/%d/%Y")))
