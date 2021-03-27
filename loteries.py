import discord
from discord.ext import commands
import random
import time
import asyncio

#BLANK CHARACTER >᲼᲼᲼᲼᲼᲼<

client = commands.Bot(command_prefix = "l!")

#Deleted commands
client.remove_command("help")

#Help

@client.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
       colour = discord.Colour.blue()
    )

    embed.set_author(name= "HELP")
    embed.add_field(name="```INFO```" , value="᲼᲼᲼᲼᲼", inline=True)
    embed.add_field(name="**l!help**" , value="*Shows this message*", inline=False)
    embed.add_field(name="**l!ping**" , value="*Returnes Pong!*", inline=False)
    embed.add_field(name="**l!loterie**" , value="*Randomly chooses 6 numbers between 1 and 40 (numbers can be the same!)*", inline=False)

    await ctx.send(embed=embed)
#BOT READY

@client.event
async def on_ready():
    print("Bot is ready!")



#PING COMMAND

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")



#Loterie commands

@client.command()
async def loterie(ctx):
    liczba1 = random.randint(1, 40)
    liczba2 = random.randint(1, 40)
    liczba3 = random.randint(1, 40)
    liczba4 = random.randint(1, 40)
    liczba5 = random.randint(1, 40)
    liczba6 = random.randint(1, 40)
    await ctx.send("**---------------------------------------**")
    await ctx.send("**Loterie will start soon!**")
    await ctx.send("**---------------------------------------**")
    time.sleep(3)
    await ctx.send("**GOOD LUCK EVERYONE!**")
    await ctx.send("**---------------------------------------**")
    time.sleep(5)
    await ctx.send(f"**Numbers:** ```{liczba1} {liczba2} {liczba3} {liczba4} {liczba5} {liczba6}```")
    await ctx.send("**---------------------------------------**")

client.run("ODI1MzQwMzgwNzg2MzI3NTYy.YF8gIA.fn_Ylzxcw5gPXQdq1eMq5XrxnRk")
