import discord
from discord.ext import commands
from cmcAPI import get_data
from cogs.convert import usd


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name='top10', brief='Command that retrieves the current top ten coins.')
    async def topten(self, ctx):
        i = 0
        print('The top ten coins:\n')
        for item in get_data()['data']:
            rank = item['cmc_rank']
            name = item['name']
            symbol = item['symbol']
            i += 1
            await ctx.send(f'{rank} {name} {symbol}')
            if i == 10:
                await ctx.send('')
                break


    @commands.command(name='info', brief='Command that retrieves name, symbol, rank, price of coin.')
    async def coinInfo(self, ctx, coin):
        x = usd('BTC')
        y = usd('ETH')
        z = usd(coin.upper())
        gValue = (z/y)
        sValue = (z/x)
        for item in get_data()['data']:
            cmc_rank = item['cmc_rank']
            name = item['name']
            symbol = item['symbol']
            price = item['quote']['USD']['price']
            percent_change_24h = item['quote']['USD']['percent_change_24h']
            if coin.upper() == item['symbol'] :
                await ctx.send(f'```{coin.upper()}\nName: {name}\nSymbol: {symbol}\nCurrent rank: {cmc_rank}\nPrice: $ {round(price, 6)}\nSatoshi: {"{:.8f}".format(float(sValue))}\nGwei: {"{:.8f}".format(float(gValue))}```')
                if str(percent_change_24h).startswith('-'):
                    await ctx.send(f'```diff\n-Percent Change (24 Hrs): {percent_change_24h} %```')
                elif not str(percent_change_24h).startswith('-'):
                    await ctx.send(f'```diff\n+Percent Change (24 Hrs): {percent_change_24h} %```')


    @commands.command(name='addy', brief='Command that retrieves token address of coin.')
    async def tokenAddy(self, ctx, coin):
        try:
            for item in get_data()['data']:
                if coin.upper() == item['symbol']:
                    address = item['platform']['token_address']
                    await ctx.send(f'{address}')
        except:
            await ctx.send(f'Token Address for {coin.upper()} does not exist') 


def setup(client):
    client.add_cog(Info(client))