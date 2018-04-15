
var http = require('http');
var url = require('url');

var net = require('net');
var client = new net.Socket();

http.createServer(function (req, res) {
  var q = url.parse(req.url, true).query;
  
  var txt = q.year + " " + q.month;

  client.connect(8060, 'localhost', function() {
    console.log('Connected');
    client.write('GETMAP');
  });

  client.on('data', function(data) {
    // console.log('Received: ' + data);
    res.end(data);
    // client.destroy(); // kill client after server's response
  });

  client.on('close', function() {
    console.log('Connection closed');
    client.destroy();
  });

}).listen(8070);
