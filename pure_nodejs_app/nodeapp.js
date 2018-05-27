const http = require('http');
const fs = require('fs');
const ejs = require('ejs');
const url = require('url');

const index_page = fs.readFileSync('./index.ejs', 'UTF-8');
const other_page = fs.readFileSync('./other.ejs', 'UTF-8');
const style_sheet = fs.readFileSync('./common.css', 'UTF-8');

var server = http.createServer(getFromClient);

server.listen(3000);
console.log('server start');


function getFromClient(request, response) {
  var url_parts = url.parse(request.url);
//  console.log('access to ' + url_parts.pathname);
  
  switch (url_parts.pathname) {
    case '/':
      var content = ejs.render(index_page, {
        title: 'Index',
        contents: 'Welcome to index page !',
      });
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(content);
      response.end();
      break;
    
    case '/other.ejs':
      var content = ejs.render(other_page, {
        title: 'Other',
        contents: 'Welcome to other page !',
      });
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(content);
      response.end();
      break;
    
    case '/common.css':
      response.writeHead(200, {'Content-Type': 'text/css'});
      response.write(style_sheet);
      response.end();
      break;
      
    default:
      response.writeHead(200, {'Content-Type': 'text/plain'});
      response.end('Page Not Found.');
      break;
  }
}
