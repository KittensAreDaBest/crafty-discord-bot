    # -------------------------------------------------------------------------

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

    # -------------------------------------------------------------------------

    # name of server id 2
    serverid2name = "Bedwars"

    # this is attempt of cleaning the code up by making it smaller, this finds the online status of the server
    serverid2 = " ".join([w.translate(datastrip) for w in re.findall(r'Bedwars(.*?)},', str(data))])

    # this for grabbing server stats
    serverid2info = re.findall(r'serverid: 2(.*?)serverid: 3', str(datavaluesassembled))
    serverid2assembled = ''.join(map(str, serverid2info))

    # find cpu from cweb.get_host_stats_server
    serverid2cpudata = re.findall(r'cpuusage:(.*?)memoryusage', str(serverid2assembled))
    serverid2cpu = ''.join(map(str, serverid2cpudata))

    # find mem from cweb.get_host_stats_server
    serverid2memdata = re.findall(r'memoryusage:(.*?)maxplayers', str(serverid2assembled))
    serverid2mem = ''.join(map(str, serverid2memdata))

    # find players from cweb.get_host_stats_server
    serverid2playerdata = re.findall(r'onlineplayers:(.*?)players', str(serverid2assembled))
    serverid2player = ''.join(map(str, serverid2playerdata))

    # checks what status it is and then selects the right status
    if srvrunning in serverid2:
        embedstatus.add_field(name=serverid2name,
                              value="ID 2 " + serverid2name + " Server Status: Online CPU Usage:" + serverid2cpu + "% Memory:" + serverid2mem + " Players Online:" + serverid2player,
                              inline=False)
    if srvstopped in serverid2:
        embedstatus.add_field(name=serverid2name, value="ID 2 " + serverid2name + " Server Status: Stopped",
                              inline=False)
    if srvcrashed in serverid2:
        embedstatus.add_field(name=serverid2name, value="ID 2 " + serverid2name + " Server Status: Crashed",
                              inline=False)

    # -------------------------------------------------------------------------

    # name of server id 3
    serverid3name = "Lobby"

    # this is attempt of cleaning the code up by making it smaller, this finds the online status of the server
    serverid3 = " ".join([w.translate(datastrip) for w in re.findall(r'Lobby(.*?)},', str(data))])

    # this for grabbing server stats
    serverid3info = re.findall(r'serverid: 3(.*?)serverid: 4', str(datavaluesassembled))
    serverid3assembled = ''.join(map(str, serverid3info))

    # find cpu from cweb.get_host_stats_server
    serverid3cpudata = re.findall(r'cpuusage:(.*?)memoryusage', str(serverid3assembled))
    serverid3cpu = ''.join(map(str, serverid3cpudata))

    # find mem from cweb.get_host_stats_server
    serverid3memdata = re.findall(r'memoryusage:(.*?)maxplayers', str(serverid3assembled))
    serverid3mem = ''.join(map(str, serverid3memdata))

    # find players from cweb.get_host_stats_server
    serverid3playerdata = re.findall(r'onlineplayers:(.*?)players', str(serverid3assembled))
    serverid3player = ''.join(map(str, serverid3playerdata))

    # checks what status it is and then selects the right status
    if srvrunning in serverid3:
        embedstatus.add_field(name=serverid3name,
                              value="ID 3 " + serverid3name + " Server Status: Online CPU Usage:" + serverid3cpu + "% Memory:" + serverid3mem + " Players Online:" + serverid3player,
                              inline=False)
    if srvstopped in serverid3:
        embedstatus.add_field(name=serverid3name, value="ID 3 " + serverid3name + " Server Status: Stopped",
                              inline=False)
    if srvcrashed in serverid3:
        embedstatus.add_field(name=serverid3name, value="ID 3 " + serverid3name + " Server Status: Crashed",
                              inline=False)

    # -------------------------------------------------------------------------

    # name of server id 4
    serverid4name = "Skyblock"

    # this is attempt of cleaning the code up by making it smaller, this finds the online status of the server
    serverid4 = " ".join([w.translate(datastrip) for w in re.findall(r'Skyblock(.*?)},', str(data))])

    # this for grabbing server stats
    serverid4info = re.findall(r'serverid: 4(.*?)serverid: 5', str(datavaluesassembled))
    serverid4assembled = ''.join(map(str, serverid4info))

    # find cpu from cweb.get_host_stats_server
    serverid4cpudata = re.findall(r'cpuusage:(.*?)memoryusage', str(serverid4assembled))
    serverid4cpu = ''.join(map(str, serverid4cpudata))

    # find mem from cweb.get_host_stats_server
    serverid4memdata = re.findall(r'memoryusage:(.*?)maxplayers', str(serverid4assembled))
    serverid4mem = ''.join(map(str, serverid4memdata))

    # find players from cweb.get_host_stats_server
    serverid4playerdata = re.findall(r'onlineplayers:(.*?)players', str(serverid4assembled))
    serverid4player = ''.join(map(str, serverid4playerdata))

    # checks what status it is and then selects the right status
    if srvrunning in serverid4:
        embedstatus.add_field(name=serverid4name,
                              value="ID 4 " + serverid4name + " Server Status: Online CPU Usage:" + serverid4cpu + "% Memory:" + serverid4mem + " Players Online:" + serverid4player,
                              inline=False)
    if srvstopped in serverid4:
        embedstatus.add_field(name=serverid4name, value="ID 4 " + serverid4name + " Server Status: Stopped",
                              inline=False)
    if srvcrashed in serverid4:
        embedstatus.add_field(name=serverid4name, value="ID 4 " + serverid4name + " Server Status: Crashed",
                              inline=False)

    # -------------------------------------------------------------------------

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

    # -------------------------------------------------------------------------
