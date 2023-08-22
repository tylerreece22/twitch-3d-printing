import sendSqsMessage from "./send-message.js";

const {sqs_queue_url} = process.env

const params = {
    // Remove DelaySeconds parameter and value for FIFO queues
    // DelaySeconds: 10,
    MessageAttributes: {},
    MessageBody: 'hello there from local',
    // MessageDeduplicationId: "TheWhistler",  // Required for FIFO queues
    // MessageGroupId: "Group1",  // Required for FIFO queues
    QueueUrl: sqs_queue_url
};

try {
    sendSqsMessage(params)
    console.log('Sent message')
} catch (e) {
    console.log(`Failed to send message: ${e.message}`)
}

// if needed leaving here
// client.say(target, `You rolled a ${num}`);