import os

os.system("apachectl -k stop")
print("--[+] Server is stopped ")
os.system("xdg-open 127.0.0.1:8080/")