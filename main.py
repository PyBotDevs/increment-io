# Imports
import os
import time
import os.path
import discord
import datetime
import requests
import json
from discord.ext import commands
from discord.ext.commands import *
from discord.ext import tasks
from keep_alive import keep_alive

# Startup and Variables
ids = [
    816941773032390676,
    738290097170153472,
    705462972415213588,
    706697300872921088
]
console = False
log = True
if os.name == 'nt': os.system('cls')
else: os.system('clear')
print('Checking for rate limit errors...')
r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit error found: {int(r.headers['Retry-After']) / 60} minutes left")
    raise(SystemExit)
except: print("No rate limit found.")
time.sleep(1)
intents = discord.Intents.all()
errHandlerVer = 'v2.4'
botVer = 'v1.0'
if os.name == 'nt': os.system('cls')
else: os.system('clear')
owner = '@notsniped'
homedir = os.path.expanduser("~")
client = commands.Bot(command_prefix="+", intents=intents)
global startTime
startTime = time.time()
client.remove_command('help')
theme_color = 0xffbd59
color_success = 0x77b255
color_fail = 0xc92424
rootdir = 'C://Users//dhruvbhat//OneDrive//Desktop//increment.io'
loggerHandler_path = 'botLog/log.txt'
errorHandler_path = 'botLog/errors.txt'
correctnumber = {}

class colors:
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

with open('database/count.json', 'r') as f: count = json.load(f)
with open('database/configuration/countchannel.json', 'r') as f: countchannel = json.load(f)
with open('database/configuration/warning.json', 'r') as f: warnmsg = json.load(f)
with open('database/configuration/autoreactions.json', 'r') as f: autoreactions = json.load(f)

def savedata():
    with open('database/count.json', 'w+') as f: json.dump(count, f)
    with open('database/configuration/countchannel.json', 'w+') as f: json.dump(countchannel, f)
    with open('database/configuration/autoreactions.json', 'w+') as f: json.dump(autoreactions, f)

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

# Events
@client.event
async def on_ready():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=f"the epic comeback. (+help) | {str(len(client.guilds))} guilds"
        )
    )
    print('Bot is online')
    print('==================')
    print('------------------')
    print('Bot Info')
    print(f'Bot version: {colors.cyan}{botVer}{colors.end}')
    print(f'Error handler version: {colors.cyan}{errHandlerVer}{colors.end}')
    print(f"Username: {colors.green}{client.user.name}{colors.end}")
    print(f"Bot id: {colors.green}{client.user.id}{colors.end}")
    print(f"Developer name: {colors.green}{owner}{colors.end}")
    print('==================')
    print('Bot config:')
    print('------------------')
    print(f'Ping: {round(client.latency * 1000)}')
    print('------------------')
    boot = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    print(f'Startup time: {boot}')
    print('------------------')
    print(f'Server count: {str(len(client.guilds))}')
    print('------------------')
    if bool(log) == True:
        print(f'Logging: {colors.green}{log}{colors.end}')
        print('==================')
    else:
        print(f'Logging: {colors.red}{log}{colors.end}')
        print('==================')
        pass
    print('Bot admins')
    print('------------------')
    print(colors.cyan)
    for id in ids: print(id)
    print(colors.end)
    print('==================')
    print('System info')
    print('Running as: ' + str(os.system("whoami")))
    print('------------------')
    print('Os name: ' + str(os.name))
    print('------------------')
    print('Current working dir: ' + str(os.getcwd()))
    print(f'System directory: {homedir}')
    print('------------------')
    try:
        botpath = 'main.py'
        botsize = os.path.getsize(botpath)
        print(f'Bot file size: {botsize}b')
        print('------------------')
    except FileNotFoundError:
        if os.name == 'posix':
            try:
                print('Bot file size: ' + os.path.getsize('main.py'))
                print('------------------')
            except FileNotFoundError:
                print('Bot file size: ' + os.path.getsize(str(os.getcwd() + '\\main.py')))
                print('------------------')

