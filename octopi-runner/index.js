import receiveMessage from "./receive-message.js";

const checkIntervalSeconds= 1

setInterval(receiveMessage, checkIntervalSeconds * 1000)