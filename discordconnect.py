import re
import string

import discord
from discord.ext import commands

from crafty_client import CraftyWeb

URL = ""  # WebServer
API_TOKEN = ""  # Crafty API Token
BOT_TOKEN = ""  # Discord Bot Token
logging_channel = ""  # Discord Startup Channel ID
craftyperms = ""  # Role bot searches for and if have role then can execute admin commands

# Enable Alert command, a yes or no answer THIS REQUIRES YOU TO HAVE A PROXY SERVER
enablealert = "no"

# What is the proxy server id?
proxyid = "0"

client = discord.Client()

cweb = CraftyWeb(URL, API_TOKEN)

client = commands.Bot(command_prefix='!')
client.remove_command('help')


def convertTuple(tup):
    str = " ".join(tup)
    return str


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


@client.event
async def on_ready():
    logs = client.get_channel(int(logging_channel))  # channel to send start message
    author = await client.fetch_user(259875936852246528)
    print("Bot is ready!")
    print("Logged in as: " + client.user.name)
    print("Bot ID: " + str(client.user.id))
    for guild in client.guilds:
        print("Connected to server: {}".format(guild))
    await client.change_presence(activity=discord.Game(name="!help"))
    embedstartup = discord.Embed(title="Starting Crafty Bot", color=0x37cdaf)
    embedstartup.add_field(name="Logged in as ", value="Logged in as: " + client.user.name, inline=True)
    embedstartup.add_field(name="Bot ID", value="Bot ID: " + str(client.user.id), inline=True)
    for guild in client.guilds:
        embedstartup.add_field(name="Connected To Servers", value="Connected to server: {}".format(guild), inline=True)
        print("Connected to server: {}".format(guild))
    authorstring = str(author)
    embedstartup.set_footer(text="Created by " + authorstring)
    await logs.send(embed=embedstartup)  # sends startup meessage


@client.command()
async def send(ctx, arg, *arg4):
    logs = client.get_channel(int(logging_channel))  # channel to send log message
    strsend = convertTuple(arg4)
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        sendembed = discord.Embed(title="Crafty Command Execution", color=0x31c4b3)
        sendembed.add_field(name="Server sent to", value="ID " + arg, inline=True)
        sendembed.add_field(name="Command", value=strsend, inline=True)
        sendembed.add_field(name="Action Sucessful?", value=cweb.run_command(arg, strsend), inline=True)
        sendembed.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=sendembed)
        await logs.send(embed=sendembed)
    else:
        await ctx.channel.send("You do not have permission to run this command.")


@client.command()
async def alert(ctx, *arg5):
    logs = client.get_channel(int(logging_channel))  # channel to send log message
    str = convertTuple(arg5)
    output = ("alert " + str)
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if enablealert == "yes":
        if role in ctx.author.roles:
            sendembedalert = discord.Embed(title="Crafty Alert Execution", color=0x31c4b3)
            sendembedalert.add_field(name="Command", value=str, inline=True)
            sendembedalert.add_field(name="Action Sucessful?", value=cweb.run_command(proxyid, output), inline=True)
            sendembedalert.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
            await ctx.send(embed=sendembedalert)
            await logs.send(embed=sendembedalert)
        else:
            await ctx.channel.send("You do not have permission to run this command.")
    else:
        await ctx.channel.send("The Alert Command has been disabled / not setup " + ctx.message.author.mention)


@client.command()
async def backup(ctx, args):
    logs = client.get_channel(int(logging_channel))  # channel to send log message
    if "all" in args:
        embedbackup = discord.Embed(title="Crafty Backup Execution", color=0x31c4b3)
        # for the backup all command list your servers like the example provided below
        embedbackup.add_field(name="Backup Server ID 1 Sucessful?", value=cweb.backup_server(1), inline=True)
        # -------------------------------------------------------------------------
        embedbackup.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedbackup)
        await logs.send(embed=embedbackup)

    else:
        embedbackup2 = discord.Embed(title="Crafty Backup Execution", color=0x31c4b3)
        embedbackup2.add_field(name="Sending Backup Request to ID" + args + " Sucessful?",
                               value=cweb.backup_server(args), inline=True)
        embedbackup2.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedbackup2)
        await logs.send(embed=embedbackup2)


@client.command()
async def restart(ctx, argid):
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        logs = client.get_channel(int(logging_channel))  # channel to send log message
        embedrestart = discord.Embed(title="Crafty Restart Execution", color=0x31c4b3)
        embedrestart.add_field(name="Restart Server ", value="ID " + argid, inline=True)
        embedrestart.add_field(name="Action Sucessful?", value=cweb.restart_server(argid), inline=True)
        embedrestart.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedrestart)
        await logs.send(embed=embedrestart)
    else:
        await ctx.channel.send("You do not have permission to run this command.")


@client.command()
async def stop(ctx, argid):
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        logs = client.get_channel(int(logging_channel))  # channel to send log message
        embedstop = discord.Embed(title="Crafty Stop Execution", color=0x31c4b3)
        embedstop.add_field(name="Stop Server ", value="ID " + argid, inline=True)
        embedstop.add_field(name="Action Sucessful?", value=cweb.stop_server(argid), inline=True)
        embedstop.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedstop)
        await logs.send(embed=embedstop)

    else:
        await ctx.channel.send("You do not have permission to run this command.")


