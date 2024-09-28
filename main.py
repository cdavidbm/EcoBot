import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy EcoBot, un bot de Discord que te dará ideas básicas de reciclaje.')

@bot.command()
async def ayuda(ctx):
    await ctx.send('Utiliza el simbolo / seguido de alguna de estas palabras para recibir mas información: vidrio, plastico, organicos')

@bot.command()
async def vidrios(ctx):
    await ctx.send('para reciclar vidrios, te recomiendo: \n - lavarlos \n - desecharlos en lugares especializados \n - no los quemes')

@bot.command()
async def enviar_imagen(ctx):
    with open('imagen.png', 'rb') as file:
        await ctx.send(file=discord.File(file, 'imagen.jpg'))

bot.run('TOKEN')



