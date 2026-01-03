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

print('Starting server...')

time.sleep(10)

input("\n\n\n\n\n\n\n\n\n\nEduTools running, press enter to open")
webbrowser.open(URL)

try:
    while True:
        threading.Event().wait()
except KeyboardInterrupt:
    print("\nShutting down…")