import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola! Soy EcoBot, un bot de Kodland inspirado en "El Libro de Python" que te dará ideas básicas de reciclaje.')

@bot.command()
async def ayuda(ctx):
    await ctx.send('Utiliza el simbolo / seguido de alguna de estas palabras para recibir más información: vidrio, plástico, orgánicos')

@bot.command()
async def vidrios(ctx):
    await ctx.send('Para reciclar vidrios, te recomiendo: \n - lavarlos \n - desecharlos en lugares especializados \n - no los quemes')

@bot.command()
async def plasticos(ctx):
    await ctx.send('Para reciclar plástico, te recomiendo: \n - limpiar los envases \n - separarlos por tipo \n - llevarlos a centros de reciclaje')

@bot.command()
async def organicos(ctx):
    await ctx.send('Para reciclar desechos orgánicos, te recomiendo: \n - compostar los restos de comida \n - evitar el uso de plásticos \n - utilizar contenedores específicos para orgánicos')

@bot.command()
async def el_libro_de_python(ctx):
    with open('imagen.png', 'rb') as file:
        await ctx.send(file=discord.File(file, 'imagen.jpg'))

@bot.command()
async def enviar_imagen_aleatoria(ctx):
    carpeta_imagenes = 'ruta/a/tu/carpeta'
    imagenes = os.listdir(carpeta_imagenes)
    imagen_seleccionada = random.choice(imagenes)
    ruta_imagen = os.path.join(carpeta_imagenes, imagen_seleccionada)
    
    with open(ruta_imagen, 'rb') as file:
        await ctx.send(file=discord.File(file, imagen_seleccionada))

bot.run('TOKEN')
