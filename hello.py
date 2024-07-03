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
        @import url('https://fonts.googleapis.com/css2?family=Rubik+Bubbles&display=swap');
/* BODY */
body {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background-color: skyblue;
  background-image: -webkit-linear-gradient(90deg, skyblue 0%, steelblue 100%);
  background-attachment: fixed;
  background-size: 100% 100%;
  overflow: hidden;
  font-family: "Rubik Bubbles", system-ui;
  font-weight: 400;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
}

::selection {
  background: transparent;
}
/* CLOUDS */
body:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  width: 0;
  height: 0;
  margin: auto;
  border-radius: 100%;
  background: transparent;
  display: block;
  box-shadow: 0 0 150px 100px rgba(255, 255, 255, 0.6),
    200px 0 200px 150px rgba(255, 255, 255, 0.6),
    -250px 0 300px 150px rgba(255, 255, 255, 0.6),
    550px 0 300px 200px rgba(255, 255, 255, 0.6),
    -550px 0 300px 200px rgba(255, 255, 255, 0.6);
}
/* JUMP */
h1 {
  cursor: default;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100px;
  margin: auto;
  display: block;
  text-align: center;
}

h1 span {
  position: relative;
  top: 20px;
  display: inline-block;
  -webkit-animation: bounce 0.4s ease infinite alternate;
  font-size: 80px;
  color: #fff;
  text-shadow: 0 1px 0 #ccc, 0 2px 0 #ccc, 0 3px 0 #ccc, 0 4px 0 #ccc,
    0 5px 0 #ccc, 0 6px 0 transparent, 0 7px 0 transparent, 0 8px 0 transparent,
    0 9px 0 transparent, 0 10px 10px rgba(0, 0, 0, 0.4);
}

h1 span:nth-child(2) {
  -webkit-animation-delay: 0.4s;
}

h1 span:nth-child(3) {
  -webkit-animation-delay: 0.6s;
}

h1 span:nth-child(4) {
  -webkit-animation-delay: 0.8s;
}

h1 span:nth-child(5) {
  -webkit-animation-delay: 0.10s;
}

h1 span:nth-child(6) {
  -webkit-animation-delay: 0.2s;
}

h1 span:nth-child(7) {
  -webkit-animation-delay: 0.4s;
}

h1 span:nth-child(8) {
  -webkit-animation-delay: 0.6s;
}

h1 span:nth-child(9) {
  -webkit-animation-delay: 0.8s;
}

h1 span:nth-child(10) {
  -webkit-animation-delay: 0.10s;
}

h1 span:nth-child(11) {
  -webkit-animation-delay: 0.12s;
}

h1 span:nth-child(12) {
  -webkit-animation-delay: 0.14s;
}


/* ANIMATION */
@-webkit-keyframes bounce {
  100% {
    top: -20px;
    text-shadow: 0 1px 0 #ccc, 0 2px 0 #ccc, 0 3px 0 #ccc, 0 4px 0 #ccc,
      0 5px 0 #ccc, 0 6px 0 #ccc, 0 7px 0 #ccc, 0 8px 0 #ccc, 0 9px 0 #ccc,
      0 50px 25px rgba(0, 0, 0, 0.2);
  }
}
    </style>
</head>
<body>
    <h1>
  <span>H</span>
  <span>E</span>
  <span>L</span>
  <span>L</span>
  <span>O</span>
</br>
  <span>W</span>
  <span>O</span>
  <span>R</span>
  <span>L</span>
  <span>D</span>
  <span>!</span>
</h1>
</body>
</html>
        '''

        self.wfile.write(html_content.encode('utf-8'))


serv = HTTPServer(('', PORT), HandlerClass)
print(f"HTTP Server started...[{PORT}]")
serv.serve_forever()
