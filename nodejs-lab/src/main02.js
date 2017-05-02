var events = require("events");

var eventEmitter = new events.EventEmitter();

eventEmitter.on("connectionEvent", function(){
    console.log("connection connected");
    eventEmitter.emit("data_received");
});

eventEmitter.on("data_received", function(){
    console.log("data received");
});

eventEmitter.emit("connectionEvent");

