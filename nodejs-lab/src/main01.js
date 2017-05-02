var fs = require('fs');

var data = fs.readFileSync("input.txt");
fs.readFile("input.txt",function(err, data){
    console.log('async', data.toString());
});
console.log('sync ',data.toString());
