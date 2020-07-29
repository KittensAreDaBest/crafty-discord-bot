# crafty-discord-bot
A discord bot using the crafty-client API to control Crafty Controlleer

# requirements
discord.py installed
Discord Bot Token
Discord Role
Discord Channel
Crafty Controller API Token
Knowledge

# what can it do?
This bot can do many commands
!serverinfo
Lists all of the Servers and their CPU Usage, Memory Usage and Player Count.
!hoststat
Lists the total CPU Usage, Memory Usage and Disk Usage of the Host.
!help
Shows commands
!start [ID]
Starts the server with the supplied ID
!stop [ID]
Stops the server with the supplied ID
!restart [ID]
Restarts the server with the supplied ID
!backup [ID]
Backups the server with the supplied ID
!send [ID] [Command]
Sends the Command to the server with the supplied ID and Command

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
