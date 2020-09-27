import requests,json,os,time,sys,re
from colorama import Fore, init, Style
init(convert = True)
os.system("title Account Clean")
bottle1 = f"""





{Fore.CYAN}
                             .```````````                                     
                           /dd`          ```                                  
                           -os-.``         `.`                                
                               -.::.          ..                              
                              .--:-.sosso .````                               
                              :/:` `hddddo.                                   
                              .`    /+/+:/.                                   
                                    :--/:--:                                  
                                    ///oo+++/                                 
                                    :+++s++++-                                
                                    /+++s+++++`                               
                                   `/+++o+++++/                               
                                  -+++++{Fore.RED}oo{Fore.CYAN}+++++-                              
                                 :++++{Fore.RED}oosso{Fore.CYAN}+++++                              
                                :++{Fore.RED}oyhyyyyyys{Fore.CYAN}+++:                             
                                o+{Fore.RED}ohyyyyyyyyyy{Fore.CYAN}+++`                            
                               `++{Fore.RED}yyyyyyyyyyyyy{Fore.CYAN}++:                            
                               .++{Fore.RED}hyyyyyyyyyyyh{Fore.CYAN}+++                            
                                ++{Fore.RED}hyyyyyyyyyyyys{Fore.CYAN}++`                           
                                o+{Fore.RED}yyyyyyyyyyyyys{Fore.CYAN}++-                           
                                ++{Fore.RED}syyyyyyyyyyyyy{Fore.CYAN}++:                           
                                /++{Fore.RED}yyyyyyyyyyyys{Fore.CYAN}++:                           
                                -++{Fore.RED}oyyyyyyyyyyy{Fore.CYAN}+++:                           
                                 ++++{Fore.RED}syyyyyhys{Fore.CYAN}++++-                           
                                 :++++++{Fore.RED}oo{Fore.CYAN}++++++++                            
                                 `+++++++++++++++.                            
                                   .-::::::::-.`                                                     
"""                        
bottle2 = f"""






{Fore.CYAN}
                      .`  `                                                
                    ` `   `  `                                             
                  `   `   ` `.  `                                          
                     `  `       `                                          
                  `     ` `    .  `--.``````                               
                     `   ``  `  ` -dd:     `````                           
                  `   `  `   `  ```:+-.        `.                          
                      `   ``  ` `     :--`       .`                        
                  `` `   ``          `-::-.``     `.                       
                    ` . ``   .       `//`shhyy`.````-                      
                         .            :: syyyh/`                           
                     `       `          .:://::`                           
                       ``              `:--/:---                           
                                       .+++s++++                           
                                       /+++s++++`                          
                                     `./++oo++++-                          
                                   `-/++++oo++++:                          
                                  -/++++++s+++++:                          
                                 :++osyyyyyso+++/                          
                                -++{Fore.RED}yyyyyyyyyys{Fore.CYAN}+++                          
                                ++{Fore.RED}yyyyyyyyyyyy{Fore.CYAN}+++                          
                               .+oh{Fore.RED}yyyyyyyyyyyo{Fore.CYAN}++                          
                               /+s{Fore.RED}yyyyyyyyyyyyo{Fore.CYAN}++                          
                               ++{Fore.RED}yyyyyyyyyyyyh{Fore.CYAN}++/                          
                              .++{Fore.RED}yyyyyyyyyyyyy{Fore.CYAN}++:                          
                              -++{Fore.RED}yyyyyyyyyyyys{Fore.CYAN}++.                          
                              :++{Fore.RED}oyyyyyyyyyyy{Fore.CYAN}+++                           
                              /+++{Fore.RED}oyyyyyyyys{Fore.CYAN}+++-                           
                              :++++++{Fore.RED}ooooo{Fore.CYAN}++++/                            
                              `://+++++++++++/`                            
                                 `.-:://///:-                             
                              
"""
logo = """
 █████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝
███████║██║     ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   
██╔══██║██║     ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   
██║  ██║╚██████╗╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   
                                                             
 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗███████╗██████╗    
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔════╝██╔══██╗   
██║     ██║     █████╗  ███████║██╔██╗ ██║█████╗  ██████╔╝   
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗   
╚██████╗███████╗███████╗██║  ██║██║ ╚████║███████╗██║  ██║   
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝   
                                                             
"""







print(bottle1)
time.sleep(0.1)
os.system("cls")
print(bottle2)
time.sleep(0.1)
os.system("cls")
print(bottle1)
time.sleep(0.1)
os.system("cls")
print(bottle2)
time.sleep(0.1)
os.system("cls")
print(bottle1)
time.sleep(0.1)
os.system("cls")
print(bottle2)
time.sleep(0.1)
os.system("cls")
print(bottle1)
time.sleep(0.1)
os.system("cls")
print(bottle2)
time.sleep(0.1)
os.system("cls")


print(Fore.CYAN)
print(logo)
token = input("[!] Account token:")
token = token.replace('"',"")#some people paste their token straight from discord - this will include the " " - this simple line of code removes the " "
print(f"{Fore.CYAN}[+] Validating Token...")
time.sleep(0.1)
validate = requests.get("https://canary.discordapp.com/api/v6/users/@me", headers={'authorization': token}).status_code


if validate == 200:
    print(f"{Fore.GREEN}[+] VALID.")
    time.sleep(1.5)
else:
    print(f"{Fore.RED}[-] INVALID.")
    input("[-] Press Enter To Quit\n[-] ")
    sys.exit(0)