@client.command()
async def start(ctx, argid):
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        logs = client.get_channel(int(logging_channel))  # channel to send log message
        embedstart = discord.Embed(title="Crafty Start Execution", color=0x31c4b3)
        embedstart.add_field(name="Start Server ", value="ID " + argid, inline=True)
        embedstart.add_field(name="Action Sucessful?", value=cweb.start_server(argid), inline=True)
        embedstart.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedstart)
        await logs.send(embed=embedstart)
    else:
        await ctx.channel.send("You do not have permission to run this command.")


@client.command()
async def hostinfo(message):
    if message.author == client.user:
        return
    else:
        embedhoststatus = discord.Embed(title="Crafty Host Info", color=0x31c4b3)
        hostdata = cweb.get_host_stats_pc()

        nodotto = string.punctuation
        nodotto = remove.replace(".", "")
        datastripnodot = str.maketrans("", "", r"[{}]".format(nodotto))

        datastrip = str.maketrans("", "", datastripnodot)

        cpuassembled = " ".join([w.translate(datastrip) for w in re.findall(r'cpu_usage(.*?),', str(hostdata))])

        embedhoststatus.add_field(name="CPU", value="CPU Usage" + cpuassembled + "%", inline=False)

        hostmem = re.findall(r'mem_percent(.*?),', str(hostdata))
        hostmemused = re.findall(r'mem_usage(.*?),', str(hostdata))
        hostmemall = re.findall(r'mem_total(.*?),', str(hostdata))

        memassembled = " ".join([w.translate(datastrip) for w in hostmem])

        memusedassembled = " ".join([w.translate(datastrip) for w in hostmemused])

        memallassembled = " ".join([w.translate(datastrip) for w in hostmemall])

        embedhoststatus.add_field(name="Memory Used",
                                  value="Memory Usage" + memassembled + "%" + memusedassembled + " Used out of" + memallassembled,
                                  inline=False)

        hostdisk = re.findall(r'disk_percent(.*?),', str(hostdata))
        hostdiskused = re.findall(r'disk_usage(.*?),', str(hostdata))
        hostdisktotal = re.findall(r'disk_total(.*?)}', str(hostdata))

        diskassembled = " ".join([w.translate(datastrip) for w in hostdisk])

        diskusedassembled = " ".join([w.translate(datastrip) for w in hostdiskused])

        disktotalassembled = " ".join([w.translate(datastrip) for w in hostdisktotal])

        embedhoststatus.add_field(name="Disk Used",
                                  value="Disk Usage" + diskassembled + "%" + diskusedassembled + " Used out of" + disktotalassembled,
                                  inline=False)

        embedhoststatus.add_field(name="Requested by", value=message.message.author.mention, inline=True)
        await message.channel.send(embed=embedhoststatus)


@client.command()
async def ping(message):
    await message.channel.send('Pong! {0}'.format(round(client.latency, 1)) + " Secounds")


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Crafty Help Commands", color=0x31c4b3)
    embed.add_field(name="Ping", value="!ping", inline=False)
    embed.add_field(name="Server Info", value="!serverinfo", inline=False)
    embed.add_field(name="Host Info", value="!hostinfo", inline=False)
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        embed.add_field(name="**ADMIN ONLY**", value="**ADMIN ONLY**", inline=False)
        embed.add_field(name="Start Server", value="!start ID", inline=False)
        embed.add_field(name="Stop Server", value="!stop ID", inline=False)
        embed.add_field(name="Restart Server", value="!restart ID", inline=False)
        embed.add_field(name="Backup Server", value="!backup ID", inline=False)
        embed.add_field(name="Send Command", value="!send [id] [command]", inline=False)
    embed.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
    embed.set_footer(text="Created by CatsAreDaBest#3054")
    await ctx.send(embed=embed)


@client.command()
async def serverinfo(message):
    embedstatus = discord.Embed(title="Crafty Server Info",
                                description="Lists all of the Servers and their Current Status", color=0x31c4b3)

    # this is to list mc servers and their current status
    data = cweb.list_mc_servers()

    # variable for removing punctuation for the status
    datastrip = str.maketrans("", "", string.punctuation)

    # making the variable that has all the punctuation except for : and ,
    remove = string.punctuation
    remove = remove.replace(".", "")
    remove = remove.replace(":", "")
    datastripnew = str.maketrans("", "", r"[{}]".format(remove))

    # grabs the status of mc servers and formats them by removing punctuation except for : and ,
    datavaluesassembled = ''.join(
        map(str, [w.translate(datastripnew) for w in ','.join(map(str, cweb.get_host_stats_server()))]))

    srvrunning = "Server running True"  # this is just defining variables
    srvstopped = "Server running False crashed False"  # this is just defining variables
    srvcrashed = "Server running False crashed True"  # this is just defining variables

    # -------------------------------------------------------------------------
    
    # PLEASE LOOK AT FURTHEREXAMPLES.py OR READ THE INSTRUCTIONS FIRST
    # -------------------------------------------------------------------------

    # sends them all out
    await message.channel.send(embed=embedstatus)


client.run(BOT_TOKEN)
