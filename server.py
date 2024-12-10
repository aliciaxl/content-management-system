from http.server import HTTPServer, BaseHTTPRequestHandler
import json

with open('index.html', 'r') as file:
    html_content = file.read()

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())

def main():
    HOST = 'localhost'
    PORT = 12345
    server = HTTPServer((HOST, PORT), requestHandler)
    print(f'Server listening on localhost:{PORT}')
    server.serve_forever()
    
if __name__ == '__main__':
    main()








