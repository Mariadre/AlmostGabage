const http = require('http');
const url = require('url');
const proc = require('child_process');

var server = http.createServer(getFromClient);

server.listen(3000);
console.log('server start.');


function getFromClient(request, response) {
  var url_parts = url.parse(request.url);
  
  switch (url_parts.pathname) {
    case '/':
      response.end('index');
      break;
      
    case '/iris':
      var spawn = proc.spawn;
      var py = spawn('python', ['iris_classification.py']);
      var data = {
        'sepal_length': 5.84, 
        'sepal_width':  3.05,
        'petal_length': 3.76,
        'petal_width':  1.20,
      };
      var dataString = '';
      var prediction = 'iris'
      
      py.stdout.on('data', function(data) {
        dataString += data.toString();
        console.log('send data to python');
      });
      py.stderr.on('data', function(data) {
        dataString += data.toString();
        console.log('Error:' + dataString);
      });

      py.stdout.on('end', function() {
        prediction = dataString;
        console.log('data from python:' + dataString);
      });
      
      py.stdin.write(JSON.stringify(data));
      py.stdin.end();

      response.end();
      break;
      
    default:
      break;
  }
}

