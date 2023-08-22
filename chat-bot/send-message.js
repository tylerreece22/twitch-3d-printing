import AWS from 'aws-sdk';
AWS.config.update({region: 'REGION'});
const sqs = new AWS.SQS({apiVersion: '2012-11-05'});
const sendSqsMessage = (params) => sqs.sendMessage(params, function(err, data) {
    if (err) {
        console.log("Error", err);
    } else {
        console.log("Success", data.MessageId);
    }
});

export default sendSqsMessage