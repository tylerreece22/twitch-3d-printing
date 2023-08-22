// Load the AWS SDK for Node.js
import AWS from 'aws-sdk';
import sendCommand from "./send-command-to-octopi.js";
// Set the region
AWS.config.update({region: 'REGION'});
const {sqs_queue_url} = process.env

// Create an SQS service object
const sqs = new AWS.SQS({apiVersion: '2012-11-05'});

const queueURL = sqs_queue_url;

const params = {
    AttributeNames: [
        "SentTimestamp"
    ],
    MaxNumberOfMessages: 10,
    MessageAttributeNames: [
        "All"
    ],
    QueueUrl: queueURL,
    VisibilityTimeout: 20,
    WaitTimeSeconds: 0
};

const receiveMessage = () => sqs.receiveMessage(params, function(err, data) {
    if (err) {
        console.log("Receive Error", err);
    } else if (data.Messages) {
        console.log(`Receivied message ${JSON.stringify(data.Messages[0])}`)
        const gcodeCommands = JSON.parse(data.Messages[0].Body)

        if (gcodeCommands) {
            sendCommand(gcodeCommands)
            console.log(`Sent print line command to pi: ${JSON.stringify(gcodeCommands)}`)
        } else {
            console.log(`Did not send print commands: ${gcodeCommands}`)
        }

        const deleteParams = {
            QueueUrl: queueURL,
            ReceiptHandle: data.Messages[0].ReceiptHandle
        };
        sqs.deleteMessage(deleteParams, function(err, data) {
            if (err) {
                console.log("Delete Error", err);
            } else {
                console.log("Message Deleted", data);
            }
        });
    }
})

export default receiveMessage