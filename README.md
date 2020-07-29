# crafty-discord-bot
A discord bot using the crafty-client API to control Crafty Controller

# need-help
Need any help? If so, contact CatsAreDaBest#3054 on Discord

# requirements
discord.py installed

Discord Bot Token

Discord Role

Discord Channel

Crafty Controller API Token

Knowledge in Python

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
Sends the Command to the server with the supplied ID and Command

<img width="318" alt="send" src="https://user-images.githubusercontent.com/60989180/88817929-79e3e480-d201-11ea-9e89-4b91870fa728.png">

# installation
Firstly Supply the URL to the Crafty Controller Server

Then Supply the Crafty Controller API Token

Then Supply the Discord Bot Token

Supply the Discord Channel [ID FORM] for the bot to execute its start command

Then supply a Discord Role [NAME] which the bot will consider allowed to run admin commands

# MUTIPLE SERVERS
Go to Line 239 and add your first server. Use this as a example [ONLY IF YOU ARE USING MUTIPLE SERVERS]

        serverid1info = re.findall(r'serverid: 1(.*?)serverid: 2',str(datavaluesassembled)) # this says to find text between server id 1 and 2
        serverid1assembled = ''.join(map(str, serverid1info)) 

        datasurvival = re.findall(r'Survival(.*?)},',str(data)) # this is to find the status of the server named "Survival Server"
        survivalstripped = [w.translate(datastrip) for w in datasurvival]
        survivalassembled = " ".join(survivalstripped)

        SURVCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid1assembled)) # this is to find the data of the CPU Usage for ID 1
        SURVCPUASSEMBLED = ''.join(map(str, SURVCPU))
        SURVMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid1assembled)) # this is to find the data of the Memory Usage for ID 1
        SURVMEMASSEMBLED = ''.join(map(str, SURVMEM))
        SURVPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid1assembled)) # this is to find the data of how many Players are on the server for ID 1
        SURVPLAYERSASSEMBLED = ''.join(map(str, SURVPLAYERS))

        if srvrunning in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Online CPU Usage:" + SURVCPUASSEMBLED +"% Memory:" + SURVMEMASSEMBLED + " Players Online:" + SURVPLAYERSASSEMBLED, inline=False)
        if srvstopped in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Stopped", inline=False)
        if srvcrashed in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Crashed", inline=False
            
This Line is for your last Server
                                                            WHERE IT SAYS serverid: 2, you will need to change it to the first word of your last server name
                                                            
        serverid1info = re.findall(r'serverid: 1(.*?)serverid: 2',str(datavaluesassembled)) # this says to find text between server id 1 and 2
        serverid1assembled = ''.join(map(str, serverid1info)) 

        datasurvival = re.findall(r'Survival(.*?)},',str(data)) # this is to find the status of the server named "Survival Server"
        survivalstripped = [w.translate(datastrip) for w in datasurvival]
        survivalassembled = " ".join(survivalstripped)

        SURVCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid1assembled)) # this is to find the data of the CPU Usage for ID 1
        SURVCPUASSEMBLED = ''.join(map(str, SURVCPU))
        SURVMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid1assembled)) # this is to find the data of the Memory Usage for ID 1
        SURVMEMASSEMBLED = ''.join(map(str, SURVMEM))
        SURVPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid1assembled)) # this is to find the data of how many Players are on the server for ID 1
        SURVPLAYERSASSEMBLED = ''.join(map(str, SURVPLAYERS))

        if srvrunning in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Online CPU Usage:" + SURVCPUASSEMBLED +"% Memory:" + SURVMEMASSEMBLED + " Players Online:" + SURVPLAYERSASSEMBLED, inline=False)
        if srvstopped in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Stopped", inline=False)
        if srvcrashed in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Crashed", inline=False
            
If you require or would like to look at a further example. Look at furtherexample.py
            
# SINGLE SERVER
Go to Line 239 and add your first server. Use this as a example
Use this code if you are only hosting a single server on the crafty panel
                                                            WHERE IT SAYS serverid: 2, you will need to change it to the first word of your last server name
                                                            
        serverid1info = re.findall(r'serverid: 1(.*?)serverid: 2',str(datavaluesassembled)) # this says to find text between server id 1 and 2
        serverid1assembled = ''.join(map(str, serverid1info)) 

        datasurvival = re.findall(r'Survival(.*?)},',str(data)) # this is to find the status of the server named "Survival Server"
        survivalstripped = [w.translate(datastrip) for w in datasurvival]
        survivalassembled = " ".join(survivalstripped)

        SURVCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid1assembled)) # this is to find the data of the CPU Usage for ID 1
        SURVCPUASSEMBLED = ''.join(map(str, SURVCPU))
        SURVMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid1assembled)) # this is to find the data of the Memory Usage for ID 1
        SURVMEMASSEMBLED = ''.join(map(str, SURVMEM))
        SURVPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid1assembled)) # this is to find the data of how many Players are on the server for ID 1
        SURVPLAYERSASSEMBLED = ''.join(map(str, SURVPLAYERS))

        if srvrunning in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Online CPU Usage:" + SURVCPUASSEMBLED +"% Memory:" + SURVMEMASSEMBLED + " Players Online:" + SURVPLAYERSASSEMBLED, inline=False)
        if srvstopped in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Stopped", inline=False)
        if srvcrashed in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Crashed", inline=False
            
# starting bot
To start the bot up, open a cmd window in its directory and type
        python discordconnect.py
Once it starts check the channel you provided for the start message and see if this has popped up
<img width="540" alt="start messagee" src="https://user-images.githubusercontent.com/60989180/88817934-7b151180-d201-11ea-83d9-ecfa8966b7f4.png">
