# EchoBot

EchoBot is a Discord bot designed to retrieve cryptocurrency data and to convert various currencies into their relative satoshi/gwei values. This program is designed to obtain real time data from https://coinmarketcap.com which implements REST APIs. Use either a ! or ? as the command prefix or customize it by changing the source code.

The creator of this program is "jdlee6" and the source for the bot can be found at: https://github.com/jdlee6/EchoBot

How to install/use on Linux (Docker):
1. Install Docker `sudo apt install docker.io`

2. Build Docker Image `sudo docker build -t <image name> <path of project>`
   - Make sure to set environment variables such as Discord Bot Token and Coinmarketcap API key in the Dockerfile

3. To run EchoBot from Docker image `sudo docker run <image name>`

<img src="https://imgur.com/zdAwQlA.png" width="600">

<img src="https://imgur.com/QUE3Nf4.png" width="600">

<img src="https://imgur.com/EN8ZDty.png" width="600">

# Future Implementations:

- [x]Convert amnt of Coin -> USD value
- [x]Color Code % Changes
- [X]Implement Charts (SMAs with Labels)
- [X]Make .json configuration file 
- [X]Implement Docker so installation is quick and efficient
- [ ]Customize Help Box
