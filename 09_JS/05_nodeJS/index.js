const http = require('http');
const port = 3001;

http.createServer((req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/plain',
        // 'Content-Length': res.body.length,
    })
    res.statusCode = 200;
    // res.write('Lunch Time\n');
    res.end('End of response\n');
}).listen(port);

console.log(`Server in runnig @ http://localhost:${port}`);