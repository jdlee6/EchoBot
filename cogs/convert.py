import discord
from discord.ext import commands
from cmcAPI import data


def usd(coin):
    usdValue = dict()
    for item in data['data']:
        symbol = item['symbol']
        price = item['quote']['USD']['price']
        if item['symbol'] == coin:
            usdValue[symbol] = price
            return price


class Convert(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    #  Converts amount of any Coin to USD
    @commands.command(name='toUSD', brief='Command that converts any amount of coin to USD')
    async def toUSD(self, ctx, amnt, coin):
        try:
            x = float(amnt)
            y = usd(coin)
            totalUSD = x*y
            await ctx.send(f'{amnt} {coin} is $' + str(round(float(totalUSD), 2)))
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


    # Converts coin's USD value into Satoshi (BTC Value)
    @commands.command(brief='Command that converts USD value of coin to satoshi value.')
    async def sat(self, ctx, coin):
        try:
            x = usd('BTC')
            y = usd(coin)
            sValue = (y/x)
            for item in data['data']:
                if coin == item['symbol']:
                    await ctx.send(f'The satoshi value of {coin} is: '+"{:.8f}".format(float(sValue)))
        except:
            await ctx.send(f'Error! {coin} doesn\'t exist!')


    # Convert coin's USD value to into Gwei (ETH Value)
    @commands.command(brief='Command that converts USD value of coin to gwei value.')
    async def gwei(self, ctx, coin):
        try:
            x = usd('ETH')
            y = usd(coin)
            sValue = (y/x)
            for item in data['data']:
                if coin == item['symbol']:
                    await ctx.send(f'The gwei value of {coin} is: '+"{:.8f}".format(float(sValue)))
        except:
            await ctx.send(f'Error! {coin} doesn\'t exist!')


def setup(client):
    client.add_cog(Convert(client))
