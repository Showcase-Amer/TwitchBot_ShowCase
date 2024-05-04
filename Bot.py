import webbrowser
import requests
#import Game
from http.server import BaseHTTPRequestHandler, HTTPServer
from twitchio.ext import commands





#variable
hostName = "localhost"
serverPort = 17563
url ="https://id.twitch.tv/oauth2/authorize?response_type=code&client_id=This-Is-Blacked-Out&redirect_uri=http://localhost:17563&scope=chat%3Aread&state=3252342"
client_id = "This-Is-Blacked-Out"
client_secret = "This-Is-Blacked-Out" #if this is getting replaced, why not make an empty string?
global Token
Token = ""

test= []

#Locathost server part
class MyServer(BaseHTTPRequestHandler):

    code ="SSS"
    reponse_data=""

    def do_GET(self, ):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.wfile)
        self.wfile.write(bytes("<html><head><title>QSimulator</title></head>", "utf-8"))
        self.wfile.write(bytes("<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Start The Mini Game</a>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

        response = self.path
        if "code" in response:
            MyServer.code = response
            splittedList = MyServer.code.split('=')
            for item in splittedList:
                if "&scope" in item:
                    MyServer.code = item.replace("&scope", "")
                    print("The code is : " + MyServer.code)
                    client_id = "This-Is-Blacked-Out"
                    client_secret = "This-Is-Blacked-Out"

                    headers = {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    }
                    data = f'client_id={client_id}&client_secret={client_secret}&code={MyServer.code}&grant_type=authorization_code&redi' \
                           f'rect_uri=http://localhost:17563'

                    response = requests.post('https://id.twitch.tv/oauth2/token', headers=headers, data=data)
                    MyServer.response_data = response.json()
                    global Token
                    Token = MyServer.response_data["access_token"]
                    print("the token is : " + MyServer.response_data["access_token"])



class client(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=Token, prefix='?', initial_channels=[Channel])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...

        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return


        if message.content =="hello":
            print("Hello Lovely")

        # Print the contents of our message to console...
        print(str(message.timestamp) +" " +str(message.author.name)+" : "+str(message.content))

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    #@commands.command()
   # async def join(self, ctx: commands.Context):
        #change the player_v1 to be random
      #  Game.playerlist.append(Game.Player(ctx.author.name, 'Player_V1.png').nickname)
      #  print(*Game.playerlist)



def TrueToken():
    return Token == ""


if __name__ := 'Bot':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    Channel = input("What is your Channel : ")
    # open new tab to the local server
    webbrowser.open_new(url)
    while TrueToken():
        webServer.handle_request()
    print("Server stopped.")

    # print(f"You Connected to {Channel}'s Channel")
    client = client()
    client.run()
    #PygameTest.Game()

    print("GG")
    # The code will be in the log
