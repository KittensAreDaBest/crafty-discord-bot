# crafty-discord-bot
A discord bot using the crafty-client API to control Crafty Controller

# need-help
Need any help? If so, contact CatsAreDaBest#3054 on Discord

# pleasenote
This bot uses a custom version of the crafty-client api which is provided. what it changes is that in craftyweb.py it seperates the stats from get_host_status to get_host_stats_pc [grabs pc stats] and get_host_status_server [grabs server stats]. I plan on soon making it work without modification

# requirements
discord.py installed

Discord Bot Token

Discord Role

Discord Channel

Crafty Controller API Token

Knowledge in Python and how to change variables in Python

# what can it do?
This bot can do many commands

!serverinfo
Lists all of the Servers and their CPU Usage, Memory Usage and Player Count.

<img width="556" alt="serverinfo" src="https://user-images.githubusercontent.com/60989180/88817930-7a7c7b00-d201-11ea-9a71-39e69681cd93.png">

!hostinfo
Lists the total CPU Usage, Memory Usage and Disk Usage of the Host.

<img width="346" alt="hostinfo" src="https://user-images.githubusercontent.com/60989180/88817951-7f412f00-d201-11ea-89d6-53f999b8452a.png">

!help
Shows commands

<img width="218" alt="help" src="https://user-images.githubusercontent.com/60989180/88817948-7ea89880-d201-11ea-9bf1-d7fcca151f32.png">

!start [ID]
Starts the server with the supplied ID

<img width="340" alt="start" src="https://user-images.githubusercontent.com/60989180/88817939-7bada800-d201-11ea-9c75-18de65ebb8b7.png">

!stop [ID]
Stops the server with the supplied ID

<img width="336" alt="stop" src="https://user-images.githubusercontent.com/60989180/88817941-7bada800-d201-11ea-9987-287da967d83e.png">

!restart [ID]
Restarts the server with the supplied ID

<img width="356" alt="restart" src="https://user-images.githubusercontent.com/60989180/88817927-76e8f400-d201-11ea-83f2-fb4d4fc22ebe.png">

!backup [ID]
Backups the server with the supplied ID

<img width="413" alt="backup" src="https://user-images.githubusercontent.com/60989180/88817947-7e100200-d201-11ea-9a03-78b73afb5071.png">

!send [ID] [Command]
Sends the Command to the server with the supplied ID and Command [I plan on fixing the run: true and making it just say true in a future release]

<img width="318" alt="send" src="https://user-images.githubusercontent.com/60989180/88817929-79e3e480-d201-11ea-9e89-4b91870fa728.png">

# installation
1.Supply the URL to the Crafty Controller Server

2.Supply the Crafty Controller API Token

3.Supply the Discord Bot Token

4.the Discord Channel [ID FORM] for the bot to execute its start command

5.supply a Discord Role [NAME] which the bot will consider allowed to run admin commands

6.Supply servers [Example and instructions can be found below]

# MUTIPLE SERVERS
Go to Line 274 and add your first server. Use this as a examplem Also make sure to adjust variables as needed. [ONLY IF YOU ARE USING MUTIPLE SERVERS, SINGLE SERVER CODE BELOW]. 

    # name of server id 1
    serverid1name = "Survival"

    # this is attempt of cleaning the code up by making it smaller, this finds the online status of the server
    serverid1 = " ".join([w.translate(datastrip) for w in re.findall(r'Survival(.*?)},', str(data))])

    # this for grabbing server stats
    serverid1info = re.findall(r'serverid: 1(.*?)serverid: 2', str(datavaluesassembled))
    serverid1assembled = ''.join(map(str, serverid1info))

    # find cpu from cweb.get_host_stats_server
    serverid1cpudata = re.findall(r'cpuusage:(.*?)memoryusage', str(serverid1assembled))
    serverid1cpu = ''.join(map(str, serverid1cpudata))

    # find mem from cweb.get_host_stats_server
    serverid1memdata = re.findall(r'memoryusage:(.*?)maxplayers', str(serverid1assembled))
    serverid1mem = ''.join(map(str, serverid1memdata))

    # find players from cweb.get_host_stats_server
    serverid1playerdata = re.findall(r'onlineplayers:(.*?)players', str(serverid1assembled))
    serverid1player = ''.join(map(str, serverid1playerdata))

    # checks what status it is and then selects the right status
    if srvrunning in serverid1:
        embedstatus.add_field(name=serverid1name,
                              value="ID 1 " + serverid1name + " Server Status: Online CPU Usage:" + serverid1cpu + "% Memory:" + serverid1mem + " Players Online:" + serverid1player,
                              inline=False)
    if srvstopped in serverid1:
        embedstatus.add_field(name=serverid1name, value="ID 1 " + serverid1name + " Server Status: Stopped",
                              inline=False)
    if srvcrashed in serverid1:
        embedstatus.add_field(name=serverid1name, value="ID 1 " + serverid1name + " Server Status: Crashed",
                              inline=False)
            
