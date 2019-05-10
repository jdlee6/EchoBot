from discord.ext import commands
import discord, requests, json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style
from mpl_finance import candlestick_ohlc
import datetime as dt 


# Define Moving Average Function
def movingaverage(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas


class Chart(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Set chart style and font
    style.use('ggplot')
    mpl.rcParams.update({'font.size': 9})


    # Split data from json into lists within an array
    @commands.command(name='chart', brief='Command that charts coin to BTC (Ticker)')
    async def graphData(self, ctx, coin, MA1=5, MA2=20):
        url = f'https://min-api.cryptocompare.com/data/histoday?fsym={coin}&tsym=BTC&limit=100'


        response = requests.get(url)
        source = response.text
        new_source = json.loads(source)


        # Method to obtain only integers from json dataset
        new_list = [', '.join(map(str, d.values())) for d in new_source['Data']]


        # Load data with numpy
        time, close, high, low, open, volumefrom, volumeto = np.loadtxt(new_list,
        delimiter=',',
        unpack=True)


        # Convert unix time
        dateconv = np.vectorize(dt.datetime.fromtimestamp)
        time = dateconv(time)


        # Define ax1 (subplot1 for candlestick chart)
        fig = plt.figure()
        ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
        plt.xlabel('Date')
        plt.ylabel('Satoshi Price')
        plt.title(coin)


        # Define ax2 (subplot2 for volume)
        ax2 = plt.subplot2grid((5,4), (4,0),  sharex=ax1, rowspan=1, colspan=4)
        ax2.bar(time, volumefrom, color='#498fff', alpha=0.3)
        ax2.grid(True)
        plt.ylabel('Volume')
        plt.xlabel('Date')


        # Get rid of volume ticks/labels
        ax2.axes.yaxis.set_ticklabels([])


        # Convert datetime.datetime(2019, 5, 3, 20, 0) by using mdates.date2num(time) --> 737138.83333333
        # and then format by using mdates.DateFormatter('%Y-%m-%d)
        time = mdates.date2num(time)
        new_format = mdates.DateFormatter('%Y-%m-%d')
        ax1.xaxis.set_major_formatter(new_format)


        # Create OHLC list, and append data from dataset
        x = 0
        y = len(time)
        ohlc = []
        while x < y:
            append_me = time[x], open[x], high[x], low[x], close[x], volumefrom[x]
            ohlc.append(append_me)
            x += 1


        # Define average 1 and average 2
        av1 = movingaverage(close, MA1)
        av2 = movingaverage(close, MA2)


        # Define starting point for Moving Averages
        sp = len(time[MA2-1:])


        # Plot data with candlestick_ohlc
        candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#40ec43', colordown='#fb3131')


        # Plot moving averages on candlestick_ohlc chart
        ax1.plot(time[-sp:], av1[-sp:], color='#7d60fd', alpha=0.7)
        ax1.plot(time[-sp:], av2[-sp:], color='#ff9830', alpha=0.7)


        # Tilt x axis labels for volume chart and hide the x axis of subplot 1
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)
        ax1.axes.get_xaxis().set_visible(False)
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.grid(True)


        # Labels for Simple Moving Averages
        plt.plot([], [], color='#7d60fd', label='5 Day SMA', linewidth=3)
        plt.plot([], [], color='#ff9830', label='20 Day SMA', linewidth=3)
        plt.subplots_adjust(left=0.15, bottom=0.19, right=0.97, top=0.94, wspace=0.2, hspace=0)
        plt.legend()


        # Save figure to cwd
        fig.savefig(coin+'.png')


        # Send our chart info via Discord bot
        file = discord.File(f'{coin}.png', filename=f'{coin}.png')
        await ctx.send(f'{coin}', file=file)


def setup(client):
    client.add_cog(Chart(client))
