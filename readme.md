# OsintCorpBot
OsintCorpBot is a simple IRC bot written in Python that connects to a specified IRC server

## Prerequisites

- Python 3.x
- Access to an IRC server (e.g., a local or public IRC server).

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/osintcorpbot.git
   cd osintcorpbot
   ```
2. Ensure you have Python 3.x installed on your machine. If not, install it using your package manager:
   - On Ubuntu:
   ```bash
   sudo apt update
   sudo apt install python3
   ```
## Usage

1. Edit the Bot Configuration: Modify the bot.py file to set the IRC server, port, and channel you want the bot to connect to. The default configuration is set to:
  ```bash
  server = "localhost"
  port = 6667
  channel = "#home"
  botnick = "Nick"
  ```
2. Run the Bot:
  ```bash
  python3 bot.py
  ```
Once the bot is running, it will automatically:

- Connect to the specified IRC server.
- Join the specified channel.

HF-947a10a7f84fb7c6fd353b1ee5f5dd8d
