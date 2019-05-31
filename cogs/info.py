import discord
from discord.ext import commands
from cmcAPI import get_data


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


    @commands.command(name='info', brief='Command that retrieves information of coin.')
    async def coinInfo(self, ctx, coin):
        for item in get_data()['data']:
            cmc_rank = item['cmc_rank']
            name = item['name']
            symbol = item['symbol']
            price = item['quote']['USD']['price']
            percent_change_24h = item['quote']['USD']['percent_change_24h']
            if item['symbol'] == coin.upper():
                await ctx.send(f'```{coin.upper()}\nName: {name}\nSymbol: {symbol}\nCurrent rank: {cmc_rank}\nPrice: $ {round(price, 6)}\n```')
                if str(percent_change_24h).startswith('-'):
                    await ctx.send(f'```diff\n-Percent Change (24 Hrs): {percent_change_24h} %```')
                elif not str(percent_change_24h).startswith('-'):
                    await ctx.send(f'```diff\n+Percent Change (24 Hrs): {percent_change_24h} %```')

                    
    @commands.command(name='usd', brief='Command that retrieves USD value of coin.')
    async def getusd(self, ctx, coin):
        usdValue = dict()
        for item in get_data()['data']:
            symbol = item['symbol']
            price = item['quote']['USD']['price']
            percent_change_24h = item['quote']['USD']['percent_change_24h']
            if item['symbol'] == coin.upper():
                usdValue[symbol] = price
                await ctx.send(f'```Price of {coin.upper()} is $ {round(price, 2)}```') 
                if str(percent_change_24h).startswith('-'):
                    await ctx.send(f'```diff\n-Percent Change (24 Hrs): {percent_change_24h} %```')
                elif not str(percent_change_24h).startswith('-'):
                    await ctx.send(f'```diff\n+Percent Change (24 Hrs): {percent_change_24h} %```')


    @commands.command(name='addy', brief='Command that retrieves token address of coin.')
    async def tokenAddy(self, ctx, coin):
        try:
            for item in get_data()['data']:
                if item['symbol'] == coin.upper():
                    address = item['platform']['token_address']
                    await ctx.send(f'{address}')
        except:
            await ctx.send(f'Token Address for {coin.upper()} does not exist')    


def setup(client):
    client.add_cog(Info(client))
