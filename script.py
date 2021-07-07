
import random
import discord
from discord.ext import tasks
import os 
from discord.ext import commands, tasks
from itertools import cycle
import distutils


client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def ping(ctx):
    await ctx.send (f'Pong!{round(client.latency*10000)}ms')



@client.command(aliases =['8ball'])
async def _8ball(ctx,*,question ):
    responses =[ "It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount: int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def example(ctx):
    await ctx.send (f'Hi im {ctx.author}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

@clear.error
async def clear_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send ('Please specify an amount of messages to delete.')

@tasks.loop(seconds=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run('ODUyNDg0OTcyNDU4OTM0Mjgz.YMHgfw.qbjyZvzO7hhElR9K9lXpCE5MH_4')
