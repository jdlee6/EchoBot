import discord
from discord.ext import commands
from cmcAPI import get_data


def usd(coin):
    usdValue = dict()
    for item in get_data()['data']:
        symbol = item['symbol']
        price = item['quote']['USD']['price']
        if coin.upper() == item['symbol']:
            usdValue[symbol] = price
            return price


class Convert(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    #  Converts amount of any Coin to USD
    @commands.command(name='toUSD', brief='Command that converts any amount of coin to USD.')
    async def toUSD(self, ctx, amnt, coin):
        try:
            x = float(amnt)
            y = usd(coin.upper())
            totalUSD = x*y
            await ctx.send(f'{amnt} {coin.upper()} is $' + str(round(float(totalUSD), 2)))
        except Exception as e:
            print(f'{e}')

            
    #  Convert USD Amount to BTC
    @commands.command(name='toBTC', brief='Command that converts USD to BTC.')
    async def convertToBTC(self, ctx, usdAmnt):
        x = usd('BTC')
        await ctx.send(f'${usdAmnt} converted to BTC: ' + str(int(usdAmnt) / x))
        

    #  Convert USD Amount to LTC
    @commands.command(name='toLTC', brief='Command that converts USD to LTC.')
    async def convertToLTC(self, ctx, usdAmnt):
        y = usd('LTC')
        await ctx.send(f'${usdAmnt} converted to LTC: ' + str(int(usdAmnt) / y))


    # Convert USD Amount to ETH
    @commands.command(name='toETH', brief='Command that converts USD to ETH.')
    async def convertToETH(self, ctx, usdAmnt):
        z = usd('ETH')
        await ctx.send(f'${usdAmnt} converted to ETH: ' + str(int(usdAmnt) / z))


def setup(client):
    client.add_cog(Convert(client))
