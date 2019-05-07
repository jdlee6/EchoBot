import discord
from discord.ext import commands
from cmcAPI import data


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name='top10', brief='Command that retrieves the current top ten coins.')
    async def topten(self, ctx):
        i = 0
        print('The top ten coins:\n')
        for item in data['data']:
            rank = item['cmc_rank']
            name = item['name']
            symbol = item['symbol']
            i += 1
            await ctx.send(f'{rank} {name} {symbol}')
            if i == 10:
                await ctx.send('')
                break


    @commands.command(name='chartBTC', brief='Command that displays chart of coin to BTC (Ticker)')
    async def chartBTC(self, ctx, coin):
        for item in data['data']:
            if item['symbol'] == coin:
                await ctx.send(f'{coin} vs. BTC\nhttps://tradingview/chart{coin}BTC')


    @commands.command(name='chartUSD', brief='Command that displays chart of coin to USD (Ticker)')
    async def chartUSD(self, ctx, coin):
        for item in data['data']:
            if item['symbol'] == coin:
                await ctx.send(f'{coin} vs. USD\nhttps://tradingview/chart{coin}USD')


    @commands.command(name='info', brief='Command that retrieves information of coin. (Full name)')
    async def coinInfo(self, ctx, coin):
        for item in data['data']:
            cmc_rank = item['cmc_rank']
            name = item['name']
            symbol = item['symbol']
            price = item['quote']['USD']['price']
            percent_change_24h = item['quote']['USD']['percent_change_24h']
            if item['name'] == coin:
                await ctx.send(f'{coin}\nName: {name}\nSymbol: {symbol}\nCurrent rank: {cmc_rank}\nPrice: $ {round(price, 6)}\nPercent Change (24 Hrs): {round(percent_change_24h, 2)} %\n')


    @commands.command(name='usd', brief='Command that retrieves USD value of coin. (Ticker)')
    async def getusd(self, ctx, coin):
        usdValue = dict()
        for item in data['data']:
            symbol = item['symbol']
            price = item['quote']['USD']['price']
            if item['symbol'] == coin:
                usdValue[symbol] = price
                await ctx.send(f'Price of {coin} is $ {round(price, 2)}') 


    @commands.command(name='addy', brief='Command that retrieves token address of coin. (Ticker)')
    async def tokenAddy(self, ctx, coin):
        try:
            for item in data['data']:
                if item['symbol'] == coin:
                    address = item['platform']['token_address']
                    await ctx.send(f'{address}')
        except:
            await ctx.send(f'Token Address for {coin} does not exist')    


def setup(client):
    client.add_cog(Info(client))