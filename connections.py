import requests, random, json, os, easygui, time
from colorama import init, Fore
init(convert=True)

clear = lambda : os.system("cls")


class Connection:
    def __init__(self):
        self = self

    def info(self):

        info = {}

        print(f"{Fore.CYAN} Please select your tokens file {Fore.RESET}")
        time.sleep(1)
        info["tokens"] = "".join(open(easygui.fileopenbox()).readlines()).split("\n")
        clear()
        print(f"{Fore.CYAN} Please input your desired method: [battlenet, skype, lol, contacts] {Fore.RESET}")
        info["option"] = str(input(" > "))
        print(f"{Fore.CYAN} Input the amount of connections {Fore.RESET}")
        info["amount"] = int(input(" > "))
        print(f"{Fore.CYAN} Input the desired name {Fore.RESET}")
        info["name"] = str(input(" > "))
        return json.loads(str(info).replace("'", '"'))

    def start(self):

        information = self.info()

        with requests.Session() as session:

                    for token in information["tokens"]:
                        session.put(f"https://discordapp.com/api/v6/users/@me/connections/skype/{random.randint(1, 10)}", json={ "name": 'icewallowcum',"visibility": 1, "verified": True },headers={"Authorization": token})

                        for _i in range(information["amount"]):
                            req = session.put(f'https://discordapp.com/api/v6/users/@me/connections/{information["option"]}/{random.randint(1, 10)}', 

                            json={
                                        "name": information["name"],
                                        "visibility": 1,
                                        "verified": True
                                },
                            headers={
                                        "Content-Type": "application/json",
                                        "Content-Length": str(len(information["name"])),
                                        "Authorization": token
                                    })

                                
                            try:
                                if json.loads(req.text)["type"]:
                                        print(f"{Fore.GREEN} Successfully added the new connection {Fore.RESET}")
                            except:
                                pass
                    self.quest()

    def quest(self):
            print(f'''
 {Fore.CYAN}[{Fore.RESET}1{Fore.CYAN}]: {Fore.RESET} Add new connection 
 {Fore.CYAN}[{Fore.RESET}2{Fore.CYAN}]: {Fore.RESET} Exit Program 
        ''')

            choice = int(input(" > "))

            if choice == 1:
                clear()
                self.start()
                return

            if choice == 2:
                clear()
                exit()
                return


if __name__ == "__main__":
    Connection().start()