# Error Handler
@client.event
async def on_command_error(ctx, error):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if isinstance(error, discord.ext.commands.CommandNotFound):
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}/WARN] Ignoring exception at CommandNotFound. Details: This command does not exist.\n')
                f.close()
                print(f'{colors.red}[{current_time}/WARN] Ignoring exception at CommandNotFound. Details: This command does not exist.{colors.end}')
        else: pass
    if isinstance(error, discord.ext.commands.CommandOnCooldown):
        await ctx.send(f':warning: This command is currently on cooldown, try after **{str(datetime.timedelta(seconds=int(round(error.retry_after))))}**', delete_after=5)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}/WARN] Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown.\n')
                f.close()
                print(f'{colors.red}[{current_time}/WARN] Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown.{colors.end}')
        else: pass
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
        await ctx.send(':x: Your command has missing required argument(s).', delete_after=3)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}/WARN] Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.\n')
                f.close()
                print(f'{colors.red}[{current_time}/WARN] Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.{colors.end}')
        else: pass
    if isinstance(error, discord.ext.commands.MissingPermissions):
        await ctx.send(':x: You don\'t have permissions to use this command.', delete_after=3)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}/WARN] Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.\n')
                f.close()
                print(f'{colors.red}[{current_time}/WARN] Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.{colors.end}')
        else: pass
    if isinstance(error, discord.ext.commands.BadArgument):
        await ctx.send(':x: Invalid argument.', delete_after=3)
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}/WARN] Ignoring exception at BadArgument.\n')
                f.close()
                print(f'{colors.red}[{current_time}/WARN] Ignoring exception at BadArgument.{colors.end}')
        else: pass
    if isinstance(error, discord.ext.commands.BotMissingPermissions):
        await ctx.send(':x: I don\'t have permissions to do this. Kindly manage my role permissions to get this feature working.')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}/WARN] Ignoring exception at BotMissingPermissions.\n Details: The bot doesn\'t have the required permissions.\n')
                f.close()
                print(f'{colors.red}[{current_time}/WARN] Ignoring exception at BotMissingPremissions. Details: The bot doesn\'t have the required permissions.{colors.end}')
        else: pass

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message(message):
    global count
    if str(message.channel.id) not in count:
        count[str(message.channel.id)] = 1
        savedata()
    if str(message.guild.id) not in countchannel:
        countchannel[str(message.guild.id)] = 0
        savedata()
    if str(message.guild.id) not in warnmsg:
        warnmsg[str(message.guild.id)] = 0
        savedata()
    if str(message.guild.id) not in autoreactions:
        autoreactions[str(message.guild.id)] = 1
        savedata()
    if not message.author.bot:
        if message.channel.id == countchannel[str(message.guild.id)]:
            try:
                if int(message.content) == count[str(message.channel.id)]:
                    count[str(message.channel.id)] += 1
                    if autoreactions[str(message.guild.id)] == 1: await message.add_reaction('☑')
                    savedata()
                else:
                    if autoreactions[str(message.guild.id)] == 1: await message.add_reaction('❌')
                    await message.reply(f'**Wrong!** The next number is `{count[str(message.channel.id)]}`', mention_author = False, delete_after = 3)
            except:
                if autoreactions[str(message.guild.id)] == 1: await message.add_reaction('⚠')
    await client.process_commands(message)

# Commands
@client.command()
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f'This session has been running for **{uptime}**')

@client.command(aliases=['commands'])
async def help(ctx):
    emb = discord.Embed(title=f'increment.io Commands',  description=f'I am a counting bot who looks for numbers and makes sure that the count doesn\'t get messed up. If you want help on commands or want a more organized view, check https://notsniped.github.io/increment.io/commands\n :warning: This bot is still WIP. Some commands/features may not work as expected.\n\n**Prefix:** ```Main Prefix: +```\n**Information:** ```+help, +ping, +stats, +serverstats,+credits```\n**Counting:** ```+setchannel, +numberonly [on/off], +reactions [on/off], +setnumber [number], +resetcount```', color=theme_color)
    await ctx.send(embed = emb)

@client.command(aliases=['pong'])
async def ping(ctx):
    await ctx.send(f':ping_pong: Pong! In **{round(client.latency * 1000)}ms**.')

@client.command()
async def credits(ctx):
    emb = discord.Embed(title='Bot Credits', description='Owner: <@!738290097170153472>\nHelpers: <@!706697300872921088>, <@!705462972415213588>',color=theme_color)
    emb.set_footer(text='increment.io >> https://notsniped.github.io/increment.io')
    await ctx.send(embed=emb)

@client.command()
async def serverstats(ctx):
    servericon = ctx.guild.icon_url
    setchannelstats = countchannel[str(ctx.guild.id)]
    setchannelmaxcount = count[setchannelstats]
    emb12 = discord.Embed(title='This Server\'s Stats', color=theme_color)
    emb12.add_field(name='Count Channel', value=f'<#{setchannelstats}>')
    emb12.add_field(name='Current Count', value=setchannelmaxcount)
    emb12.set_thumbnail(url=servericon)
    await ctx.send(embed = emb12)

# Count Commands
@client.command()
@commands.has_permissions(administrator = True)
async def setchannel(ctx):
    try:
        countchannel[str(ctx.guild.id)] = ctx.channel.id
        savedata()
        await ctx.send(f':white_check_mark: <#{channel_to_set}> set as counting channel.')
    except: await ctx.send(':x: Unable to set count channel. Try again later.')

@client.command()
@commands.has_permissions(administrator = True)
async def reactions(ctx, setting:str):
    if setting == 'on':
        if autoreactions[str(ctx.guild.id)] == 1: await ctx.send(':warning: This feature is already enabled.')
        else:
            autoreactions[str(ctx.guild.id)] = 1
            savedata()
            await ctx.send(f':white_check_mark: Turned **on** count reactions.')
    elif setting == 'off':
        if autoreactions[str(ctx.guild.id)] == 0: await ctx.send(':warning: This feature is already disabled')
        else:
            autoreactions[str(ctx.guild.id)] = 0
            savedata()
            await ctx.send(f':white_check_mark: Turned **off** count reactions.')
    else: await ctx.send(f'\'{setting}\' is not a valid option. You can choose between `on` and `off`')

@client.command(aliases=['setnum'])
async def setnumber(ctx, arg1:int):
    if arg1 < 1: raise(discord.ext.commands.BadArgument)
    else:
        count[str(ctx.channel.id)] = arg1
        savedata()
        await ctx.reply(f':white_check_mark: Count set to `{count[str(ctx.channel.id)]}`')

@client.command(aliases=['resetnumber', 'reset', 'resetnum'])
async def resetcount(ctx):
    count[str(ctx.channel.id)] = 1
    savedata()
    await ctx.reply(':white_check_mark: Count successfully reset back to `1`')

# Client initialization
keep_alive()
client.run('')  # Insert your bot token here
