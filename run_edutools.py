import os
import http.server
import socketserver
import threading
import webbrowser

os.system("git clone --recurse-submodules -j 8 https://github.com/EducationalTools/EducationalTools.github.io.git edutools")

PORT = 8000
ROOT = "./edutools"
URL  = f"http://localhost:{PORT}"

os.chdir(ROOT)
Handler = http.server.SimpleHTTPRequestHandler
httpd   = socketserver.TCPServer(("", PORT), Handler)

threading.Thread(target=httpd.serve_forever, daemon=True).start()
input("Server running. Press Enter to open in browser…")
webbrowser.open(URL)

try:
    while True:
        threading.Event().wait()
except KeyboardInterrupt:
    print("\nShutting down…")
    httpd.shutdown()
    