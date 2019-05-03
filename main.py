import discord
from discord.ext import commands
from discord import Game


TOKEN= 'INSERT TOKEN HERE'
BOT_PREFIX = ['!', '?']


description = '''EchoBot is a Discord bot designed to retrieve cryptocurrency data and to convert various currencies into their relative satoshi/gwei values. This program is designed to obtain real time data from Coinmarketcap.com which implements REST APIs. Use either a ! or ? as the command prefix. The creator of this program is "jdlee6" and the source for the bot can be found at: https://github.com/jdlee6/EchoBot'''
client = commands.Bot(command_prefix=BOT_PREFIX, description=description)


# Setting up COG extensions
extensions = ['cogs.convert', 'cogs.info']


# Log in
@client.event
async def on_ready():
    print('Bot Online')


    await client.change_presence(activity=Game(name="with Finesse"))
    print('Logged in as ' + client.user.name)


    print('Current servers: ')
    for guild in client.guilds:
        print(guild.name, guild.id)


# Manually loading and unloading COGs
@client.command(name='load', hidden=True, brief='Command to load a module')
async def load(extension):
    for extension in extensions:
        try:
            client.load_extension(extensions)
        except Exception as e:
            print(f'{extension} cannot be loaded. {e}')


@client.command(name='unload', hidden=True, brief='Command to unload a module')
async def unload(extension):
    for extension in extensions:
        try:
            client.unload_extension(extension)
        except Exception as e:
            print(f'{extension} cannot be unloaded. {e}')


# Finalizing COG extensions
if __name__ == "__main__":
   for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'Loaded {extension}')
        except Exception as error:
            print(f'Failed to load extension {extension}.')


client.run(TOKEN)   
