import socket
server = "localhost"
port = 6667
channel = "#home"
botnick = "OsintCorpBot"
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(bytes(f"NICK {botnick}\r\n", "UTF-8"))
irc.send(bytes(f"USER {botnick} 0 * :OSINTCORP IRC Bot\r\n", "UTF-8"))
def send_message(message):
    irc.send(bytes(f"PRIVMSG {channel} :{message}\r\n", "UTF-8"))
def send_private_message(user, message):
    irc.send(bytes(f"PRIVMSG {user} :{message}\r\n", "UTF-8"))
def set_channel_topic(topic):
    irc.send(bytes(f"TOPIC {channel} :{topic}\r\n", "UTF-8"))
# Main bot loop
def bot_loop():
    joined = False
    while True:
        response = irc.recv(2048).decode("UTF-8").strip("\r\n")
        if response.startswith("PING"):
            irc.send(bytes(f"PONG {response.split()[1]}\r\n", "UTF-8"))
          
        if " 001 " in response and not joined:
            irc.send(bytes(f"JOIN {channel}\r\n", "UTF-8"))
            joined = True
            send_message("OsintCorpBot has joined the channel.")
            set_channel_topic(new_topic)
        if "JOIN" in response and channel in response:
            nick = response.split("!")[0][1:] 
            send_private_message(nick, "Hello there! I am OsintCorpBot, an open-source IRC bot!")
        if not any(cmd in response for cmd in ['372', '376', '401', '421']):
            print(response)
if __name__ == "__main__":
    bot_loop()
