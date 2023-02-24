from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = 'Hello, World!'
        self.wfile.write(message.encode())

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, Handler)
    print('Server running at localhost:8000')
    httpd.serve_forever()

run()