This Line is for your last Server
WHERE IT SAYS Proxy, you will need to change it to the first word of your last server name, also make sure to adjust the varibles as needed
                                                            
    # name of server id 5
    serverid5name = "Proxy"

    # this is attempt of cleaning the code up by making it smaller, this finds the online status of the server
    serverid5 = " ".join([w.translate(datastrip) for w in re.findall(r'Proxy(.*?)]', str(data))])

    # this for grabbing server stats
    serverid5info = re.findall(r'serverid: 5(.*?)Proxy', str(datavaluesassembled))
    serverid5assembled = ''.join(map(str, serverid5info))

    # find cpu from cweb.get_host_stats_server
    serverid5cpudata = re.findall(r'cpuusage:(.*?)memoryusage', str(serverid5assembled))
    serverid5cpu = ''.join(map(str, serverid5cpudata))

    # find mem from cweb.get_host_stats_server
    serverid5memdata = re.findall(r'memoryusage:(.*?)maxplayers', str(serverid5assembled))
    serverid5mem = ''.join(map(str, serverid5memdata))

    # find players from cweb.get_host_stats_server
    serverid5playerdata = re.findall(r'onlineplayers:(.*?)players', str(serverid5assembled))
    serverid5player = ''.join(map(str, serverid5playerdata))

    # checks what status it is and then selects the right status
    if srvrunning in serverid5:
        embedstatus.add_field(name=serverid5name,
                              value="ID 5 " + serverid5name + " Server Status: Online CPU Usage:" + serverid5cpu + "% Memory:" + serverid5mem + " Players Online:" + serverid5player,
                              inline=False)
    if srvstopped in serverid5:
        embedstatus.add_field(name=serverid5name, value="ID 5 " + serverid5name + " Server Status: Stopped",
                              inline=False)
    if srvcrashed in serverid5:
        embedstatus.add_field(name=serverid5name, value="ID 5 " + serverid5name + " Server Status: Crashed",
                              inline=False)
            
If you require or would like to look at a further example. Look at furtherexample.py
            
# SINGLE SERVER
Go to Line 274 and add your first server. Use this as a example
Use this code if you are only hosting a single server on the crafty panel
WHERE IT SAYS serverid: 2, you will need to change it to the first word of your server name and chane serverid1name to your server
                                                            
    # name of server id 1
    serverid1name = "Survival"

    # this is attempt of cleaning the code up by making it smaller, this finds the online status of the server
    serverid1 = " ".join([w.translate(datastrip) for w in re.findall(r'Survival(.*?)},', str(data))])

    # this for grabbing server stats
    serverid1info = re.findall(r'serverid: 1(.*?)serverid: 2', str(datavaluesassembled))
    serverid1assembled = ''.join(map(str, serverid1info))

    # find cpu from cweb.get_host_stats_server
    serverid1cpudata = re.findall(r'cpuusage:(.*?)memoryusage', str(serverid1assembled))
    serverid1cpu = ''.join(map(str, serverid1cpudata))

    # find mem from cweb.get_host_stats_server
    serverid1memdata = re.findall(r'memoryusage:(.*?)maxplayers', str(serverid1assembled))
    serverid1mem = ''.join(map(str, serverid1memdata))

    # find players from cweb.get_host_stats_server
    serverid1playerdata = re.findall(r'onlineplayers:(.*?)players', str(serverid1assembled))
    serverid1player = ''.join(map(str, serverid1playerdata))

    # checks what status it is and then selects the right status
    if srvrunning in serverid1:
        embedstatus.add_field(name=serverid1name,
                              value="ID 1 " + serverid1name + " Server Status: Online CPU Usage:" + serverid1cpu + "% Memory:" + serverid1mem + " Players Online:" + serverid1player,
                              inline=False)
    if srvstopped in serverid1:
        embedstatus.add_field(name=serverid1name, value="ID 1 " + serverid1name + " Server Status: Stopped",
                              inline=False)
    if srvcrashed in serverid1:
        embedstatus.add_field(name=serverid1name, value="ID 1 " + serverid1name + " Server Status: Crashed",
                              inline=False)
            
# starting bot
To start the bot up, open a cmd window in its directory and type
        python discordconnect.py
Once it starts check the channel you provided for the start message and see if this has popped up

<img width="540" alt="start messagee" src="https://user-images.githubusercontent.com/60989180/88817934-7b151180-d201-11ea-83d9-ecfa8966b7f4.png">