def convoclean():
    headers = {'Authorization': token}
    resp = requests.get("https://discord.com/api/v8/users/@me/channels",headers=headers)
    data = json.loads(resp.text)
    deleted = int(0)

    for i in range(len(data)):
        convodeletion = requests.delete(f"https://discord.com/api/v8/channels/{data[i]['id']}",headers=headers).status_code
        if convodeletion == 200:
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}DM Conversation Cleared!")
            deleted += 1
            os.system(f"title Deleted {deleted} Conversations!")
        else:
            print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Error Deleting DM Conversation!")#most likely ratelimited/invalid token
        time.sleep(1)#idc if it slows it down - its better to not get the account locked and wait rather then lose it all
    print(f"[+] Conversations Cleared! {deleted} Conversations Deleted")
       
    

def serverclean():
    headers = {'Authorization': token}
    resp = requests.get("https://discord.com/api/v8/users/@me/guilds",headers=headers)
    data = json.loads(resp.text)
    deleted = int(0)

    for i in range(len(data)):
        serverleaving = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{data[i]['id']}",headers=headers).status_code
        #print(serverleaving)
        if serverleaving == 204:
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Server Left")
            deleted += 1
            os.system(f"title Left {deleted} Servers!")
        else:
            print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Error Leaving Server!")#most likely ratelimited/invalid token
        time.sleep(1)#idc if it slows it down - its better to not get the account locked and wait rather then lose it all
    print(f"[+] Conversations Cleared! {deleted} Conversations Deleted")
       



def friendpendclean():
    ids = []
    success = 0
    headers = {
        'authorization': token,
    }

    friends = requests.get('https://discordapp.com/api/v6/users/@me/relationships', headers=headers)
    if '401: Unauthorized' not in friends.text:
        types = re.findall(r'"id": "\w{18}", "type": \w{1}', friends.text)
    else:
        pass

    for type_ in types:
        if ': 3' in type_:
            ids.append(type_)

    if len(ids) != 0:
        for id_ in ids:
            id_raw = id_.split('"id": "')[1].split('", "')[0]
            decline = requests.delete('https://discord.com/api/v6/users/@me/relationships/%s' % (id_raw), headers=headers)
            if decline.status_code == 204:
                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Denied Incoming Friend Request")
                success = success + 1
            else:
                print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Error Declining Friend Request!")
    
        if success != 1:
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Declined {success} Friend Requests")
        else:
            print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Declined 1 Friend Request")
    else:
        print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE}No Incoming Friend Requests To Clear')



def outgoingcancel():
        ids = []
        success = 0
        headers = {
            'authorization': token,
        }

        friends = requests.get('https://discordapp.com/api/v6/users/@me/relationships', headers=headers)
        if '401: Unauthorized' not in friends.text:
            types = re.findall(r'"id": "\w{18}", "type": \w{1}', friends.text)
        else:
            pass

        for type_ in types:
            if ': 4' in type_:
                ids.append(type_)

        if len(ids) != 0:
            for id_ in ids:
                id_raw = id_.split('"id": "')[1].split('", "')[0]
                decline = requests.delete('https://discord.com/api/v6/users/@me/relationships/%s' % (id_raw), headers=headers)
                if decline.status_code == 204:
                    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Cancelled Outgoing Friend Request")
                    success = success + 1
                else:
                    print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Error Declining Friend Request!")
    
            if success != 1:
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Cancelled {success} Friend Requests")
            else:
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Declined 1  Friend Request")
        else:
            print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE}No Friend Requests To Cancel')


def allfriendremove():
        ids = []
        success = 0
        headers = {
            'authorization': token,
        }

        friends = requests.get('https://discordapp.com/api/v6/users/@me/relationships', headers=headers)
        if '401: Unauthorized' not in friends.text:
            types = re.findall(r'"id": "\w{18}", "type": \w{1}', friends.text)
        else:
            pass

        for type_ in types:
            if ': 1' in type_:
                ids.append(type_)

        if len(ids) != 0:
            for id_ in ids:
                id_raw = id_.split('"id": "')[1].split('", "')[0]
                decline = requests.delete('https://discord.com/api/v6/users/@me/relationships/%s' % (id_raw), headers=headers)
                if decline.status_code == 204:
                    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}Removed Friend")
                    success = success + 1
                else:
                    print(f"{Fore.WHITE}[{Fore.RED}+{Fore.WHITE}] {Fore.RED}Error Removing Friend")
    
            if success != 1:
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Removed {success} Friends")
            else:
                print(f"{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}Removed 1  Friend")
        else:
            print(f'{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE}No Friends To Remove')

os.system("cls")
menu = f"""
{Fore.CYAN}[{Fore.WHITE}1{Fore.CYAN}]{Fore.WHITE} = Clear All Conversations And Leave All Groups.
{Fore.CYAN}[{Fore.WHITE}2{Fore.CYAN}]{Fore.WHITE} = Leave All Servers.
{Fore.CYAN}[{Fore.WHITE}3{Fore.CYAN}]{Fore.WHITE} = Remove ALL Friends.
{Fore.CYAN}[{Fore.WHITE}4{Fore.CYAN}]{Fore.WHITE} = Remove ALL Incoming Friend Requests.
{Fore.CYAN}[{Fore.WHITE}5{Fore.CYAN}]{Fore.WHITE} = Remove ALL Outgoing Friend Requests.
{Fore.CYAN}[{Fore.WHITE}6{Fore.CYAN}]{Fore.WHITE} = FULL CLEAN!
"""   

print(menu)
choice = input("[>] = ")
if choice == "1":
    convoclean()
elif choice == "2":
    serverclean()
elif choice == "3":
    allfriendremove()
elif choice == "4":
    friendpendclean()
elif choice == "5":
    outgoingcancel()
elif choice == "6" or choice.lower() == "all":
    convoclean()
    serverclean()
    allfriendremove()
    friendpendclean()
    outgoingcancel()




