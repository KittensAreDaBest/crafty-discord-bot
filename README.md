# crafty-discord-bot
A discord bot to control Crafty Controller

# need-help
Need any help? If so, contact Kittens#3054 on the Crafty Controller Discord https://discord.gg/9VJPhCE

# command
    !help - Help Command
    !serverinfo - Info about the servers in Crafty Controller
    !hostinfo - Info about the Host
    !ping - Latency between Discord and the Bot
    !start serverid - Start a Server
    !stop serverid - Stop a Server
    !restart serverid - Restart a Server
    !backup serverid - Backup a Server
    !send serverid command - Send a Command to a server

# installation
Make sure you have Python Installed First

Firstly Configure the Config.json

    {"bot_token": "discordbottoken", # replace "discordbottoken" with bot token
    "api_token": "apitoken", # replace apitoken with the crafty controller api token
    "crafty_url": "https://localhost:8000", # replace with server url. keep the https:// in there.
    "log_channel": 0, # replace with log channel id
    "admin_role": 0, # replace with admin role id
    "prefix": "!", # replace if wanted. Discord Bot Prefix
    "ssl_check": "False"} # if your crafty controller has a valid ssl certificate. Replace with True
    
Secoundly install the requirements with
    
    Windows - pip install -r requirements.txt
    
    Linnx / Macos - pip3 install -r requirements.txt
    
Lastly run the bot 
    
    Windows - python index.py
    
    Linux / Macos - python3 index.py
   
    
