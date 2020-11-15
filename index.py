import discord
import aiohttp
from discord.ext import commands
import time
import json

with open('config.json') as json_file:
    data = json.load(json_file)

URL = data["crafty_url"]
API_TOKEN = data["api_token"]
BOT_TOKEN = data["bot_token"]
log_channel = data["log_channel"]
admin_role = data["admin_role"]
prefix = data["prefix"]
if data["ssl_check"] == True:
    ssl_check = True
else:
    ssl_check = False

client = discord.Client()
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

async def server_valid(ctx, serverid):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
            async with session.get(f'{URL}/api/v1/server_stats?token={API_TOKEN}') as resp:
                data = await resp.json()
    except aiohttp.ClientConnectorError:
        await ctx.send("Unable to connect to Crafty Controller")
        return "CError"
    a = "Invalid"
    for i in data["data"]:
        if i["id"] == serverid:
            a = "Valid"
    return a

@client.event
async def on_ready():
    logs = client.get_channel(log_channel)
    print("Bot is ready!")
    print("Logged in as: " + client.user.name)
    print("Bot ID: " + str(client.user.id))
    await client.change_presence(activity=discord.Game(name="!help"))
    await logs.send("Crafty Bot Started")

@client.command()
async def send(ctx, id: int, *, command):
    logs = client.get_channel(log_channel)
    role = discord.utils.get(ctx.guild.roles, id=admin_role)
    if role in ctx.author.roles:
        a = await server_valid(ctx, id)
        if a == "CError":
            await ctx.send(f"Unable to Connect to Crafty Controller")
            return
        if a == "Invalid":
            await ctx.send(f"The Server ID you provided was not Valid.")
            return
        msg = await ctx.send("Executing Command...")
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
                async with session.post(f"{URL}/api/v1/server/send_command?token={API_TOKEN}", params={'id': id}, json={'command': command}) as resp:
                    if resp.status == 200:
                        await msg.edit(content=f"Command has been executed to Server ID {str(id)}")
                        embed = discord.Embed(title="Crafty Command Execution", description=f"Command Issuer  - {ctx.message.author.mention} \n Server ID - {str(id)} \n Command - {command}")
                        await logs.send(embed=embed)
                    else:
                        await msg.edit(content=f"An error occured while sending the request to Crafty Controller")
        except Exception as e:
            await msg.edit(content=f"A unknown error has occurred. It has been logged to console")
            print(e)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def backup(ctx, id: int):
    role = discord.utils.get(ctx.guild.roles, id=admin_role)
    if role in ctx.author.roles:
        a = await server_valid(ctx, id)
        if a == "CError":
            await ctx.send(f"Unable to Connect to Crafty Controller")
            return
        if a == "Invalid":
            await ctx.send(f"The Server ID you provided was not Valid.")
            return
        logs = client.get_channel(log_channel)
        msg = await ctx.send("Executing Command...")
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
                async with session.post(f"{URL}/api/v1/server/force_backup?token={API_TOKEN}", params={'id': id}) as resp:
                    if resp.status == 200:
                        await msg.edit(content=f"Backup Command sent to backup Server ID {str(id)}")
                        embed = discord.Embed(title="Crafty Command Execution", description=f"Command Issuer  - {ctx.message.author.mention} \n Server ID - {str(id)} \n Action - Backup Server")
                        await logs.send(embed=embed)
                    else:
                        await msg.edit(content=f"An error occured while sending the request to Crafty Controller")
        except Exception as e:
            await msg.edit(content=f"A unknown error has occurred. It has been logged to console")
            print(e)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def start(ctx, id: int):
    role = discord.utils.get(ctx.guild.roles, id=admin_role)
    if role in ctx.author.roles:
        a = await server_valid(ctx, id)
        if a == "CError":
            await ctx.send(f"Unable to Connect to Crafty Controller")
            return
        if a == "Invalid":
            await ctx.send(f"The Server ID you provided was not Valid.")
            return
        logs = client.get_channel(log_channel)
        msg = await ctx.send("Executing Command...")
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
                async with session.post(f"{URL}/api/v1/server/start?token={API_TOKEN}", params={'id': id}) as resp:
                    if resp.status == 200:
                        await msg.edit(content=f"Start Command sent to Server ID {str(id)}")
                        embed = discord.Embed(title="Crafty Command Execution", description=f"Command Issuer  - {ctx.message.author.mention} \n Server ID - {str(id)} \n Action - Start")
                        await logs.send(embed=embed)
                    else:
                        await msg.edit(content=f"An error occured while sending the request to Crafty Controller")
        except Exception as e:
            await msg.edit(content=f"A unknown error has occurred. It has been logged to console")
            print(e)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def stop(ctx, id: int):
    role = discord.utils.get(ctx.guild.roles, id=admin_role)
    if role in ctx.author.roles:
        a = await server_valid(ctx, id)
        if a == "CError":
            await ctx.send(f"Unable to Connect to Crafty Controller")
            return
        if a == "Invalid":
            await ctx.send(f"The Server ID you provided was not Valid.")
            return
        logs = client.get_channel(log_channel)
        msg = await ctx.send("Executing Command...")
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
                async with session.post(f"{URL}/api/v1/server/stop?token={API_TOKEN}", params={'id': id}) as resp:
                    if resp.status == 200:
                        await msg.edit(content=f"Stop Command sent to Server ID {str(id)}")
                        embed = discord.Embed(title="Crafty Command Execution", description=f"Command Issuer  - {ctx.message.author.mention} \n Server ID - {str(id)} \n Action - Stop")
                        await logs.send(embed=embed)
                    else:
                        await msg.edit(content=f"An error occured while sending the request to Crafty Controller")
        except Exception as e:
            await msg.edit(content=f"A unknown error has occurred. It has been logged to console")
            print(e)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def restart(ctx, id: int):
    role = discord.utils.get(ctx.guild.roles, id=admin_role)
    if role in ctx.author.roles:
        a = await server_valid(ctx, id)
        if a == "CError":
            await ctx.send(f"Unable to Connect to Crafty Controller")
            return
        if a == "Invalid":
            await ctx.send(f"The Server ID you provided was not Valid.")
            return
        logs = client.get_channel(log_channel)
        msg = await ctx.send("Executing Command...")
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
                async with session.post(f"{URL}/api/v1/server/restart?token={API_TOKEN}", params={'id': id}) as resp:
                    if resp.status == 200:
                        await msg.edit(content=f"Restart Command sent to Server ID {str(id)}")
                        embed = discord.Embed(title="Crafty Command Execution", description=f"Command Issuer  - {ctx.message.author.mention} \n Server ID - {str(id)} \n Action - Restart")
                        await logs.send(embed=embed)
                    else:
                        await msg.edit(content=f"An error occured while sending the request to Crafty Controller")
        except Exception as e:
            await msg.edit(content=f"A unknown error has occurred. It has been logged to console")
            print(e)
    else:
        await ctx.channel.send("You do not have permission to run this command.")

