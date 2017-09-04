######################################################################
## script to draw first page chart
## initial date: 31/01/2017
######################################################################
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea


#helper
def poly_line(df, deg):
    """
    Takes a dataframe with datetime index and one columns
    and returns dataframe with polinomial approximation
    input:
    -----
    - df: dataframe
    - deg: int
    returns:
    - dataframe
    """
    dt = pd.date_range(df.index[0], df.index[-1], freq='d')
    dn = pd.DataFrame(list(range(0, len(dt))),index=dt)
    dnna = pd.merge(dn, df, left_index=True, right_index=True, how="outer").dropna()
    poly = pd.np.polyfit(dnna.iloc[:, 0].values, dnna.iloc[:, 1], deg)
    s =  pd.np.poly1d(poly)(range(0, len(dt)))
    return pd.DataFrame(s, index=dt, columns=['poly'])



# IPCA linked
db = pd.read_excel("./data/indicators_input.xlsx", sheetname='NTN-B',
                   index_col=3, dayfirst=True,
                   usecols=[1, 2, 4, 8])


# Fixed Bonds
df = pd.read_excel("./data/indicators_input.xlsx", sheetname='LTN',
                   index_col=3, dayfirst=True,
                   usecols=[1, 2, 6, 8, 11])
df['DI'] = df['DI']*100

dl = pd.read_excel("./data/indicators_input.xlsx", sheetname='NTN-F',
                   index_col=3, dayfirst=True,
                   usecols=[1, 2, 6, 8, 11])
dl['DI'] = dl['DI']*100

dfixed = pd.concat([df, dl], join="inner").sort_index()
dfixed["% DI"] = dfixed["% DI"]*100


## charts
def gen_chart_ntnb(dfinal, title, y_title):
    """
    chart for report
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # data
    for c in ["BE", "Bond Yield"]:
        if c == "BE":
            dfinal.loc[:, c].plot(ax=ax, linewidth=2, style='-v',
                                  label=c)
        else:
            dfinal.loc[:, c].plot(ax=ax, linewidth=2, style='-o',
                                  label=c)
    # labels
    for label in ax.xaxis.get_ticklabels():
        label.set_fontsize(14)
    for label in ax.yaxis.get_ticklabels():
        label.set_fontsize(14)
    ax.set_title(title, dict(fontsize=24))
    ax.set_ylabel(y_title, dict(fontsize=16))
    ax.set_xlabel('', dict(fontsize=16))

    yv = 0.08 #vertical shift to labels
    for i, text in enumerate(dfinal.Labels):
        x, y = (dfinal.index[i], dfinal["Bond Yield"].values[i])
        ax.annotate(str(text), xy=(x, y), xytext=(x, y + yv))


    # axis config
    ax.set_ylim([0, 7])
    ax.title.set_position([.5,1.03])


    # legend
    ax.legend(loc="lower right", fontsize=14)

    return fig


def gen_chart_fixed(dfinal, title, y_title):
    """
    chart for report
    """
    global df_ploly
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # data

    dfinal[["% DI"]].plot(ax=ax, style='-o',
                linewidth=0, label="%DI")
    df_poly = poly_line(dfinal[["% DI"]], 3)
    df_poly.plot(ax=ax, linewidth=1, label="poly aprox.")
    # labels
    for label in ax.xaxis.get_ticklabels():
        label.set_fontsize(14)

    for label in ax.yaxis.get_ticklabels():
        label.set_fontsize(14)
    ax.set_title(title, dict(fontsize=24))
    ax.set_ylabel(y_title, dict(fontsize=16))
    ax.set_xlabel('', dict(fontsize=16))

    yv = 0.08 #vertical shift to labels
    for i, text in enumerate(dfinal.Labels):
        x, y = (dfinal.index[i], dfinal["% DI"].values[i])
        if text in ['out-17', 'jul-18', 'jan-19', 'abr-19', 'F18']:
            ax.annotate(str(text), xy=(x, y), xytext=(x, y + yv - 0.02))
        else:
            ax.annotate(str(text), xy=(x, y), xytext=(x, y - yv))

    # axis config
    ax.margins(0.0, 0.2)
    ax.title.set_position([.5,1.03])


    # legend
    ax.margins(0.0, 0.2)
    ax.legend(loc="upper right", fontsize=14)

    return fig


def gen_chart_fixed_di(dfinal, title, y_title):
    """
    chart for report
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # data
    dfinal[["Bond Yield"]].plot(ax=ax, style='o',
                                label="Bond Yield")
    dfinal[["DI"]].plot(ax=ax, linewidth=1,
                        label="DI")
    for label in ax.xaxis.get_ticklabels():
        label.set_fontsize(14)
    for label in ax.yaxis.get_ticklabels():
        label.set_fontsize(14)
    ax.set_title(title, dict(fontsize=24))
    ax.set_ylabel(y_title, dict(fontsize=16))
    ax.set_xlabel('', dict(fontsize=16))

    yv = 0.08 # vertical shift to labels
    for i, text in enumerate(dfinal.Labels):
        x, y = (dfinal.index[i], dfinal["Bond Yield"].values[i])
        if text in ['out-17', 'abr-18', 'jul-18', 'out-18',
                    'abr-19', 'out-19', 'jan-20', 'jul-20']:
            ax.annotate(str(text), xy=(x, y), xytext=(x, y + yv - 0.2))
        elif text in ['F18', 'F19', 'F21']:
            ax.annotate(str(text), xy=(x, y), xytext=(x, y + - yv + 0.2))
        else:
            ax.annotate(str(text), xy=(x, y), xytext=(x, y - yv))

    #axis config
    ax.title.set_position([.5,1.03])

    #margins
    ax.margins(x=0.1, y=0.2)
    ax.set_xlim(ax.get_xlim()[0]-1, ax.get_xlim()[1]+ 1)

    # legend
    ax.legend(loc="upper right", fontsize=14)

    return fig


fig_ntnb = gen_chart_ntnb(db, "IPCA Linked Bonds", "%")
fig_ntnb.savefig("./charts/ntnb.png")

fig_fixed = gen_chart_fixed(dfixed[["Labels", "% DI"]], "Fixed-Rate Bonds", "%")
fig_fixed.savefig("./charts/fixed.png")

fig_fixed_di = gen_chart_fixed_di(dfixed[["Labels", "Bond Yield", "DI"]], "Fixed Bonds x DI", "%")
fig_fixed_di.savefig("./charts/fixed_di.png")

print("Fixed income charts are done!")
