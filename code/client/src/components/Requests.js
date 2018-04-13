
var net = require('net');
var client = new net.Socket();

console.log("lol");

client.connect(8060, 'localhost', function() {
  console.log('Connected');
  client.write('GETMAP');
});

client.on('data', function(data) {
  console.log('Received: ' + data);
  client.destroy(); // kill client after server's response
});

client.on('close', function() {
  console.log('Connection closed');
});
