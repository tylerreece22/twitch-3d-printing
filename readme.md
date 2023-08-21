# Twitch 3d printing
**Note**: Follow [get started docs](https://dev.twitch.tv/docs/irc/get-started/) for more detailed information

## Run bot.js
* Register application on the [developer console](https://dev.twitch.tv/console/apps)
* Download [Twitch CLI](https://dev.twitch.tv/docs/cli/)
* Run `twitch token -u -s 'chat:read chat:edit'`
* Pull access token from terminal
```
Opening browser. Press Ctrl+C to cancel...
2023/08/21 11:47:17 Waiting for authorization response ...
2023/08/21 11:47:18 Closing local server ...
2023/08/21 11:47:19 User Access Token: <your token> 
Refresh Token: <your token>  
Expires At: 2023-08-21 20:08:44.287707 +0000 UTC
Scopes: [chat:edit chat:read]
```
* Export your username and access token `export username=<your username> access_token=<your access token>`
* Run `node chat-bot/bot.js` and you are connected to your chat :)

