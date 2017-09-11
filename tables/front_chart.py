######################################################################
## script to draw first page chart
## initial date: 31/01/2017
######################################################################
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sea

df = pd.read_excel("./data/indicators_input.xlsx", sheetname='chart',
                   index_col=0, parse_cols="A:B",
                   dayfirst=True, usecols=[0, 1]).dropna()
df.columns = ["DI Jan/21"]

def gen_chart(df, title, y_title, date_ini):
    """
    chart for the front page
    """
    global dfinal
    dfinal = df[df.index >= date_ini]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # data
    dfinal.plot(ax=ax, kind='line', color='red',
                linewidth=3, label="DI")
    # labels
    for label in ax.xaxis.get_ticklabels():
        label.set_fontsize(20)
    for label in ax.yaxis.get_ticklabels():
        label.set_fontsize(20)
    ax.set_title(title, dict(fontsize=30))
    ax.set_ylabel(y_title, dict(fontsize=20))
    ax.set_xlabel('', dict(fontsize=14))
    for label in ax.xaxis.get_ticklabels():
        label.set_fontsize(18)

    #frame
    ax.legend_.remove()
    fig.tight_layout()
    return fig


##
if __name__ =='__main__':
    date_ini = "2017-02-01"
    fig = gen_chart(df, "DI Jan/21", "", date_ini)
    fig.savefig('./charts/front_chart.png')
    print ("Front Chart is done!")
