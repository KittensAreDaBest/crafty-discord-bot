        serverid1info = re.findall(r'serverid: 1(.*?)serverid: 2',str(datavaluesassembled))
        serverid1assembled = ''.join(map(str, serverid1info))

        datasurvival = re.findall(r'Survival(.*?)},',str(data))
        survivalstripped = [w.translate(datastrip) for w in datasurvival]
        survivalassembled = " ".join(survivalstripped)

        SURVCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid1assembled))
        SURVCPUASSEMBLED = ''.join(map(str, SURVCPU))
        SURVMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid1assembled))
        SURVMEMASSEMBLED = ''.join(map(str, SURVMEM))
        SURVPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid1assembled))
        SURVPLAYERSASSEMBLED = ''.join(map(str, SURVPLAYERS))

        if srvrunning in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Online CPU Usage:" + SURVCPUASSEMBLED +"% Memory:" + SURVMEMASSEMBLED + " Players Online:" + SURVPLAYERSASSEMBLED, inline=False)
        if srvstopped in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Stopped", inline=False)
        if srvcrashed in survivalassembled:
            embedstatus.add_field(name="Survival", value="ID 1 Survival Server Status: Crashed", inline=False)

        databedwars = re.findall(r'Bedwars(.*?)},', str(data))
        bedwarsstripped = [w.translate(datastrip) for w in databedwars]
        bedwarsassembled = " ".join(bedwarsstripped)

        serverid2info = re.findall(r'serverid: 2(.*?)serverid: 3',str(datavaluesassembled))
        serverid2assembled = ''.join(map(str, serverid2info))

        BDWARSCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid2assembled))
        BDWARSCPUASSEMBLED = ''.join(map(str, BDWARSCPU))
        BDWARSVMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid2assembled))
        BDWARSMEMASSEMBLED = ''.join(map(str, BDWARSVMEM))
        BDWARSPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid2assembled))
        BDWARSPLAYERSASSEMBLED = ''.join(map(str, BDWARSPLAYERS))

        if srvrunning in bedwarsassembled:
            embedstatus.add_field(name="Bedwars", value="ID 2 Bedwars Server Status: Online CPU Usage:" + BDWARSCPUASSEMBLED +"% Memory:" + BDWARSMEMASSEMBLED + " Players Online:" + BDWARSPLAYERSASSEMBLED, inline=False)
        if srvstopped in bedwarsassembled:
            embedstatus.add_field(name="Bedwars", value="ID 2 Bedwars Server Status: Stopped", inline=False)
        if srvcrashed in bedwarsassembled:
            embedstatus.add_field(name="Bedwars", value="ID 2 Bedwars Server Status: Crashed", inline=False)

        serverid3info = re.findall(r'serverid: 3(.*?)serverid: 4',str(datavaluesassembled))
        serverid3assembled = ''.join(map(str, serverid3info))

        LOBBYCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid3assembled))
        LOBBYCPUASSEMBLED = ''.join(map(str, LOBBYCPU))
        LOBBYMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid3assembled))
        LOBBYMEMASSEMBLED = ''.join(map(str, LOBBYMEM))
        LOBBYPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid3assembled))
        LOBBYPLAYERSASSEMBLED = ''.join(map(str, LOBBYPLAYERS))

        datalobby = re.findall(r'Lobby(.*?)},', str(data))
        lobbystripped = [w.translate(datastrip) for w in datalobby]
        lobbyassembled = " ".join(lobbystripped)

        if srvrunning in lobbyassembled:
            embedstatus.add_field(name="Lobby", value="ID 3 Lobby Server Status: Online CPU Usage:" + LOBBYCPUASSEMBLED +"% Memory:" + LOBBYMEMASSEMBLED + " Players Online:" + LOBBYPLAYERSASSEMBLED, inline=False)
        if srvstopped in lobbyassembled:
            embedstatus.add_field(name="Lobby", value="ID 3 Lobby Server Status: Stopped", inline=False)
        if srvcrashed in lobbyassembled:
            embedstatus.add_field(name="Lobby", value="ID 3 Lobby Server Status: Crashed", inline=False)

        serverid4info = re.findall(r'serverid: 4(.*?)serverid: 5',str(datavaluesassembled))
        serverid4assembled = ''.join(map(str, serverid4info))

        SKYBLOCKCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid4assembled))
        SKYBLOCKCPUASSEMBLED = ''.join(map(str, SKYBLOCKCPU))
        SKYBLOCKMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid4assembled))
        SKYBLOCKMEMASSEMBLED = ''.join(map(str, SKYBLOCKMEM))
        SKYBLOCKPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid4assembled))
        SKYBLOCKPLAYERSASSEMBLED = ''.join(map(str, SKYBLOCKPLAYERS))

        dataskyblock = re.findall(r'Skyblock(.*?)},', str(data))
        skyblockstripped = [w.translate(datastrip) for w in dataskyblock]
        skyblockassembled = " ".join(skyblockstripped)

        if srvrunning in skyblockassembled:
            embedstatus.add_field(name="Skyblock", value="ID 4 Skyblock Server Status: Online CPU Usage:" + SKYBLOCKCPUASSEMBLED +"% Memory:" + SKYBLOCKMEMASSEMBLED + " Players Online:" + SKYBLOCKPLAYERSASSEMBLED , inline=False)
        if srvstopped in skyblockassembled:
            embedstatus.add_field(name="Skyblock", value="ID 4 Skyblock Server Status: Stopped", inline=False)
        if srvcrashed in skyblockassembled:
            embedstatus.add_field(name="Skyblock", value="ID 4 Skyblock Server Status: Crashed", inline=False)

        serverid5info = re.findall(r'serverid: 5(.*?)Proxy',str(datavaluesassembled))
        serverid5assembled = ''.join(map(str, serverid5info))
        print("datavaluesassembled")
        print(datavaluesassembled)
        print("ID5")
        print(serverid5assembled)
        PROXYCPU = re.findall(r'cpuusage:(.*?)memoryusage',str(serverid5assembled))
        PROXYCPUASSEMBLED = ''.join(map(str, PROXYCPU))
        PROXYMEM = re.findall(r'memoryusage:(.*?)maxplayers',str(serverid5assembled))
        PROXYMEMASSEMBLED = ''.join(map(str, PROXYMEM))
        PROXYPLAYERS = re.findall(r'onlineplayers:(.*?)players',str(serverid5assembled))
        PROXYPLAYERSASSEMBLED = ''.join(map(str, PROXYPLAYERS))

        dataproxy = re.findall(r'Proxy(.*?)]', str(data))
        proxystripped = [w.translate(datastrip) for w in dataproxy]
        proxyassembled = " ".join(proxystripped)

        if srvrunning in proxyassembled:
            embedstatus.add_field(name="Proxy", value="ID 5 Proxy Server Status: Online CPU Usage:" + PROXYCPUASSEMBLED +"% Memory:" + PROXYMEMASSEMBLED + " Players Online:" + PROXYPLAYERSASSEMBLED, inline=False)
        if srvstopped in proxyassembled:
            embedstatus.add_field(name="Proxy", value="ID 5 Proxy Server Status: Stopped", inline=False)
        if srvcrashed in proxyassembled:
            embedstatus.add_field(name="Proxy", value="ID 5 Proxy Server Status: Crashed", inline=False)
