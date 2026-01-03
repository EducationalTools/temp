import os
import threading
import webbrowser
import time

print("Downloading EduTools")
os.system("git clone -j 8 https://github.com/EducationalTools/EducationalTools.github.io.git edutools")

ROOT = "./edutools"
URL  = "http://localhost:3000"

os.chdir(ROOT)

threading.Thread(
    target=lambda: os.system("pnpx serve -l 3000 -s . > /dev/null"),
    daemon=True
).start()

input("Server running. Press Enter to open in browser…")
webbrowser.open(URL)

try:
    while True:
        threading.Event().wait()
except KeyboardInterrupt:
    print("\nShutting down…")