import pywinauto as pwa
import pygetwindow as pgw
import pyautogui as pag
from datetime import datetime, timedelta
import time
import requests
import random


level_images = {
    1: "https://i.imgur.com/9eo56BR.png",
    2: "https://i.imgur.com/106N9Yf.png",
    3: "https://i.imgur.com/u9KhBcG.png",
    4: "https://i.imgur.com/YxcmDxy.png",
    5: "https://i.imgur.com/MTiwRK3.png",
    6: "https://i.imgur.com/k8APHiv.png",
    7: "https://i.imgur.com/bE5gKaT.png",
    8: "https://i.imgur.com/ENjlUpK.png",
    9: "https://i.imgur.com/K3hwAZs.png",
    10: "https://i.imgur.com/Y1sVIbk.png",
    11: "https://i.imgur.com/Wsx2NGq.png",
    12: "https://i.imgur.com/mOxPfl2.png",
    13: "https://i.imgur.com/VoYiQCD.png",
    14: "https://i.imgur.com/e491BJT.png",
    15: "https://i.imgur.com/muGvca5.png",
    16: "https://i.imgur.com/Vm2WAw7.png",
    17: "https://i.imgur.com/HQsTXrx.png",
    18: "https://i.imgur.com/mx45X4N.png",
    19: "https://i.imgur.com/enBms4J.png",
    20: "https://i.imgur.com/BxL3mXo.png",
    21: "https://i.imgur.com/lOmwNZG.png",
    22: "https://i.imgur.com/AQZJJa7.png",
    23: "https://i.imgur.com/QBXe6Vc.png",
    24: "https://i.imgur.com/y0cKj7V.png",
    25: "https://i.imgur.com/zeTxGvX.png",
    26: "https://i.imgur.com/Iot76Gw.png",
    27: "https://i.imgur.com/K6Oc6Py.png",
    28: "https://i.imgur.com/wpY0RPR.png",
    29: "https://i.imgur.com/QLtmra1.png",
    30: "https://i.imgur.com/xb8wQVg.png",
    31: "https://i.imgur.com/VEULovI.png",
    32: "https://i.imgur.com/c4YjUiF.png",
    33: "https://i.imgur.com/JKk7kPU.png",
    34: "https://i.imgur.com/swH0U2t.png",
    35: "https://i.imgur.com/qSvKWa0.png",
    36: "https://i.imgur.com/xgH6sOr.png",
    37: "https://i.imgur.com/VyO0UVf.png", 
    38: "https://i.imgur.com/CPSe9YL.png",
    39: "https://i.imgur.com/eUW0tc7.png",
    40: "https://i.imgur.com/NLfgDXY.png",
 
    # Add more levels and corresponding image URLs as needed
}
ErrorsCount = 1
found_kill = False
matches_found = 0
start_time = datetime.now()

# Query user for initial level and xp values
print("""  /_/l""")
time.sleep(0.01)
print(""" : : :""")
time.sleep(0.01)
print("""  ; ; ;""")
time.sleep(0.01)
print("""  : : :""")
time.sleep(0.01)
print("""   L ; ;  __.-._.-+. """)
time.sleep(0.01)
print("""  /.'^.:.L.' .^-.  \`.""")
time.sleep(0.01)
print(""" :`.`. \"/\ /.-. `. \ \ """)
time.sleep(0.01)
print(""" ;\ \ ` ;-.y(_.-\  \ `.`.""")
time.sleep(0.01)
print(""" :   _. ;;  `    \  \. `-n""")
time.sleep(0.01)
print(""" \ T :: :=,   ,=^\  \"-._;          __..------.._ """)
time.sleep(0.01)
print(""" /;:-'; ; `._L.--^.     .-""-.`.   \     ""--..   """)
time.sleep(0.01)
print(""": :_.': :           ;/     \   /      \ \   ;          ""--._ """)
time.sleep(0.01)
print(""" ;  T   \ \  s      /:.---.  ;_/    `-._; ;  :     ______    \"-.""")
time.sleep(0.01)
print(""":   :\   \ `.-=^" .:-"    _\   \_.      : :  _:.--".-"  .T"---:-.'"--'"\  ""-. """)
time.sleep(0.01)
print(""";    \\   "-.\__.:'      /-'. ; ;    _. ; ;  /   -'    '    .- \        ;     "-._.-""'"-,""")
time.sleep(0.01)
print(""":     ;\     `..'      .'    \: ;      / / .'               )   ;  __  /         T        :""")
time.sleep(0.01)
print(""" ;      `,     \    .-"       ;/"---" /.' /                 `- /"'"  ""- -"''"----..___..-'""")
time.sleep(0.01)
print(""" :    .-" `.      .'.-\      / ""----"''"^-.._              .-"  Made by @hineshvh#2825""")
time.sleep(0.01)
print("""  \_.'      "._.-"-..-'`-..-'                 ""--..__..--""\n""")
time.sleep(0.01)

