
from os.path import exists
from os import environ
from sys import exit
from psutil import process_iter
from time import sleep

print("\nSublime Text Activator/Register by Sirox\n")

if not exists(f'{environ["PROGRAMFILES"]}\Sublime Text\sublime_text.exe'):
    print(f'[ERROR] No Sublime executable found. {environ["PROGRAMFILES"]}\Sublime Text\sublime_text.exe not existing')
    exit()

print("[INFO] Searching for conflicts...")

for p in process_iter():
    if p.name() == "sublime_text.exe":
        print("[INFO] Conflict found! Killing sublime_text.exe.")
        p.kill()
        sleep(1)

print("[INFO] Starting modification...")

with open(f'{environ["PROGRAMFILES"]}\Sublime Text\sublime_text.exe', 'rb') as f:
    content = f.read().hex()

if not "807805000f94c1" in content:
    print("[ERROR] Could not activate Sublime. Try reinstalling it and try again.")
    exit()

content = content.replace("807805000f94c1", "c64005014885c9")

if "807805000f94c1" in content:
    print("[ERROR] Could not activate Sublime. Try reinstalling it and try again.")
    exit()

print("[INFO] Successfully modified Sublime Text.")
print("[INFO] Writing executable...")

with open(f'{environ["PROGRAMFILES"]}\Sublime Text\sublime_text.exe', 'wb') as f:
    f.write(bytes.fromhex(content))

print("\n[Success] Successfully registered/activated Sublime Text.")
