import tmi from 'tmi.js';
import sendSqsMessage from "./send-message.js";
import 'dotenv/config'

const {username, access_token, chat_sqs_queue_url} = process.env

console.log('username', username?.length > 0)
console.log('access_token', access_token?.length > 0)
console.log('chat_sqs_queue_url', chat_sqs_queue_url?.length > 0)
const minutes = 30

// Define configuration options
const opts = {
    identity: {
        username,
        password: access_token
    },
    channels: [
        username
    ]
};

// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

// Connect to Twitch:
client.connect();

// Called every time a message comes in
function onMessageHandler(target, context, msg, self) {
    if (self) {
        return;
    }

    // Remove whitespace from chat message
    const chatMessage = msg.trim();
    console.log(`Received chat message ${chatMessage}`)

    const params = {
        // Remove DelaySeconds parameter and value for FIFO queues
        // DelaySeconds: 10,
        MessageAttributes: {},
        MessageBody: chatMessage,
        // MessageDeduplicationId: "TheWhistler",  // Required for FIFO queues
        // MessageGroupId: "Group1",  // Required for FIFO queues
        QueueUrl: chat_sqs_queue_url
    };

    try {
        sendSqsMessage(params)
        console.log('Sent message')
    } catch (e) {
        console.log(`Failed to send message: ${e.message}`)
    }

    // if needed leaving here
    // client.say(target, `You rolled a ${num}`);
}

// Called every time the bot connects to Twitch chat
function onConnectedHandler(addr, port) {
    console.log(`* Connected to ${addr}:${port}`);
}