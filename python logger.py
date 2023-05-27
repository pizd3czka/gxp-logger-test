import pywinauto as pwa
import pygetwindow as pgw
import pyautogui as pag
from datetime import datetime, timedelta
import time
import requests
import random

ErrorsCount = 1
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


level = int(input("          Enter Your Level: "))
xp = int(input("          Enter Your xp: "))

matches_found = 0
start_time = datetime.now()

print("script working :}")


def send_discord_message(webhook_url, message):
    current_time = datetime.now().strftime('%H:%M')
    payload = {
        "username": "GXP - logger",
        "avatar_url": "https://i.imgur.com/Fh6qHCE.png",  # URL of the bot's icon
        "embeds": [{
            "description": f"```\n{message}\n```",
            "color": random.randint(0, 0xFFFFFF),
        }],
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 204:
        raise ValueError(f"Request to Discord returned an error {response.status_code}, the response is:\n{response.text}")


def ErrorFound():
    global ErrorsCount
    error_message = f'[{datetime.now().strftime("%H:%M:%S")}] here type message  here u need to paste ur user id ->  <@950839011323289610>'
    print(error_message)
    send_discord_message("ur discord weebhok", error_message)
    ErrorsCount += 1


while True:
    time.sleep(0.1)
    screenshot = pag.screenshot()

    OKButton = pag.locate("here path to ok.png", screenshot, confidence=0.8)
    wonmatch = pag.locate("here path to scaut.png", screenshot, confidence=0.8)

    if OKButton is not None:
        ErrorFound()
    elif wonmatch is not None:
        xp += 117
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
        send_discord_message("ur discord weebhok", f"🔨Game:\n{matches_found}\n⌚️Start Time:\n{int(hours)}h:{int(minutes)}m:{int(seconds)}s\n🎯Rank:\n{level}\n👴🏻Progres:\n{xp}/5000")
        time.sleep(15)
