
import json,requests
from selenium import webdriver


def clear():
   print("\n" * 100)
   startmenu()
print('''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 'o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                              .
''')
print("Welcome To MF Discord TokenLogin                Dev:HO3EINWAVE")
print("")
request = requests.Session()
token = input("Enter Token > ")
headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }


print('''
 [1] Token Info        [2] Login To Token

''')

def tokenLogin(token):
    src = request.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
    if src.status_code == 403:
      print("Token Is Invalid")
      startmenu()
    elif src.status_code == 401:
      print("Token Is Invalid")
      startmenu()
    else:
      opts = webdriver.ChromeOptions()
      opts.add_experimental_option("detach", True)
      driver = webdriver.Chrome('chromedriver.exe', options=opts)
      script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
      driver.get("https://discord.com/login")
      driver.execute_script(script + f'\nlogin("{token}")')

def tokeninfo():
   src = request.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10)
   response = json.loads(src.content)

   if src.status_code == 403:
      print("[*] Token Is Invalid")
      startmenu()
   elif src.status_code == 401:
      print("[*] Token Is Invalid")
      startmenu()
   else:
      print("Token Is Valid")
      infotk = f'''\n   Name: {response['username']}#{response['discriminator']}   ID: {response['id']}\n   Email: {response['email']}   Phone: {response['phone']}\n   Language: {response['locale']}\n'''
      print(infotk)
      startmenu()




def startmenu():
   keywrd = input("Command > ")
   if keywrd == "exit":
      print("Bye !")
      exit()
   elif keywrd == "clear":
      clear()
   elif keywrd == "1":
      tokeninfo()
      startmenu()
   elif keywrd == "2":
      tokenLogin(token)
   else:
      print(" [!] Command Not Found !")
      startmenu()

startmenu()