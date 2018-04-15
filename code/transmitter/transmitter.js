
var http = require('http');
var url = require('url');

var net = require('net');
var client = new net.Socket();

http.createServer(function (req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Request-Method', '*');
  res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET');
  res.setHeader('Access-Control-Allow-Headers', '*');
  res.writeHead(200, {'Content-Type': 'application/json'});
  if ( req.method === 'OPTIONS' ) {
    res.writeHead(200);
    res.end();
    return;
  }
  var q = url.parse(req.url, true).query;
  console.log('oui');

  var txt = ("test" + q.ID);
/*
  client.connect(8060, 'localhost', function() {
    console.log('Connected');
    client.write('GETMAP');
  });

  client.on('data', function(data) {
    console.log('Received: ' + data);
    res.end(data);
    // client.destroy(); // kill client after server's response
  });

  client.on('close', function() {
    console.log('Connection closed');
    client.destroy();
  });*/

  res.write(txt);

  res.end();

}).listen(8070);