@client.command()
async def ping(ctx):
    before = time.monotonic()
    before_ws = int(round(client.latency * 1000, 1))
    message = await ctx.send("🏓 Pong")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

@client.command()
async def help(ctx):
    desc = f"""{prefix}serverinfo - Shows information about the Servers \n {prefix}hostinfo - Shows information about the Host \n {prefix}ping - Shows Bot Latency \n {prefix}start serverid - Starts a Server \n {prefix}stop serverid - Stops a Server \n {prefix}backup serverid - Starts a Backup for a server \n {prefix}send serverid command - Sends a command to a server"""
    embed = discord.Embed(title="Crafty Help Commands", description=desc)
    await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
            async with session.get(f'{URL}/api/v1/server_stats?token={API_TOKEN}') as resp:
                data = await resp.json()
    except aiohttp.ClientConnectorError:
        await ctx.send("Unable to connect to Crafty Controller")
        return
    embed = discord.Embed(title="Server Info")
    for i in data["data"]:
        if i["server_start_time"] == "Not Started":
            status = "Offline"
        else:
            status = "Online"
        data = f"""Status - {status} \n CPU Usage - {i["cpu_usage"]} \n Memory Usage - {i["memory_usage"]} \n Players - {i["online_players"]} / {i["max_players"]}"""
        embed.add_field(name=f"Server {i['id']} - {i['name']}", value=data)
    await ctx.send(embed=embed)

@client.command()
async def hostinfo(ctx):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_check)) as session:
            async with session.get(f'{URL}/api/v1/host_stats?token={API_TOKEN}') as resp:
                data = await resp.json()
    except aiohttp.ClientConnectorError:
        await ctx.send("Unable to connect to Crafty Controller")
        return
    desc = f"""CPU Load - {data["data"]["cpu_usage"]} \n Memory Usage - {data["data"]["mem_usage"]} / {data["data"]["mem_total"]} \n Disk Usage - {data["data"]["disk_usage"]} / {data["data"]["disk_total"]}"""
    embed = discord.Embed(title="Host Info", description=desc)
    await ctx.send(embed=embed)




@client.event
async def on_command_error(ctx, error):
    await ctx.send("An Error occurred while executing your Command. The error has been logged into console")
    print(error)


client.run(BOT_TOKEN)
