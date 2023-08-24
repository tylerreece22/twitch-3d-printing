# Twitch 3d printing
The purpose of this project is to solidify some of the Python, Lambda, and AWS skills I have acquired recently. Anyone in chat will have the ability to specify two coordinates on a chess board (overlayed on a 3d printer bed) and the printer will print a line from coordinate A to B utilizing Python, NodeJS, and message queues. 

Below is a diagram (intentionally overly complex) which shows how I decided to set up the data flow.
![TwitchChatTo3DPrintingWorkflow.png](docs%2FTwitchChatTo3DPrintingWorkflow.png)

## Link to full broadcast
[Twitch stream](https://www.twitch.tv/videos/1905892673)

## Run bot.js
This bot will consume your chat and send all messages to the AWS SQS queue. You can add your own filter here if you want but considering the message limit was 1 million messages, I was unconcerned with cost.

**Note**: Follow [get started docs](https://dev.twitch.tv/docs/irc/get-started/) for more detailed information

* cd to `./chat-bot`
* Run `npm i`
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
* Export your chat_sqs_queue_url from AWS `export chat_sqs_queue_url=<your_sqs_url>`
* Run `poetry install` 
* Run with `node chat-bot/bot.js` or `sh scripts/chat-bot-runner.sh` and you are connected to your chat :)

## Run lambdas/twitch_chat_message_processor
This is the meat of the application which will process all messages in the SQS queue from the chatbot. It will parse the messages and convert them into the appropriate gcode commands for an Ender 3 Pro. After processing, it will send the gcode commands in an array as the body of an message to the SQS queue.

* Create lambda function
* Add IAM service role to Lambda function
* Add trigger to SQS queue so that all messages are sent to the function
* Create additional SQS queue for gcode commands
* Add the `gcode_sqs_message_url` environment variable to the Lambda
* Deploy this code to be used in your function

## Set up Octoprint
This is an opensource image available in the [Raspberry Pi Imager](https://www.raspberrypi.com/software/). This image allows you to control a 3d printer remotely using http://octopi.local on your network. For more information you can look at the [official docs](https://docs.octoprint.org/en/master/). I use this as a quick-n-dirty way to interface with my 3d printer through the Octoprint APIs.

* Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
* Select 'Other specific-purpose OS' -> 3D Printing -> OctoPi -> OctoPi (stable)
* Flash micro USB
* Connect to your printer
* Follow set up instructions

## Run octopi-runner
This is just a basic runner which will poll the SQS queue specified in the env variables and send the gcode commands through your local network to your OctoPi. 

* cd to `./octopi-runner`
* Run `npm i`
* Export SQS url `export gcode_sqs_queue_url=<your sqs url>`
* Run the app with `node ./octopi-runner/index.js` or `sh ./scripts/octopi-runner.sh`

After you are all set up everything should run as expected