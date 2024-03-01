import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def mem(ctx):
    with open('img/sigma.png', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('img/iphone-20.png', 'rb') as f2:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f2)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('img/tele.png', 'rb') as f3:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f3)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def animals_mems(ctx):
    with open(f'animals/{img_name}', 'rb') as f:
            picture = discord.File(f)

bot.run("blablabla")
