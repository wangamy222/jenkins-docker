from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 9999

class HandlerClass(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html_content = '''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HI</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        h1 {
	    font-size: 55px;
        }
    </style>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
        '''
        
        self.wfile.write(html_content.encode('utf-8'))


serv = HTTPServer(('', PORT), HandlerClass)
print(f"HTTP Server started...[{PORT}]")
serv.serve_forever()
