import discord
from crafty_client import CraftyWeb
import re
from discord.ext import commands
import string

URL = "https://" # WebServer
API_TOKEN = "" # Crafty API Token
BOT_TOKEN = "" # Discord Bot Token
STARTUP_MESSAGE_ID = "" # Discord Startup Channel ID
craftyperms = "" # Role bot searches for and if have role then can execute admin commands

STARTUP_MESSAGE_ID_INT = int(STARTUP_MESSAGE_ID) # Converts STR to INT

cweb = CraftyWeb(URL, API_TOKEN)

client = discord.Client()

client = commands.Bot(command_prefix='!')
client.remove_command('help')

def convertTuple(tup):
    str =  " ".join(tup)
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
    sendstart = client.get_channel(STARTUP_MESSAGE_ID_INT) # channel to send start message
    author = await client.fetch_user(259875936852246528) # gets authors id

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
    await sendstart.send(embed=embedstartup) # sends startup meessage


@client.command()
async def send(ctx, arg, *arg4):
    strsend = convertTuple(arg4)
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        sendembed = discord.Embed(title="Crafty Command Execution", color=0x31c4b3)
        sendembed.add_field(name="Server sent to", value="ID " + arg, inline=True)
        sendembed.add_field(name="Command", value=strsend, inline=True)
        sendembed.add_field(name="Action Sucessful?", value=cweb.run_command(arg, strsend), inline=True)
        sendembed.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=sendembed)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def alert(ctx, *arg5):
    str = convertTuple(arg5)
    argexe = "5"
    alertas = "alert"
    output = (alertas + " " + str)
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        sendembedalert = discord.Embed(title="Crafty Alert Execution", color=0x31c4b3)
        sendembedalert.add_field(name="Command", value=str, inline=True)
        sendembedalert.add_field(name="Action Sucessful?", value=cweb.run_command(argexe, output), inline=True)
        sendembedalert.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=sendembedalert)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def backup(ctx, args):
    if "all" in args:
        embedbackup = discord.Embed(title="Crafty Backup Execution", color=0x31c4b3)
        embedbackup.add_field(name="Backup Server ID 1 Sucessful?", value=cweb.backup_server(1), inline=True)
        embedbackup.add_field(name="Backup Server ID 2 Sucessful?", value=cweb.backup_server(2), inline=True)
        embedbackup.add_field(name="Backup Server ID 3 Sucessful?", value=cweb.backup_server(3), inline=True)
        embedbackup.add_field(name="Backup Server ID 4 Sucessful?", value=cweb.backup_server(4), inline=True)
        embedbackup.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedbackup)

    else:
        embedbackup2 = discord.Embed(title="Crafty Backup Execution", color=0x31c4b3)
        embedbackup2.add_field(name="Sending Backup Request to ID" + args + " Sucessful?", value=cweb.backup_server(args), inline=True)
        embedbackup2.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedbackup2)

@client.command()
async def restart(ctx, argid):
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        embedrestart = discord.Embed(title="Crafty Restart Execution", color=0x31c4b3)
        embedrestart.add_field(name="Restart Server ", value="ID " + argid, inline=True)
        embedrestart.add_field(name="Action Sucessful?", value=cweb.restart_server(argid), inline=True)
        embedrestart.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedrestart)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def stop(ctx, argid):
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        embedstop = discord.Embed(title="Crafty Stop Execution", color=0x31c4b3)
        embedstop.add_field(name="Stop Server ", value="ID " + argid, inline=True)
        embedstop.add_field(name="Action Sucessful?", value=cweb.stop_server(argid), inline=True)
        embedstop.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedstop)

    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def start(ctx, argid):
    role = discord.utils.get(ctx.guild.roles, name=craftyperms)
    if role in ctx.author.roles:
        embedstart = discord.Embed(title="Crafty Start Execution", color=0x31c4b3)
        embedstart.add_field(name="Start Server ", value="ID " + argid, inline=True)
        embedstart.add_field(name="Action Sucessful?", value=cweb.start_server(argid), inline=True)
        embedstart.add_field(name="Requested by", value=ctx.message.author.mention, inline=True)
        await ctx.send(embed=embedstart)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def hostinfo(message):
    if message.author == client.user:
        return
    else:
        embedhoststatus = discord.Embed(title="Crafty Host Info", color=0x31c4b3)
        hostdata = cweb.get_host_stats_pc()
        hostcpu = re.findall(r'cpu_usage(.*?),',str(hostdata))
        punctuationwittdot = "#$%&'()*+,-/:;<=>?@[\]^_`{|}~"
        datastrip = str.maketrans("", "", punctuationwittdot)

        cpustripped = [w.translate(datastrip) for w in hostcpu]
        cpuassembled = " ".join(cpustripped)

        embedhoststatus.add_field(name="CPU", value="CPU Usage" + cpuassembled + "%", inline=False)

        hostmem = re.findall(r'mem_percent(.*?),',str(hostdata))
        hostmemused = re.findall(r'mem_usage(.*?),',str(hostdata))
        hostmemall = re.findall(r'mem_total(.*?),',str(hostdata))

        memstripped = [w.translate(datastrip) for w in hostmem]
        memassembled = " ".join(memstripped)

        memusedstripped = [w.translate(datastrip) for w in hostmemused]
        memusedassembled = " ".join(memusedstripped)

        memallstripped = [w.translate(datastrip) for w in hostmemall]
        memallassembled = " ".join(memallstripped)

        embedhoststatus.add_field(name="Memory Used", value="Memory Usage" + memassembled + "%" + memusedassembled + " Used out of" + memallassembled, inline=False)

        hostdisk = re.findall(r'disk_percent(.*?),',str(hostdata))
        hostdiskused = re.findall(r'disk_usage(.*?),',str(hostdata))
        hostdisktotal = re.findall(r'disk_total(.*?)}',str(hostdata))

        diskstripped = [w.translate(datastrip) for w in hostdisk]
        diskassembled = " ".join(diskstripped)

        diskusedstripped = [w.translate(datastrip) for w in hostdiskused]
        diskusedassembled = " ".join(diskusedstripped)

        disktotalstripped = [w.translate(datastrip) for w in hostdisktotal]
        disktotalassembled = " ".join(disktotalstripped)

        embedhoststatus.add_field(name="Disk Used", value="Disk Usage" + diskassembled + "%" + diskusedassembled + " Used out of" + disktotalassembled, inline=False)

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
        embedstatus = discord.Embed(title="Crafty Server Info", description="Lists all of the Servers and their Current Status", color=0x31c4b3)
        data = cweb.list_mc_servers()
        datastrip = str.maketrans("", "", string.punctuation)

        remove = string.punctuation
        remove = remove.replace(".", "")
        remove = remove.replace(":", "")
        pattern = r"[{}]".format(remove)
        datastripnew = str.maketrans("", "", pattern)

        moredata = cweb.get_host_stats_server()
        datavalues = ','.join(map(str, moredata))
        print(string.punctuation)
        datastripped = [w.translate(datastripnew) for w in datavalues]
        datavaluesassembled = ''.join(map(str, datastripped))
        print(datavaluesassembled)

        srvrunning = "Server running True"
        srvstopped = "Server running False crashed False"
        srvcrashed = "Server running False crashed True"




        embedstatus.add_field(name="Requested by", value=message.message.author.mention, inline=True)

        await message.channel.send(embed=embedstatus)



client.run(BOT_TOKEN)