level = int(input("Enter your current level: "))
xp = int(input("Enter your current xp: "))
print("started")

def send_discord_message(webhook_url, message, level, gained_xp):
    current_time = datetime.now().strftime('%H:%M')
    
    payload = {
        "username": "Game Stats",
        "avatar_url": "https://i.imgur.com/Fh6qHCE.png",  # URL of the bot's icon
        "embeds": [{
            "color": random.randint(0, 0xFFFFFF),
            "fields": [
                {"name": "Game", "value": f"```{matches_found}```", "inline": True},
                {"name": "Boost Since", "value": f"```{int(hours)}h:{int(minutes)}m:{int(seconds)}s```", "inline": True},
                {"name": "Rank", "value": f"```{level}```", "inline": True},
                {"name": "Progress", "value": f"```{xp}/5000```", "inline": True},
                {"name": "Gained XP", "value": f"```{gained_xp}```", "inline": True},
            ],
            "thumbnail": {"url": level_images[level]}  # This line includes the appropriate level image
        }],
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        raise ValueError(f"Request to Discord returned an error {response.status_code}, the response is:\n{response.text}")


def ErrorFound():
    global ErrorsCount
    error_message = f'wstawaj kurwa server sie skonczyl  <@950839011323289610>'
    print(error_message)
    payload = {
        "username": "GXP - logger",
        "avatar_url": "https://i.imgur.com/Fh6qHCE.png",  # URL of the bot's icon
        "embeds": [{
            "title": "Error Message",
            "description": error_message,
            "color": 0xFF0000,  # Red color to indicate an error
        }],
    }
    response = requests.post("https://discord.com/api/webhooks/1112019607998447706/wwl1kFOdNKnOztu4_Fw5w9j09dZ1D8o_YBoSIV1yIfaGDAemw4kewUklQS8PTJp6aKa1", json=payload)
    if response.status_code != 204:
        raise ValueError(f"Request to Discord returned an error {response.status_code}, the response is:\n{response.text}")
    
    ErrorsCount += 1

while True:
    time.sleep(0.1)
    screenshot = pag.screenshot()

    OKButton = pag.locate("C:/Users/kacpe/Desktop/nouserlogon-fix-main/img/ok.png", screenshot, confidence=0.8)
    wonmatch = pag.locate("C:/Users/kacpe/Desktop/nouserlogon-fix-main/img/scaut.png", screenshot, confidence=0.8)
    kill11 = pag.locate("C:/Users/kacpe/Desktop/nouserlogon-fix-main/img/11.png", screenshot, confidence=0.8)
    kill10 = pag.locate("C:/Users/kacpe/Desktop/nouserlogon-fix-main/img/10.png", screenshot, confidence=0.8)
    kill9 = pag.locate("C:/Users/kacpe/Desktop/nouserlogon-fix-main/img/9.png", screenshot, confidence=0.8)

    if OKButton is not None:
        ErrorFound()
        xp_gain = 0
        found_kill = False
        time.sleep(30)
    elif wonmatch is not None and found_kill:
        xp += xp_gain
        matches_found += 1
        if xp >= 5000:
            level += 1
            xp -= 5000
        elapsed_time = datetime.now() - start_time
        elapsed_time_in_seconds = elapsed_time.total_seconds()
        hours, remainder = divmod(elapsed_time_in_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        match_message = f"Match logged to discord"
        print(match_message)
        send_discord_message("https://discord.com/api/webhooks/1112051968412762253/ftVxn2P3L1hgkmmFWwJPsnW6Akv2IlyNihoPcB-ScU67XESDbU8GS1GL0nU4-WqilHVG", f"Game:\n```{matches_found}```\nStart Time:\n```{int(hours)}h:{int(minutes)}m:{int(seconds)}s```\nRank:\n```{level}```\nProgres:\n```{xp}/5000```", level, xp_gain)
        xp_gain = 0
        found_kill = False
        time.sleep(30)
    elif not found_kill:
        if kill11 is not None:
            print("11")
            found_kill = True
            xp_gain = 117
            time.sleep(100)
        if kill10 is not None:
            print("10")
            found_kill = True
            xp_gain = 114
            time.sleep(100)
        if kill9 is not None:
            print("9")
            found_kill = True
            xp_gain = 110
            time.sleep(100)



